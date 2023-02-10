# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.urls import path
from .views import newPage, landing3,landing4, landing5,landing6, landing7

urlpatterns = [
    path("new", newPage, name="newpage"),
    path("landing3", landing3, name="landing3"),
    path("landing4", landing4, name="landing4"),
    path("landing5", landing5, name="landing5"),
    path("landing6", landing6, name="landing6"),
    path("", landing7, name="landing7"),
]
