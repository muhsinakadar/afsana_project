from django.shortcuts import render

# Create your views here.
def student(request):
    return render(request, "student/student_home.html")