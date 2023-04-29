from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from rest_framework import permissions
from .serializers import UserSerializer, GroupSerializer, ProductSerializer, ProductInstanceSerializer
from .models import Product, ProductInstance


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]


class ProductViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows products to be viewd or edited
    """
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class ProductInstanceViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows all product instance to be viewed or edited
    """
    queryset = ProductInstance.objects.all()
    serializer_class = ProductInstanceSerializer