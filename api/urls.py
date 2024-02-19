# api\urls.py
from django.urls import path
from rest_framework import routers
from .views import UserViewSet, CategoriesViewSet, CarsViewSet

# default view
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)


router = routers.SimpleRouter()
router.register(r"users", UserViewSet)
router.register(r"cars", CarsViewSet, basename="cars")
router.register(r"categories", CategoriesViewSet, basename="categories")

urlpatterns = [
    path("token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
] + router.urls
