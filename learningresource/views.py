from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import auth
from django.utils import timezone
from .models import MediaType, LearningResource
from accounts.models import Department
from .forms import LearningResourceForm

# def create(request):
#     form = RawResourceForm()
#     if request.method == 'POST':
#         form = RawResourceForm(request.POST)
#         if form.is_valid():
#             LearningResource.objects.create(**form.cleaned_data)
#     context = {
#         'form': form
#     }
#     return render(request,"learningresource/create.html",context)

def create(request):
    form = LearningResourceForm(request.POST or None)
    if form.is_valid():
        form.save()
        form = LearningResourceForm()
    context = {
        'form': form
    }
    return render(request,"learningresource/create.html",context)


# @login_required(login_url="/accounts/login")
# def create(request):
#     user = User.objects;

#     if user is not None:
#         media = MediaType.objects.all()
#         department = Department.objects.all()
#         display = {
#             'media': media,
#             'department':department
#         }
#         return render(request,"learningresource/create.html", display)
        # If all fields required by database are filled
    #     if request.method == 'POST':
    #         if request.POST['title'] and request.POST['url'] and request.POST['media_type_id'] and request.POST['department_id'] and request.POST['description'] and request.POST['is_free']:
    #             learningresource = LearningResource()
    #             learningresource.title = request.POST['title']
    #             learningresource.description = request.POST['description']
    #             if request.POST['url'].startswith('http://') or request.POST['url'].startswith('https://'):
    #                 product.url = request.POST['url']
    #             else:
    #                 learningresource.url = 'http://' + request.POST['url']
    #             learningresource.media_type_id = request.POST['media_type_id'] 
    #             learningresource.department_id = request.POST['department_id'] 
    #             learningresource.is_free = request.POST['is_free'] 
    #             learningresource.pub_date = timezone.datetime.now()
    #             learningresource.save()
    #             return render(request,"dashboard/dashboard.html",{})
    #         else:
    #             return render(request, 'learningresource/create.html',{'error':'All fields are required.'})
    #     else:
    #         return render(request, 'learningresource/create.html')
    # else:
    #     return redirect('login')

