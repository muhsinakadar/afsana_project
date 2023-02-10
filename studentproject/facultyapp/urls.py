from django.urls import path

from facultyapp import views

urlpatterns = [
    path('', views.faculty),
]