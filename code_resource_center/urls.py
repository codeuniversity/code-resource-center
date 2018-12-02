from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
import accounts.views
import dashboard.views
import learningresource.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', dashboard.views.home, name='home'),
    path('dashboard/',include('dashboard.urls')),
    path('accounts/', include('accounts.urls')),
    path('learningresource/', include('learningresource.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
