from django.shortcuts import get_object_or_404
from rest_framework import generics, viewsets
from rest_framework.response import Response

from pizza_shop.serializers import (
    UserSerializer, User,
    PizzaSerializer, Pizza,
    OrderSerializer, Order
)
from pizza_shop.permissions import AccountPermission, ViewOnly
from rest_framework.permissions import IsAuthenticated

class UserViewSet(viewsets.ModelViewSet):
    permission_classes=(AccountPermission, )
    serializer_class = UserSerializer
    queryset = User.objects.all()

class PizzaViewSet(viewsets.ModelViewSet):
    permission_classes = (ViewOnly, )
    serializer_class = PizzaSerializer
    queryset = Pizza.objects.all()

class OrderViewSet(viewsets.ModelViewSet):
    serializer_class = OrderSerializer
    permission_classes = (IsAuthenticated, )
    def get_queryset(self):
        return Order.objects.filter(user=self.request.user)
    
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)