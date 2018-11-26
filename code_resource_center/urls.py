from django.contrib import admin
from django.urls import path, include
import accounts.views
import dashboard.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', dashboard.views.dashboard, name='home'),
    path('dashboard/',include('dashboard.urls')),
    path('accounts/', include('accounts.urls')),
<<<<<<< HEAD
=======
    path('learningresource/', include('learningresource.urls')),
>>>>>>> 1af0b18e979f89ad1f0d315b522c0a5de1041b4d

]
