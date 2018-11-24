from django.shortcuts import render, redirect
from .models import UserType, Department, Institution, UserProfile
# from django.contrib.auth.models import User
from django.contrib import auth
from django.contrib.auth.decorators import login_required
# from .forms import UserCreationForm
from .forms import RegisterForm

from .models import User, UserManager

def signup(request):
    form = RegisterForm(request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            try:
                # email must be unique
                email = form.cleaned_data.get('email')
                User.objects.get(username=email)
                context = {
                    'form': form,
                    'error': 'Account already exists.'
                }
                return render(request, 'signup.html', context) 
            except:
                if not email.endswith("@code.berlin"):
                    context = {
                        'form': form,
                        'error': 'User must register with [user]@code.berlin email.'
                    }
                    return render(request, 'signup.html', context )
                form.save()
                username = form.cleaned_data.get('username')
                password = form.cleaned_data.get('password1')
                user = auth.authenticate(username=username, password=password)
                auth.login(request, user)
                return redirect('/dashboard')
    else:
        context = {
            'form': form,
        }
        return render(request, 'signup.html', context)

# def signup(request):
#     user_form = UserSignupForm()
#     if request.method == "POST":
#         f = UserSignupForm(request.POST)
#         print('inside POST request')
#         if f.is_valid():
#             print('after is_valid')
#             try:
#                 User.objects.get(username=f.username)
#                 a_error = f.clean_fname()
#                 b_error = f.valid_email()
#                 c_error = f.password_match()
#                 context = {
#                     'user_form': user_form,
#                     'error': 'Username has already been taken.'
                    
#                 }
#                 print('insidie try')
#                 return render(request, 'signup.html', context )
#             except:
#                 # user = User.objects.create_user(user_form.username, user_form.email, user_form.password1)
#                 # user.first_name = user_form.clean_fname()
#                 # user.last_name = user_form.clean_lname()

#                 f.save()
#                 user = auth.authenticate(username=request.POST['username'], password=request.POST['password'])
#                 auth.login(request, user)
#                 print('inside except')
#                 return redirect('/dashboard')
#         else:
#             print('inside errors')
#             print(f.errors)
#             context = {
#                     'user_form': f,
#                     'error': f.errors

#             }
#             return render(request, 'signup.html', context )
#     else:
#         context = {'user_form': user_form}
#         print('inside get')
#         return render(request, 'signup.html', context)

        # if request.POST['password1'] == request.POST['password2']:
        #     try:
        #         User.objects.get(username=request.POST['input-username'])
        #       
        #     except:
        #        # store user info in User table
        #        user = User.objects.create_user(request.POST['input-username'], request.POST['input-email'], request.POST['password1'])
        #        user.first_name = request.POST['input-first-name']
        #        user.last_name = request.POST['input-last-name']
        #        user.save()
        #         auth.login(request, user)
        #        return redirect('/dashboard')
        # else:
        #     return render(request, 'signup.html', {'error': 'Passwords must match.' } )
    # else:
    #     context = {'user_form': user_form}
    #     return render(request, 'signup.html', context)


 
def login(request):
    if request.method == "POST":
        #the user wants to log in
        user = auth.authenticate(username=request.POST['username'], password=request.POST['password'])
        if user is not None:
            auth.login(request, user)
            return redirect('/dashboard')
        else:
            return render(request, 'login.html', {'error': 'Ooops! Something went wrong. ☹️'})
    else:
        return render(request, 'login.html')

def logout(request):
    #TODO need to route into homepage
    #and don't forget to logout
    if request.method == "POST":
        auth.logout(request)
        return redirect('/accounts/login')
    else:
        return render(request, 'dashboard.html')
