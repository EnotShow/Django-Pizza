from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from config import settings

urlpatterns = [
    path('__debug__/', include('debug_toolbar.urls')),
    path('admin/', admin.site.urls),
    path('', include('shopingcart.urls')),
    path('', include('users.urls')),
    path('', include('pizza.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
