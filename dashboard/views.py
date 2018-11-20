from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import auth

@login_required(login_url="/accounts/login")
def dashboard(request):
    user = User.objects;
    if user is not None:
        return render(request, 'dashboard/dashboard.html')
    else:
        return redirect('login')

@login_required(login_url="/accounts/login")
def create(request):
    user = User.objects;
    if user is not None:
        return render(request, 'dashboard/create.html')
    else:
        return redirect('login')