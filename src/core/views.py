from django.http import HttpResponse
from django.shortcuts import render


def saludar(request):
    return HttpResponse("Hola desde Django!")

def saludar_con_etiqueta(request):
    return HttpResponse("<h1> Este es el título de mi App </h1>")

def saludar_con_parametros(request, nombre: str, apellido: str): 
        nombre = nombre.capitalize()
        apellido = apellido.capitalize()
        return HttpResponse(f"{apellido}, {nombre}")

def index(request):
     context = {"año": 2024}
     return render(request, "core/index.html", context)


def ejercicio1(request):
     nombre = 'Federico'
     apellido = 'Servian'
     return render(request, "core/Ejercicio1.html", {'nombre': nombre, 'apellido': apellido})

def ver_notas(request):
     lista_notas = [10, 8, 3, 7, 4, 5, 8]
     return render(request, 'core/notas.html', {'notas': lista_notas})

def ver_usuarios(request):
     lista_usuarios = [ {'Nombre': 'Juan', 'Email': 'juan@django'},
        {'Nombre': 'Santiago', 'Email': 'santi@django'},
        {'Nombre': 'Agustín', 'Email': 'agus@django'}, ]
     return render(request, 'core/Ejercicio2.html', {'usuarios': lista_usuarios})
