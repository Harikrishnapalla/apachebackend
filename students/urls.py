from django.contrib import admin
from django.urls import path, include
from students.views import testapi

urlpatterns = [
    path('data/', testapi.as_view(),name='data'),
]