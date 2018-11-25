from django.urls import path
from . import views
app_name='dashboard'

urlpatterns = [
    path('dashboard', views.dashboard, name='dashboard'),
    path('search', views.searchResult, name='searchResult'),
    path('se_filter', views.filterSoftwareEng, name='SEFilter'),
    path('pm_filter', views.filterProductManagement, name="PMFilter"),
    path('sts_filter', views.filterSTS, name="STSFilter"),
    path('id_filter', views.filterInteractionDesign, name="IDFilter"),
]
