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
