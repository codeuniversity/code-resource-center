from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from accounts.models import User, Profile
from django.contrib import auth
from .forms import LearningResourceForm
from .models import LearningResource, ProfileLearningResource

@login_required(login_url="/accounts/login")
def create(request):
    user = request.user;
    if user is not None:
        form = LearningResourceForm(request.POST or None)
        if form.is_valid():
            resource = form.save()
            ProfileLearningResource.objects.create(profile=user.profile, learningresource=resource)
            context = {
                'resource_id': resource.id
            }
            return redirect('/learningresource/'+ str(resource.id))
        else:
            form = LearningResourceForm()
            context = {
                'form': form
            }
            return render(request,"learningresource/create.html",context)
    else:
        return redirect('login')

def detail(request, resource_id):
    resource = get_object_or_404(LearningResource, pk=resource_id)
    creator = ProfileLearningResource.objects.filter(learningresource=resource_id)
    creator = creator[0].profile.user
    print("THIS IS THE CREATOR UPDATED {}".format(creator))
    context = {
        'resource': resource,
        'creator': creator,
    }
    return render(request, 'learningresource/detail.html', context)
