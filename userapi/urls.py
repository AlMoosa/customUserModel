from rest_framework import routers
from userapi.views import UserViewSet
from django.urls import path, include

router = routers.DefaultRouter()
router.register('users', UserViewSet)
#
urlpatterns = [
    path('', include(router.urls)),
    path('auth/', include('rest_auth.urls')),
]


# Для использования конечных точек API в вашем веб-сайте/приложении
# необходимо добавить '''?format=json''' к URL-адресу конечной точки,
# чтобы получить необработанный ответ в формате JSON.