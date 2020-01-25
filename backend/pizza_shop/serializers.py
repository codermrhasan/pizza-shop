from rest_framework import serializers
from pizza_shop.models import (
    User, Pizza, Order
)

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'id', 'username', 'password', 'phone']
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def create(self, validated_data):
        password = validated_data.pop('password')
        user = User(**validated_data)
        user.set_password(password)
        user.save()
        return user

class PizzaSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Pizza
        fields = ['url', 'id', 'name', 'description', 'price']

class OrderSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Order
        fields = ['url', 'id', 'time', 'user', 'pizza', 'unit']
        extra_kwargs = {
            'user': {'read_only': True}
        }
        