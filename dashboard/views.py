from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from accounts.models import User
# from django.contrib.auth.models import User
from django.contrib import auth
from django.db.models import Count
from django.db.models import Q
from learningresource.models import LearningResource, UserLearningResource

@login_required(login_url="/accounts/login")
def home(request):
    user = User.objects
    learningResources = LearningResource.objects.all()
    if user is not None:
        return render(request, 'dashboard.html', {'learningResources': learningResources})
    else:
        return redirect('login')

@login_required(login_url="/accounts/login")
def searchResult(request):
    query = None
    if 'q' in request.GET:
        query = request.GET.get('q')
        learningResources = LearningResource.objects.filter(Q(title__icontains=query) | Q(description__icontains=query))
        learning
        return render(request, 'dashboard.html', {'query':query, 'learningResources':learningResources})
    else:
        return render(request, 'dashboard.html', {'query':query})


# def getResourceId():
#     learningResources = LearningResource.objects.all()
#     for resource in learningResources:
#         print(resource.id)

def getAuthor(id):
    #id is hardcoded for now
    #TODO: find a way to get the resource id from the template!!
    relations = UserLearningResource.objects.all()
    for relation in relations:
        # print(relation.user, relation.learningresource, relation.user.id)
        if relation.learningresource.id == id:
            result = UserLearningResource.objects.filter(user=relation.user)
            author_firstname = relation.user.first_name.capitalize()
            author_lastname = relation.user.last_name.capitalize()
            return "{} {}".format(author_firstname, author_lastname)

        else:
            return "Unidentified Author"
            # return render(request, 'dashboard.html', {'name': name})
        #     # name = relation.user.first_name.capitalize() + " " + relation.user.last_name.capitalize()
        #     return relation.user.id
        # else:
        #     return "error"

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
