from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from accounts.models import User
from django.contrib import auth
from .forms import LearningResourceForm
from .models import LearningResource

@login_required(login_url="/accounts/login")
def create(request):
    user = User.objects;
    if user is not None:
        form = LearningResourceForm(request.POST or None)
        if form.is_valid():
            obj = form.save()
            resource = get_object_or_404(LearningResource, pk=obj.id)
            return render(request, 'learningresource/detail.html', {'resource':resource})
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
    return render(request, 'learningresource/detail.html', {'resource':resource})
