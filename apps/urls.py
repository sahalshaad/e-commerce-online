"""
URL configuration for celiums project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
from apps.views import *

urlpatterns = [
    path('index/', index, name="index"),
    path('contact/', contact, name="contact"),
    path('signupview/', signupview, name="signupview"),
    path('signupform/', signupform, name="signupform"),
    path('loginview/', loginview, name="loginview"),
    path('loginform/', loginform, name="loginform"),
    path('messege_send/', messege_send, name="messege_send"),
    path('seller_regv/', seller_regv, name="seller_regv"),
    path('seller_reg/', seller_reg, name="seller_reg"),
    path('add_product_view/', add_product_view, name="add_product_view"),
    path('add_product/', add_product, name="add_product"),
    path('list_product/', list_product, name="list_product"),
    path('edit_product/<id>/', edit_product, name="edit_product"),
    path('edit_post/', edit_post, name="edit_post"),
    path('delete_product/<id>/', delete_product, name="delete_product"),
    path('category/', category, name="category"),
    path('discount/<id>/', discount, name="discount"),
    path('add_discount/', add_discount, name="add_discount"),
    path('single_product/', single_product, name="single_product"),
    path('edit_discount/<id>/', edit_discount, name="edit_discount"),
    path('edit_dis_post/', edit_dis_post, name="edit_dis_post"),
]
