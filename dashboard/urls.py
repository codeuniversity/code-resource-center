from django.urls import path
from . import views
app_name='dashboard'

urlpatterns = [
    path('dashboard', views.dashboard, name='dashboard'),
    path('create', views.create, name ='create')
    path('search', views.searchResult, name='searchResult'),
]
