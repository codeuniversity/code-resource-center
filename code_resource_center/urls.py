from django.contrib import admin
from django.urls import path, include
import accounts.views
import dashboard.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', dashboard.views.dashboard, name='home'),
    path('dashboard/',include('dashboard.urls')),
    path('accounts/', include('accounts.urls')),
]
