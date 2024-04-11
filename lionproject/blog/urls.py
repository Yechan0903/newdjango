from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('new/',new,name="new"),
    path('create/',create,name = "create"),
    path('<str:id>/',detail, name = "detail"),
    path('edit/<str:id>',edit, name='edit'),
    path('update/<str:id>',update, name="update"),
    path('delete/<str:id>' , delete, name='delete'),
]