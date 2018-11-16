from django.shortcuts import render
from .models import UserType, Department, Institution

def signup(request):
    return render(request, 'signup.html', {})