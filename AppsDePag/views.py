from django.shortcuts import render

from django.http import HttpResponse
from datetime import datetime
from django.template import Template, Context, loader
import random
from AppsDePag.models import MotherBoard



def inicio(request):
    # return HttpResponse("Bienvenidos a mi INICIO!")
    
    return render(request, "AppsDePag/index.html")

def template1(request, nombre, apellido, edad):
    fecha = datetime.now()
    suma = 4 + edad
    return HttpResponse(f"<h1>Este es el template1</h1> -- Fecha: {fecha} -- Hola {nombre} {apellido} {edad}")

def template2(request, nombre, apellido, edad):
    
    archivo_abierto = open(r"C:\Users\Facuhxz'\Desktop\Visual Studio Code\MiEntregaFinal\templates\template.html")
    # archivo_abierto = open("\templates\template2.html")
    
    template = Template(archivo_abierto.read())
    
    archivo_abierto.close()
    
    fecha = datetime.now()
    
    datos = {
            "fecha":fecha,
             "nombre":nombre,
             "apellido":apellido,
             "edad":edad,
             }
    
    contexto = Context(datos)
    
    template_renderizado = template.render(contexto)
    
    
    
    return HttpResponse(template_renderizado)


def template3(request, nombre, apellido, edad):
      
    template = loader.get_template("template.html")
    
    fecha = datetime.now()
    
    datos = {
            "fecha":fecha,
             "nombre":nombre,
             "apellido":apellido,
             "edad":edad,
             }
    
    
    template_renderizado = template.render(datos)
    
    
    
    return HttpResponse(template_renderizado)

def template4(request, nombre, apellido, edad):
      
    
    fecha = datetime.now()
    
    datos = {
            "fecha":fecha,
             "nombre":nombre,
             "apellido":apellido,
             "edad":edad,
             }
    
    
    return render(request,"template.html", datos)

def probando(request):
    
    lista = list(range(500))
       
    numeros = random.choices(lista, k=50)
    
    print(numeros)
       
    return render(request, "probando_if_for.html", {"numeros": numeros})

def creacion_de_mother(request, modelo, marca):
    
    mother = MotherBoard(modelo=modelo, marca=marca)
    
    mother.save()
    
    return render(request, "mothers.template/template_mother.html", {"mother": mother})










