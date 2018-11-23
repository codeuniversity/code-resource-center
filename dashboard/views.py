from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from accounts.models import User
# from django.contrib.auth.models import User
from django.contrib import auth

@login_required(login_url="/accounts/login")
def dashboard(request):
    user = User.objects
    if user is not None:
        return render(request, 'dashboard/dashboard.html')
    else:
        return redirect('login')
