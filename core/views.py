from django.shortcuts import render, HttpResponse

# Create your views here.

def hello(request, nome, idade):
    return HttpResponse('<H1>Hello {}  de  {} anos </H1>'.format(nome, idade))
