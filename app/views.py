from django.shortcuts import render
from django.http import JsonResponse
from .models import Student
# Create your views here.

def jsondata(request):
    data = list(Student.objects.values())
    return JsonResponse(data,safe = False)
