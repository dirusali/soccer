
from django.contrib import admin
from django.conf.urls import url, include
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^api/', include('scan.urls')),
    url(r'^', include('portal.urls')),
] #+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


admin.site.site_header = 'SOCCERBETS DATOS DE APUESTAS DE FÚTBOL'



