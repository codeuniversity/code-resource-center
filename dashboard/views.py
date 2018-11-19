from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import auth

<<<<<<< HEAD
###In the case that django controls the login
# from django.contrib.auth.decorators import login_required

def dashboard(request):
    return render(request, 'dashboard/dashboard.html')

# @login_required
def create(request):
    return render(request, 'dashboard/create.html')
=======
@login_required(login_url="/accounts/login")
def dashboard(request):
    user = User.objects;
    if user is not None:
        return render(request, 'dashboard/dashboard.html')
    else:
        return redirect('login')
>>>>>>> aa330c016b783796118c6c0710627cdbd965b560
