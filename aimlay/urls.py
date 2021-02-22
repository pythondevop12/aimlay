from django.contrib import admin
from django.urls import path
from django.urls.conf import  include
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', include('app.urls')),
    path('aim/', include('django.contrib.auth.urls')),
    path('aim/', include('adminapp.urls')),
    path('', include('app.api.urls')),
    path('admin/', admin.site.urls),

]+ static(settings.MEDIA_URL, document_root= settings.MEDIA_ROOT)
