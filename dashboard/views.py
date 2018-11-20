from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import auth
from django.utils import timezone

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
        # If all fields required by database are filled
        if request.method == 'POST':
            if request.POST['title'] and request.POST['url'] and request.POST['media_type_id'] and request.POST['department_id'] and request.POST['description'] and request.POST['is_free']:
                learningresource = LearningResource()
                learningresource.title = request.POST['title']
                learningresource.description = request.POST['description']
                if request.POST['url'].startswith('http://') or request.POST['url'].startswith('https://'):
                    product.url = request.POST['url']
                else:
                    learningresource.url = 'http://' + request.POST['url']
                learningresource.media_type_id = request.POST['media_type_id'] # Fix
                learningresource.department_id = request.POST['department_id'] # Fix
                learningresource.is_free = request.POST['is_free'] # Fix
                learningresource.pub_date = timezone.datetime.now()
                learningresource.save()
                return render(request,"dashboard/dashboard.html",{})
            else:
                return render(request, 'dashboard/create.html',{'error':'All fields are required.'})
        else:
            return render(request, 'dashboard/create.html')
    else:
        return redirect('login')