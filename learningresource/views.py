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
            form.save()
            form = LearningResourceForm()
        context = {
            'form': form
        }
        return render(request,"learningresource/create.html",context)
        #return redirect('/learningresource/' + str(resource_id))
    else:
        return redirect('login')

# @login_required(login_url="/accounts/login")
# def detail(request, id):
#     user = User.objects;
#     if user is not None:
#         obj = get_object_or_404(LearningResource, id=id)
#         context = {
#             "object": obj
#         }
#     return render(request, "learningresource/detail.html", context)


# def detail(request):
#     # obj = get_object_or_404(LearningResource)
#     # context = {
#     #     "object": obj
#     # }
#     queryset = LearningResource.objects.all() # list of objects
#     context = {
#         "object_list": queryset
#     }
#     return render(request, "learningresource/detail.html", context)







def detail(request, resource_id):
    resource = get_object_or_404(LearningResource, pk=resource_id)
    return render(request, 'learningresource/detail.html', {'resource':resource})

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
