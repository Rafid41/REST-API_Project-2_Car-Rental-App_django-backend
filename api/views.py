# api\views.py
from django.shortcuts import render
from rest_framework import viewsets
from .models import User, Categories, Cars
from .serializers import UserSerializer, CarsSerializer, CategoriesSerializer
from rest_framework.permissions import IsAuthenticated

# Create your views here.


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class CategoriesViewSet(viewsets.ModelViewSet):
    queryset = Categories.objects.all()
    serializer_class = CategoriesSerializer


class CarsViewSet(viewsets.ModelViewSet):
    queryset = Cars.objects.all()
    serializer_class = CarsSerializer


############### viewSet for Order ############
# class OrderViewSet(viewsets.ModelViewSet):
#     serializer_class = OrderSerializer

#     # if user is not authenticated, he can't view it
#     #permission_classes = [
#     #    IsAuthenticated,
#     #]

#     # filter, urls e api/orders/1  : ehane "1" id, ei id hishebe filter
#     def get_queryset(self):
#         queryset = Order.objects.all()
#         id = self.request.query_params.get("id", None)

#         if id is not None:
#             queryset = queryset.filter(user__id=id)

#         return queryset
