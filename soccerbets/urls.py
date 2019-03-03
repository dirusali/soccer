
from django.contrib import admin
from django.conf.urls import url, include
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('admin/', admin.site.urls),
]


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^api/', include('scan.urls'))
] #+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^api/', include('scan.urls'))
] # + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

admin.site.site_header = 'SOCCERBETS DATOS DE APUESTAS DE FÚTBOL'



