from django.shortcuts import render

###In the case that django controls the login
# from django.contrib.auth.decorators import login_required

def dashboard(request):
    return render(request, 'dashboard/dashboard.html')

# @login_required
def create(request):
    return render(request, 'dashboard/create.html')
