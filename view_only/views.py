from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
    return HttpResponse("Hello world!!")

def product(request, num1, num2):
    return HttpResponse("<h1>%d × %d = %d</h1>" % (num1, num2, num1*num2))