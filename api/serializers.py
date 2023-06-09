from django.contrib.auth.models import User, Group
from .models import Product, ProductInstance
from rest_framework import serializers


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']


class ProductSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Product
        fields = ['url', 'name', 'category']


class ProductInstanceSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ProductInstance
        fields = ['url', 'product', 'user']

