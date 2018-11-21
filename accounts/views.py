from django.shortcuts import render, redirect
from .models import UserType, Department, Institution, UserProfile
from django.contrib.auth.models import User
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm

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
                # store user info in User table
                user = User.objects.create_user(request.POST['input-username'], request.POST['input-email'], request.POST['password1'])
                user.first_name = request.POST['input-first-name']
                user.last_name = request.POST['input-last-name']
                user.save()
                
                # create corresponding UserProfile row
                # userprofile = UserProfile.objects.get(pk=user.id)
                # get user_type from form
                # user_type = request.POST['role-select']
                # userprofile.user_type_id = user_type
                
                # get study program from form
                # userprofile.departments.add()

                # department = request.POST['role-select']
                # userprofile.user_type_id = user_type
                # save new data in UserProfile table
                # userprofile.save()
                # login user and redirect to dashboard
                auth.login(request, user)
                return redirect('/dashboard')
        else:
            return render(request, 'signup.html', {'usertypes': user_types, 'departments': departments, 'error': 'Passwords must match.' } )
    else:
        return render(request, 'signup.html', {'usertypes': user_types, 'departments': departments, 'error': None} )

 
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
