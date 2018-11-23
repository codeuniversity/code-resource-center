from django.urls import path, include
from . import views

urlpatterns = [
    path('create', views.create, name ='create'),
    #path('learningresource/<int:id>/', dynamic_lookup_view, name='view')
    # path('resource_create', views.resource_create, name='resource_create'),
]