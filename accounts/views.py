from django.shortcuts import render, redirect, get_object_or_404
from .models import User, UserManager, Department, Profile
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from .forms import (
    RegisterForm, 
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
def profile(request):
    # request user info
    if request.method == "POST":
        user_form = UpdateUserForm(request.POST or None, instance=request.user)
        if user_form.is_valid():
            # check if correct email domain
            email = user_form.cleaned_data.get('email')
            if not email.endswith("@code.berlin"):
                context = {
                    'user_form': user_form,
                    'error': 'You can only login with your code email.'
                }
                return render(request, 'profile.html', context )
            else:
                user_form.save()
                context = {
                    'user_form': user_form,
                    'success': 'Profile info changed successfully.'
                }
                return render(request, 'profile.html', context) 
        else:
            context = {
                'user_form': user_form,
                'error': 'Invalid user info.'
                }
            return render(request, 'profile.html', context) 
    else:        
        user_form = UpdateUserForm(instance=request.user)
        context = {
            'user_form': user_form,
        }
        return render(request, 'profile.html', context) 

# to change user, profile and ProfileDepartment
@login_required(login_url="/accounts/login")
def change_password(request):
    # request user info
    if request.method == "POST":
        user_instance = request.user
        form = PasswordChangeForm(data=request.POST, user=user_instance)
        if form.is_valid():
            form.save()
            # login user with new password TO DO!!!
            update_session_auth_hash(request, form.user)
            return redirect('/accounts/profile')
        else:
            return redirect('/accounts/profile')
    else:        
        user_instance = request.user
        form = PasswordChangeForm(user=user_instance)
        context = {
            'form': form,
        }
        return render(request, 'change_password.html', context) 

    #     if user_form.is_valid():
    #         print('Inside form valid')
    #         try:
    #             # email must be unique
    #             email = user_form.cleaned_data.get('email')
    #             user = User.objects.get(email=email)
    #             context = {
    #                 'user_form': user_form,
    #                 'error': 'Account already exists.'
    #             }
    #             print('Inside try')
    #             return render(request, 'profile.html', context)
    #         except User.DoesNotExist:
    #             # email must user code.berlin domain
    #             if not email.endswith("@code.berlin"):
    #                 context = {
    #                     'user_form': user_form,
    #                     'error': 'User must register with [user]@code.berlin email.'
    #                 }
    #                 print('Not code email.')
    #                 return render(request, 'profile.html', context )

    #             # check if confirmation password is correct
    #             password_confirm = user_form.cleaned_data.get('password_confirm')

    #             if user_instance.check_password(password_confirm):
    #                 print('After check password.')
    #                 user_instance.first_name = user_form.cleaned_data.get('first_name')
    #                 user_instance.last_name = user_form.cleaned_data.get('last_name')
    #                 user_instance.email = user_form.cleaned_data.get('email')
    #                 user_instance.save()
    #             user = auth.authenticate(username=email, password=password_confirm)
    #             if user is not None:
    #                 auth.login(request, user)
    #                 # context = {
    #                 #     'user_form': user_form,
    #                 #     'success': 'User info successfully changed.'
    #                 # }
    #                 # return render(request, 'profile.html', context)
    #                 return redirect('/accounts/profile')
    #             else:
    #                 return render(request, 'profile.html', {'error': 'Ooops! Something went wrong. ☹️'})
    #     else:
    #         context = {
    #             'user_form': user_form,
    #         }
    #         return render(request, 'profile.html', context )
    # else:
    #     context = {
    #         'user_form': user_form,
    #         'user_instance': user_instance
    #     }
    #     return render(request, 'profile.html', context)

