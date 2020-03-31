from rest_framework import routers
from userapi.views import UserViewSet
from django.urls import path, include

router = routers.DefaultRouter()
router.register('users', UserViewSet)
#
urlpatterns = [
    path('', include(router.urls)),
]