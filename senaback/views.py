from django.shortcuts import render, redirect
from django.http.response import JsonResponse
from .forms import ElementoConsumibleForm
from .models import *
from .forms import ElementoDevolutivoForm
from django.db.models import Q
from django.shortcuts import get_object_or_404
from django.http import HttpResponse
from .models import Usuario

def index(request):
    return render(request, 'senaback/index_main.html')

def login(request):
    return render(request, "senaback/login.html")

def otorgar_elemento(request):
    return render(request, "senaback/otorgar_elemento.html")


# Consumibles
def obtener_elementos_consumibles(request):
    elementos_consumibles = ElementoConsumible.objects.all()
    data = []
    for elemento in elementos_consumibles:
        data.append({
            'id': elemento.id,
            'nombre': elemento.nombre_consumible,
            'serial': elemento.serial,
            'cantidad': elemento.cantidad_total,
            'valor': elemento.valor,
            'categoria': elemento.categoria,
            'descripcion': elemento.descripcion_elemento,
        })
    return render(request, 'senaback/index_consumible.html', {'elementos_consumibles': elementos_consumibles})

def get_list_consumables(request):
    elementos_consumibles = list(ElementoConsumible.objects.values())
    data = {'consumibles':elementos_consumibles}
    return JsonResponse(data)

def list_consumables(request):
    elementos_consumibles = ElementoConsumible.objects.all()
    data = {'consumibles':elementos_consumibles}
    return render(request, 'senaback/index_consumible.html', data)


def crear_elemento_consumible(request):
    if request.method == 'POST':
        form = ElementoConsumibleForm(request.POST)
        if form.is_valid():
            form.save()  # Guardar el nuevo elemento consumible en la base de datos
            return redirect('list_consumables')
    else:
        form = ElementoConsumibleForm()
    return render(request, 'senaback/index_consumible.html', {'form': form})

def edit_form(request, id):
    consumible = ElementoConsumible.objects.get(id=id)
    if request.method == 'POST':
        form = ElementoConsumibleForm(request.POST, instance=consumible)
        if form.is_valid():
            form.save()
            return JsonResponse({'message': 'Elemento consumible actualizado exitosamente.'})
        else:
            return JsonResponse({'error': 'Error en el formulario'}, status=400)
    else:
        form = ElementoConsumibleForm(instance=consumible)
        return render(request, 'edit_form.html', {'form': form})



def get_consumable_details(request, consumable_id):
    consumible = get_object_or_404(ElementoConsumible, id=consumible_id)

    data = {
        'nombre_consumible': consumible.nombre_consumible,
        'categoria': consumible.categoria,
        'serial': consumible.serial,
        'cantidad_total': consumible.cantidad_total,
        'valor': consumible.valor,
        'descripcion_elemento': consumible.descripcion_elemento
    }
    
    return JsonResponse(data)

def update_consumable(request):
    if request.method == 'POST':
        consumible_id = request.POST.get('id')
        consumible = get_object_or_404(ElementoConsumible, id=consumible_id)
        
        # Actualiza los campos del elemento consumible
        consumible.nombre_consumible = request.POST.get('nombre_consumibles')
        consumible.categoria = request.POST.get('categoria')
        consumible.serial = request.POST.get('serial')
        consumible.cantidad_total = request.POST.get('cantidad_total')
        consumible.valor = request.POST.get('valor')
        consumible.descripcion_elemento = request.POST.get('descripcion_elemento')
        
        try:
            consumible.full_clean()  # Realiza la validación del modelo
            consumible.save()  # Guarda el elemento consumible
            return JsonResponse({'message': 'Elemento consumible actualizado exitosamente.'})
        except ValidationError as e:
            return JsonResponse({'error': e.message_dict}, status=400)
    else:
        return JsonResponse({'error': 'Método no permitido'}, status=405)

#devolutivos

def obtener_elementos_devolutivos(request):
    elementos_devolutivos = ElementoDevolutivo.objects.all()
    data = []
    for elemento in elementos_devolutivos:
        data.append({
            'id': elemento.id,
            'nombre': elemento.nombre_devolutivo,
            'serial': elemento.serial_devolutivo,
            'cantidad': elemento.cantidad_devolutivo_total,
            'valor': elemento.valor_devolutivo,
            'categoria': elemento.categoria_devolutivo,
            'descripcion': elemento.descripcion_devolutivo,
        })
    return render(request, 'senaback/index_devolutivos.html', {'elemento_devolutivos': elementos_devolutivos})


