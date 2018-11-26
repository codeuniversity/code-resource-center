<<<<<<< HEAD
from django.urls import path
from . import views
app_name='dashboard'

urlpatterns = [
    path('dashboard', views.dashboard, name='dashboard'),
    path('search', views.searchResult, name='searchResult'),
    path('filter_se', views.filterSoftwareEng, name='SEFilter'),
    path('filter_pm', views.filterProductManagement, name="PMFilter"),
    path('filter_sts', views.filterSTS, name="STSFilter"),
    path('filter_id', views.filterInteractionDesign, name="IDFilter"),
]
=======
from django.urls import path, include
>>>>>>> 1af0b18e979f89ad1f0d315b522c0a5de1041b4d
