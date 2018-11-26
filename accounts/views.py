from django.shortcuts import render, redirect
from .models import User, UserManager, UserType, Department, Institution, UserProfile
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from .forms import RegisterForm

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
                email = form.cleaned_data.get('email')
                password = form.cleaned_data.get('password1')
                user = auth.authenticate(username=email, password=password)
                auth.login(request, user)
                return redirect('/dashboard')
        else:
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
            return redirect('/dashboard/dashboard')
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
