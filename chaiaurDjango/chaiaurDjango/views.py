from django.http import HttpResponse
from django.shortcuts import render
def home(request):
    # return HttpResponse("hello")
    return render(request,'index.html')
def about(request):
    return HttpResponse("hello hahahaha")
def contact(request):
    return HttpResponse("hello")
def psit(request):
    return HttpResponse("hello welcome to psit kanpur")
