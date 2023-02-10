from django.urls import path

from parentapp import views

urlpatterns = [
path('', views.parent),
]