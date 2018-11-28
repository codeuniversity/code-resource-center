from django.urls import path, include
from . import views

urlpatterns = [
    path('create', views.create, name ='create'),
    # path('detail', views.detail, name='detail')
    path('<int:resource_id>', views.detail, name='detail'),
]
