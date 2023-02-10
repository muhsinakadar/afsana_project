from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def faculty(request):
    return render(request,"faculty/faculty_home.html")
