from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def student_show(request):
    x = []
    for i in range(10):
        x.append(i)

    return HttpResponse(f"<h1>Django Tutorials by Wax30d</h1>\nThe Digits are {x}")
