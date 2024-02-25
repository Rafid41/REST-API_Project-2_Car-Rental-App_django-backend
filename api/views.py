# api\views.py
from django.shortcuts import render
from rest_framework import viewsets
from .models import User, Categories, Cars, CarBookingDate
from .serializers import (
    UserSerializer,
    CarsSerializer,
    CategoriesSerializer,
    CarBookingDateSerializer,
)
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status


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

    # create new car entry
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CarBookingDateViewSet(viewsets.ModelViewSet):
    queryset = CarBookingDate.objects.all()
    serializer_class = CarBookingDateSerializer


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
