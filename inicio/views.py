from django.shortcuts import render, redirect

# from django.http import HttpResponse
# from django.template import loader

from inicio.models import Celular, Tablet, Accesorio
from inicio.forms import CrearCelularFormulario, CrearTabletFormulario, CrearAccesorioFormulario, BusquedaCelularFormulario
# from inicio.forms import CrearPaletaFormulario, BusquedaPaletaFormulario

def inicio(request):
    
    # v2
    # template = loader.get_template('inicio.html')
    # template_renderizado = template.render({})
    
    # return HttpResponse(template_renderizado)
    
    # v3
    return render(request, 'inicio/inicio.html', {})

# def paletas(request):
    
#     paleta = Paleta(marca='wilson', descripcion='pala de Giorgio', anio=2020)
#     paleta.save()
    # v1
    # marca_a_buscar = request.GET.get('marca')
    
    # if marca_a_buscar:
    #     listado_de_paletas = Paleta.objects.filter(marca__icontains=marca_a_buscar)
    # else:
    #     listado_de_paletas = Paleta.objects.all()
    
    # v2
#     formulario = BusquedaPaletaFormulario(request.GET)
#     if formulario.is_valid():
#         marca_a_buscar = formulario.cleaned_data.get('marca')
#         listado_de_paletas = Paleta.objects.filter(marca__icontains=marca_a_buscar)
    
#     formulario = BusquedaPaletaFormulario()


    # return render(request, 'inicio/paletas.html', {'paleta': paleta})


def celulares(request):
    formulario_celular = BusquedaCelularFormulario(request.GET)
    if formulario_celular.is_valid():
        marca_a_buscar = formulario_celular.cleaned_data.get('marca')
        listado_de_celulares = Celular.objects.filter(marca__icontains=marca_a_buscar)
    formulario_celular = BusquedaCelularFormulario()
    return render(request, 'inicio/celulares_dispo.html', {'formulario_celular' : formulario_celular ,'listado_de_celulares' : listado_de_celulares})


def crear_celular(request):  
        
    if request.method == 'POST':        
        formulario = CrearCelularFormulario(request.POST)
        # if formulario.is_valid():
        # info_limpia = formulario.cleaned_data
        marca = request.POST.get('marca')
        modelo = request.POST.get('modelo')
        descripcion = request.POST.get('descripcion')
        anio = request.POST.get('anio')
        celular = Celular(marca=marca, modelo=modelo, descripcion=descripcion, anio=anio)
        celular.save()     
    formulario = CrearCelularFormulario()
    return render(request, 'inicio/celulares.html', {'formulario_cel': formulario})
    


def crear_tablet(request):  
        
    if request.method == 'POST':        
        formulario = CrearTabletFormulario(request.POST)
        # if formulario.is_valid():
        # info_limpia = formulario.cleaned_data
        marca = request.POST.get('marca')
        modelo = request.POST.get('modelo')
        descripcion = request.POST.get('descripcion')
        anio = request.POST.get('anio')
        tablet = Tablet(marca=marca, modelo=modelo, descripcion=descripcion, anio=anio)
        tablet.save()     
    formulario = CrearTabletFormulario()
    return render(request, 'inicio/tablets.html', {'formulario_tab': formulario})



def crear_accesorio(request):  
        
    if request.method == 'POST':        
        formulario = CrearAccesorioFormulario(request.POST)
        # if formulario.is_valid():
        # info_limpia = formulario.cleaned_data
        tipo_producto = request.POST.get('tipo_producto')
        color = request.POST.get('color')
        marca = request.POST.get('marca')
        descripcion = request.POST.get('descripcion')
        accesorio = Accesorio(tipo_producto=tipo_producto, color=color, marca=marca, descripcion=descripcion)
        accesorio.save()     
        
    formulario = CrearAccesorioFormulario()
    return render(request, 'inicio/accesorios.html', {'formulario_acc': formulario})





# def tablets(request):
    
#     tablet = Tablets(marca='samsung', modelo='galaxy' , descripcion='tablet de Giorgio', anio=2022)
#     tablet.save()
#     return render(request, 'inicio/tablets.html', {})



# def crear_paleta(request):
    
    # v1 (HTML)
    # # print('==============')
    # # print('GET')
    # # print(request.GET)
    # # print('==============')
    # # print('POST')
    # # print(request.POST)
    
    # if request.method == 'POST':
    #     marca = request.POST.get('marca')
    #     descripcion = request.POST.get('descripcion')
    #     anio = request.POST.get('anio')
        
    #     paleta = Paleta(marca=marca, descripcion=descripcion, anio=anio)
    #     paleta.save()
    
    # v2 (Django Forms)
    # if request.method == 'POST':
    #     formulario = CrearPaletaFormulario(request.POST)
    #     if formulario.is_valid():
    #         info_limpia = formulario.cleaned_data
            
    #         marca = info_limpia.get('marca')
    #         descripcion = info_limpia.get('descripcion')
    #         anio = info_limpia.get('anio')
    
    #         paleta = Paleta(marca=marca.lower(), descripcion=descripcion, anio=anio)
    #         paleta.save()
            
    #         return redirect('paletas')
    #     else:
    #         return render(request, 'inicio/crear_paleta.html', {'formulario': formulario})
        
    # formulario = CrearPaletaFormulario()
    # return render(request, 'inicio/crear_paleta.html', {'formulario': formulario})



