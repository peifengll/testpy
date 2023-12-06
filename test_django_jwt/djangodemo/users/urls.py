#!/user/bin/env python3
# -*- coding: utf-8 -*-
from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView
from . import views

urlpatterns = [
    path(r'token/obtain', TokenObtainPairView.as_view(), name="obtain_token"),
    path(r'detail', views.DetailsView.as_view(), name="detail"),
    path(r'login', views.LoginView.as_view(), name="login")
]
