from django.shortcuts import render
from django.contrib.auth.decorators import login_required


# Create your views here.
@login_required(login_url='/student/login')
def exam(request):
    return render(request, 'student/exam.html')

@login_required(login_url='/student/login')
def lab(request):
    return render(request, 'student/lab.html')

@login_required(login_url='/student/login')
def profile(request):
    return render(request, 'student/profile.html')

@login_required(login_url='/student/login')
def resources(request):
    return render(request, 'student/resources.html')

