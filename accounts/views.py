from django.shortcuts import render, redirect, get_object_or_404
from .models import User, UserManager, Department, Profile, ProfileDepartment
from django.contrib import auth, messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from .forms import (
    RegisterForm,
    ProfileChangeForm,
    # ProfileDepartmentChangeForm,
    UpdateUserForm, 
)

def signup(request):
    form = RegisterForm(request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            try:
                # email must be unique
                email = form.cleaned_data.get('email')
                user = User.objects.get(email=email)
                context = {
                    'form': form,
                    'error': 'Account already exists.'
                }
                return render(request, 'signup.html', context)
            except User.DoesNotExist:
                if not email.endswith("@code.berlin"):
                    context = {
                        'form': form,
                        'error': 'User must register with [user]@code.berlin email.'
                    }
                    return render(request, 'signup.html', context )
                form.save()
                # authenticate user and log in
                email = form.cleaned_data.get('email')
                password = form.cleaned_data.get('password1')
                user = auth.authenticate(username=email, password=password)
                auth.login(request, user)
                return redirect('/dashboard/home')
        else:
            # Return invalid form with error messages.
            context = {
                'form': form,
            }
            return render(request, 'signup.html', context )
    else:

        context = {
            'form': form,
        }
        return render(request, 'signup.html', context)

def login(request):
    if request.method == "POST":
        #the user wants to log in
        user = auth.authenticate(username=request.POST['email'], password=request.POST['password'])
        if user is not None:
            auth.login(request, user)
            return redirect('/dashboard/home')
        else:
            return render(request, 'login.html', {'error': 'Ooops! Something went wrong. ☹️'})
    else:
        return render(request, 'login.html')

@login_required(login_url="/accounts/login")
def logout(request):
    if request.method == "POST":
        auth.logout(request)
        return redirect('/accounts/login')
    else:
        return render(request, 'dashboard.html')

# to change user, profile and ProfileDepartment
@login_required(login_url="/accounts/login")
def profile_edit(request):
    # request user info
    if request.method == "POST":
        user_form = UpdateUserForm(request.POST or None, instance=request.user)
        profile_form = ProfileChangeForm(request.POST or None, request.FILES, instance=request.user.profile)
        if user_form.is_valid() and profile_form.is_valid():
            # check if correct email domain
            email = user_form.cleaned_data.get('email')
            if not email.endswith("@code.berlin"):
                context = {
                    'user_form': user_form,
                    'profile_form': profile_form,
                    'error': 'You can only login with your code email.'
                }
                return render(request, 'profile.html', context )
            else:
                # success
                user_form.save()
                profile_form.save()
                # avoid showing instance of image in UI
                profile_form = ProfileChangeForm()
                # return a list with all checked departments
                profile_form = ProfileChangeForm()
                context = {
                    'user_form': user_form,
                    'profile_form': profile_form,
                    'success': 'Profile info changed successfully.'
                }
                return render(request, 'profile.html', context) 
        else:
            context = {
                'user_form': user_form,
                'profile_form': profile_form,
                'error': 'Invalid user info.'
                }
            return render(request, 'profile.html', context) 
    else:
        user_form = UpdateUserForm(instance=request.user)
        profile_form = ProfileChangeForm()
        context = {
            'user_form': user_form,
            'profile_form': profile_form,
        }
        return render(request, 'profile.html', context) 

# to change user, profile and ProfileDepartment
@login_required(login_url="/accounts/login")
def change_password(request):
    # request user info
    if request.method == "POST":
        form = PasswordChangeForm(data=request.POST, user=request.user)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            messages.success(request, 'Your password was changed successfully.')
            print("valid form")
            return redirect('/accounts/password')
            # context = {
            #         'success': 'Profile info changed successfully.'
            # }
            # return (request, 'change_password.html', context)
        else:
            messages.error(request, 'Please enter valid password.')
            print("invalid form")
            return redirect('/accounts/password')
    else:        
        form = PasswordChangeForm(request.user)
        context = {
            'form': form,
        }
        return render(request, 'change_password.html', context) 

