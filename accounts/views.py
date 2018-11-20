from django.shortcuts import render, redirect
from .models import UserType, Department, Institution
from django.contrib.auth.models import User
from django.contrib import auth
from django.contrib.auth.decorators import login_required

def signup(request):
    if request.method == 'POST':
        # check if passwords match
        if request.POST['password'] == request.POST['passwordrepeat']:
            try:
                # convert email into username
                # name = 
                User.objects.get(username=request.POST['username'])
                return render(request, 'signup.html', {'error': 'Username has already been taken.'})
            except User.DoesNotExist:
                # check if valid department
                # check if valid study program
                user = User.objects.create_user(request.POST['username'], password=request.POST['password'])
                auth.login(request, user)
                # create corresponding crc_user table
                return redirect('dashboard')
        else:
            return render(request, 'signup.html', {'error': 'Passwords must match.'})
    else:
        user_types = UserType.objects.all
        return render(request, 'signup.html', {'usertypes': user_types})

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
