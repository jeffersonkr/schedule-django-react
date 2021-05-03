from django.contrib import admin
from django.urls import path, include
from rest_framework import routers

from core.views import UserViewSet


router = routers.DefaultRouter()
router.register(r"users", UserViewSet)

urlpatterns = [
    path("api-auth/", include("rest_framework.urls")),
    path("", include(router.urls)),
]