from django.shortcuts import render, HttpResponse

# Create your views here.

def hello(request, nome, idade):
    return HttpResponse('<H1>Hello {}  de  {} anos </H1>'.format(nome, idade))

def somar(request, valor1, valor2):
    soma = valor1 + valor2
    return HttpResponse('A soma dos valores é : {}'.format(soma))

def subtrair(request, valor1, valor2):
    subtracao = valor1 - valor2
    return HttpResponse('Asubtracao dos valores é : {} '.format(subtracao))

def dividir(request, valor1, valor2):
    divisao = valor1 / valor2
    return HttpResponse('A divisao dos valores é: {}'.format(divisao))

def multiplicar(request, valor1, valor2):
    multiplicacao = valor1 * valor2
    return HttpResponse('A multiplicacao dos valores é : {}'.format(multiplicacao))
