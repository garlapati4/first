from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def srujana(request):
    return HttpResponse('<h1>Srujana Tinnavara,Emi raa vadhilestunava raaa</h1>')


def daddy(request):
    return HttpResponse('<marquee><h1>my daddy is my super hero</h1></marquee>')
