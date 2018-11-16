from django.shortcuts import render
from .models import Account

def signup(request):
    return render(request, 'signup.html', {})
