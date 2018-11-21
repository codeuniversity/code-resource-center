from django.shortcuts import render, redirect
from .models import UserType, Department, Institution
from django.contrib.auth.models import User
from django.contrib import auth
from django.contrib.auth.decorators import login_required

def signup(request):
    departments = Department.objects.all
    user_types = UserType.objects.all
    # error = None
    # args = {'usertypes': user_types, 'departments': departments, 'error': 'no error'}
    
    if request.method == "POST":
        if request.POST['password1'] == request.POST['password2']:
            try:
                User.objects.get(username=request.POST['input-username'])
                return render(request, 'signup.html', {'usertypes': user_types, 'departments': departments, 'error': 'Username has already been taken.'})
            except:
                user = User.objects.create_user(request.POST['input-username'], password=request.POST['password1'])
                auth.login(request, user)
                return redirect('dashboard.html')
        else:
            return render(request, 'signup.html', {'usertypes': user_types, 'departments': departments, 'error': 'Passwords must match.' } )
    else:
        return render(request, 'signup.html', {'usertypes': user_types, 'departments': departments, 'error': None} )


    # if request.method == "POST":
    #     # check if passwords match
    #     if request.POST['password'] == request.POST['passwordrepeat']:
    #         try:
    #         # convert email into username
    #             User.objects.get(username=request.POST['username'])
    #             return render(request, 'signup.html', {'error': 'Username has already been taken.'})
    #         except User.DoesNotExist:
    #             username = request.POST['username']
    #             first_name = request.POST['inputFirstName']
    #             # check if valid department
    #             # check if valid study program
    #             first_name = request.P
    #             user = User.objects.create_user(username, password=request.POST['password'])
    #             auth.login(request, user)
    #             # create corresponding crc_user table
    #             return redirect('dashboard')
    #     else:
    #         return render(request, 'signup.html', {'error': 'Passwords must match.'})
    # else:
    #     departments = Department.objects.all
    #     user_types = UserType.objects.all
    #     return render(request, 'signup.html', {'usertypes': user_types, 'departments': departments})
 
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
