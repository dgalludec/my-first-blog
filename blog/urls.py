# -*- coding: utf-8 -*-
"""
Created on Fri Jan 22 10:34:06 2021

@author: Multiple Monitors
"""

from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
]