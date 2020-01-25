from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken.views import obtain_auth_token

from pizza_shop.views import *

router = DefaultRouter()
router.register('users', UserViewSet,basename='user')
router.register('pizzas', PizzaViewSet, basename='pizza')
router.register('orders', OrderViewSet, basename='order')

urlpatterns = [
    path('auth/', obtain_auth_token),
    path('', include(router.urls)),
]