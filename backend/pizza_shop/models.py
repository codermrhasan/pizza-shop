from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    phone = models.CharField(max_length=20)

    def __str__(self):
        return self.username

class Pizza(models.Model):
    name = models.CharField(max_length=64)
    description = models.CharField(max_length=128)
    price = models.IntegerField()

    def __str__(self):
        return self.name


class Order(models.Model):
    time = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='orders')
    pizza = models.ForeignKey(Pizza, on_delete=models.CASCADE, related_name='orders')
    unit = models.IntegerField()
    
    def __str__(self):
        return self.user.username