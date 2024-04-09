from django.shortcuts import render
from django.http import HttpResponse
from.models import test,demo
# Create your views here.


def tests(request):
    return HttpResponse("hello world")

def html(request):
    
    dict = {
        'title':'database record',
        # 'firstname':'Bhawani',
        # 'lastname':'Patidar',
        'ddata':'Welcome to my django page',

    }
    return render(request,'template.html',dict) 

def bha(request):
    return HttpResponse("admin pannel")

def data(request):
    tests = test.objects.all()
    demos = demo.objects.all()
    data1 = {'tests': tests, 'demos': demos}
    return render(request,'template.html',data1)