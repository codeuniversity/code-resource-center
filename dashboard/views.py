from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import auth
from django.db.models import F
from django.db.models import Q
from accounts.models import User
from learningresource.models import LearningResource, ProfileLearningResource

@login_required(login_url="/accounts/login")
def home(request):
    user = User.objects
    learningResources = LearningResource.objects.all().order_by(F('pub_date').desc(nulls_last=True))
    relations = ProfileLearningResource.objects.all().select_related('profile').select_related('learningresource')
    if user is not None:
        return render(request, 'dashboard.html', {'learningResources': learningResources, 'relations': relations,})
    else:
        return redirect('login')

@login_required(login_url="/accounts/login")
def searchResult(request):
    query = None
    if 'q' in request.GET:
        query = request.GET.get('q')
        learningResources = LearningResource.objects.filter(Q(title__icontains=query) | Q(description__icontains=query)| Q(tag__icontains=query)).order_by(F('pub_date').desc(nulls_last=True))
        return render(request, 'dashboard.html', {'query':query, 'learningResources':learningResources})
    else:
        return render(request, 'dashboard.html', {'query':query})

def filterSoftwareEng(request):
    learningResources = LearningResource.objects.filter(department=1)
    return render(request, 'dashboard.html', {'learningResources':learningResources})

def filterProductManagement(request):
    learningResources = LearningResource.objects.filter(department=4)
    return render(request, 'dashboard.html', {'learningResources':learningResources})

def filterSTS(request):
    learningResources = LearningResource.objects.filter(department=2)
    return render(request, 'dashboard.html', {'learningResources':learningResources})

def filterInteractionDesign(request):
    learningResources = LearningResource.objects.filter(department=3)
    return render(request, 'dashboard.html', {'learningResources':learningResources})
