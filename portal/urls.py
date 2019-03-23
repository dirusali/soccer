from django.conf.urls import url
from django.contrib import admin


from .views import partidos

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^partidos/', partidos, name='partidos'),
    
]    
    