def listar_devolutivos(request):
    filtro = request.GET.get('filtro', '')  # Obtener el valor del filtro de la URL
    # Utiliza el operador Q para realizar consultas complejas
    elementos_devolutivos = ElementoDevolutivo.objects.filter(
        Q(nombre_devolutivo__icontains=filtro) |  # Filtro por nombre_devolutivo
        Q(serial_devolutivo__icontains=filtro) |  # Filtro por serial_devolutivo
        Q(categoria_devolutivo__icontains=filtro)  # Filtro por categoria_devolutivo
        # Agrega más campos aquí si es necesario
    )
    return render(request, 'senaback/index_devolutivos.html', {'elemento_devolutivos': elementos_devolutivos, 'filtro': filtro})


def crear_elemento_devolutivo(request):
    if request.method == 'POST':
        form = ElementoDevolutivoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index_devolutivos')

    else:
        form = ElementoDevolutivoForm()

    return render(request, 'senaback/index_devolutivos.html', {'form': form})


# Entregas

def obtener_entregas(request):
    entregas = entrega.objects.all()
    data = []
    for entrega in entregas:
        data.append({
            'id': entrega.id,
            'elemento': entrega.elemento_entrega,
            'serial': entrega.serial,
            'cantidad': entrega.cantidad_total,
            'responsable': entrega.valor,
        })
    return render(request, 'senaback/index_entregas.html', {'entregas': entregas})

def obtener_entregas(request):
    entregas = entrega.objects.all()
    data = []
    for entrega in entregas:
        data.append({
            'id': entrega.id,
            'elemento': entrega.nombre,
            'serial': entrega.serial,
            'cantidad': entrega.cantidad_total,
            'responsable': entrega.valor,
        })
    return render(request, 'senaback/index_entregas.html', {'entregas': entregas})

def getlist_entregas(request):
    entregas = list(entrega.objects.values())
    data = {'entregas':entregas}
    return JsonResponse(data)

def list_entregas(request):
    entregas = entrega.objects.all()
    prestamos_tabla
    data = {'entregas':entregas}
    return render(request, 'senaback/index_entregas.html', data)

def crear_entrega(request):
    return render(request, 'senaback/index_entregas.html')
    elementos_consumibles = ElementoConsumible.objects.all()
    usuarios = Usuario.objects.all()
    data = {'elementos_consumibles':elementos_consumibles , 'entregas':entregas,'usuarios': usuarios }
    return render(request, 'senaback/index_entregas.html', data)
    main

def crear_entrega(request):
    entregas = entrega.objects.all()
    elementos_consumibles = ElementoConsumible.objects.all()
    usuarios = Usuario.objects.all()
    prestamos_tabla
    return render(request, 'senaback/index_main.html', {'elementos_consumibles': elementos_consumibles, 'usuarios': usuarios})

# Préstamos

def get_list_prestamos(request):
    prestamo = list(prestamos.objects.values())
    data = {'prestamos':prestamo}
    return JsonResponse(data)

def list_prestamos(request):
    obtener_prestamos = prestamos.objects.all()
    data = {'prestamos':obtener_prestamos}
    return render(request, 'senaback/index_prestamo.html', data)

def crear_prestamo(request):
    prestamo = prestamos.objects.all()
    elementos_devolutivos = ElementoDevolutivo.objects.all()
    usuarios = Usuario.objects.all()
    return render(request, 'senaback/index_main.html', {'elementos_consumibles': elementos_devolutivos, 'usuarios': usuarios})
    data = {'elementos_consumibles':elementos_consumibles , 'entregas':entregas,'usuarios': usuarios }
    return render(request, 'senaback/index_entregas.html', data)
# # Usuarios
# def crear_entrega(request):
#     if request.method == 'GET':
#         elementos_consumibles = ElementoConsumible.objects.all()
#         usuarios = Usuario.objects.all()
#     else:
#         # Aqui es cuando va a editar o actualizar
#         # Debe obtener los datos del frontend y procesar
#         elementos_consumibles = ElementoConsumible.objects.all()
#         usuarios = Usuario.objects.all()
        
    # return render(request, 'senaback/index_entregas.html', {'elementos_consumibles': elementos_consumibles, 'usuarios': usuarios})
   main
