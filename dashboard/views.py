from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import auth
from learningresource.models import LearningResource
from django.db.models import Q

@login_required(login_url="/accounts/login")
def dashboard(request):
    user = User.objects;
    if user is not None:
        return render(request, 'dashboard.html')
    else:
        return redirect('login')

def searchResult(request):
    learning_resources = None
    query = None
    if 'q'in request.GET:
        query = request.GET.get('q')
        learning_resources = LearningResource.objects.all().filter(Q(title__icontains=query)| Q(department__icontains=query))
        return render(request, 'search.html', {'query': query, 'learningResources': learning_resources})
