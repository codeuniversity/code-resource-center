from django.contrib import admin
from django.urls import path, include
import accounts.views
import dashboard.views
<<<<<<< HEAD

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', dashboard.views.dashboard, name='home'),
=======
import learningresource.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', dashboard.views.home, name='home'),
>>>>>>> 5e0abb5b891be46b7ff9d32b8a09bdefa045013a
    path('dashboard/',include('dashboard.urls')),
    path('accounts/', include('accounts.urls')),
]
