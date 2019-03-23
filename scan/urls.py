from rest_framework import routers
from . import views
from django.conf.urls import url, include
from django.contrib.auth import views as auth_views

from .views import postmodelview


router = routers.DefaultRouter()
router.register(r'teams', views.TeamViewSet)
router.register(r'matches', views.MatchViewSet)


urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^login/$',auth_views.LoginView.as_view(template_name="useraccounts/login.html"), name="login")
    url(r'^apuestas/ apuestas, name=apuestas)

]
