from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import auth
from django.db.models import Q
from learningresource.models import LearningResource, UserLearningResource


@login_required(login_url="/accounts/login")
def dashboard(request):
    user = User.objects;
    learningResources = LearningResource.objects.all()
    if user is not None:
        return render(request, 'dashboard.html', {'learningResources': learningResources})
    else:
        return redirect('login')

def searchResult(request):
    query = None
    if 'q' in request.GET:
        query = request.GET.get('q')
        learningResources = LearningResource.objects.filter(Q(title__icontains=query) | Q(description__icontains=query))
        return render(request, 'dashboard.html', {'query':query, 'learningResources':learningResources})
    else:
        return render(request, 'dashboard.html', {'query':query})
