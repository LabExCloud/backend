from django.shortcuts import render

# Create your views here.
def exam(request):
    return render(request, 'student/exam.html')

def lab(request):
    return render(request, 'student/lab.html')

def profile(request):
    return render(request, 'student/profile.html')

def resources(request):
    return render(request, 'student/resources.html')