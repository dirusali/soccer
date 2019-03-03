
from rest_framework import routers
from . import views
from django.conf.urls import url, include
from django.contrib.auth import views as auth_views



router = routers.DefaultRouter()
router.register(r'teams', views.TeamViewSet)
router.register(r'matches', views.MatchViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url( r'^login/$',auth_views.LoginView.as_view(template_name="useraccounts/login.html"), name="login")

]
