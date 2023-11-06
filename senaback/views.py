from django.shortcuts import render, redirect, get_object_or_404
from django.http.response import JsonResponse, HttpResponse
from .forms import * 
from .models import * 
from django.db.models import Q
from django.utils import timezone
from django.forms import ValidationError
from .models import ElementoConsumible

from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

def login_view(request):
    if request.user.is_authenticated:
        return redirect('index')  # Redirigir a usuarios autenticados a la página de inicio

    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('index')
    else:
        form = AuthenticationForm()

    return render(request, 'senaback/login.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('login')

def recuperar(request):
    if request.user.is_authenticated:
        return redirect('index')
    else:
        return render(request, "senaback/recuperar_contrasena.html")

@login_required
def index(request):
    return render(request, 'senaback/index_main.html')

@login_required
def inicio(request):
    # Tu vista de la página de inicio
    return render(request, 'senaback/index.html')

@login_required
def otorgar_elemento(request):
    return render(request, "senaback/otorgar_elemento.html")

@login_required
def usuario(request):
    return render(request, "senaback/usuario.html")

@login_required
def editar_usuario(request):
    return render(request, "senaback/editar_usuario.html")

# Consumibles
@login_required
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

@login_required
def get_list_consumables(request):
    elementos_consumibles = list(ElementoConsumible.objects.values())
    data = {'consumibles':elementos_consumibles}
    return JsonResponse(data)

@login_required
def list_consumables(request):
    elementos_consumibles = ElementoConsumible.objects.all()
    data = {'consumibles':elementos_consumibles}
    return render(request, 'senaback/index_consumible.html', data)

@login_required
def crear_elemento_consumible(request):
    if request.method == 'POST':
        form = ElementoConsumibleForm(request.POST)
        if form.is_valid():
            form.save()  # Guardar el nuevo elemento consumible en la base de datos
            return redirect('list_consumables')
    else:
        form = ElementoConsumibleForm()
    return render(request, 'senaback/index_consumible.html', {'form': form})


@login_required
def Edicion_Elementos_Consumibles(request, id): 
    # Aqui pueden editar
    if request.method == 'POST':
        _id = request.POST['id']
        nombre_consumible = request.POST['txtnombre_consumible']
        categoria = request.POST['txtcategoria']
        serial = request.POST['txtserial']
        cantidad_total = request.POST['txtcantidad_total']
        valor = request.POST['txtvalor']
        descripcion_elemento = request.POST['txtdescripcion_elemento']
        
        element_cosumible = ElementoConsumible.objects.get(id=_id)
        element_cosumible.nombre_consumible = nombre_consumible
        element_cosumible.categoria = categoria
        element_cosumible.serial = serial
        element_cosumible.cantidad_total = cantidad_total
        element_cosumible.valor = valor
        element_cosumible.descripcion_elemento = descripcion_elemento
        element_cosumible.save()

        return redirect('list_consumables')
    # Aqui pueden obtener y visualizar
    else:
        element_consumible = ElementoConsumible.objects.get(id=id)
        return render(request, "senaback/editarElementos.html", {"element_cosumible": element_consumible})

# Eliminar
@login_required
def editarElemento(request):
    if request.method == 'POST':
        id = request.POST['txtid']
        nombre_consumible = request.POST['txtnombre_consumible']
        categoria = request.POST['txtcategoria']
        serial = request.POST['txtserial']
        cantidad_total = request.POST['txtcantidad_total']
        valor = request.POST['txtvalor']
        descripcion_elemento = request.POST['txtdescripcion_elemento']
        
        element_cosumible = ElementoConsumible.objects.get(id=id)
        element_cosumible.nombre_consumible = nombre_consumible
        element_cosumible.categoria = categoria
        element_cosumible.serial = serial
        element_cosumible.cantidad_total = cantidad_total
        element_cosumible.valor = valor
        element_cosumible.descripcion_elemento = descripcion_elemento
        element_cosumible.save()
    return redirect('list_consumables')

#devolutivos

@login_required
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


@login_required
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


@login_required
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

@login_required
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

@login_required
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

@login_required
def getlist_entregas(request):
    entregas = list(entrega.objects.values())
    data = {'entregas':entregas}
    return JsonResponse(data)

@login_required
def list_entregas(request):
    entregas = entrega.objects.all()
    elementos_consumibles = ElementoConsumible.objects.all()
    usuarios = Usuario.objects.all()
    data = {'elementos_consumibles':elementos_consumibles , 'entregas':entregas,'usuarios': usuarios }
    return render(request, 'senaback/index_entregas.html', data)

from django.utils import timezone

@login_required
def crear_entrega(request):
    if request.method == 'POST':
        form = EntregaForm(request.POST)
        if form.is_valid():
            elemento_entrega_id = request.POST.get('elemento')  # Cambiar a 'elemento' para coincidir con el nombre del campo en el formulario HTML
            cantidad_entregada = request.POST.get('cantidad')
            responsable_entrega_id = request.POST.get('responsable')  # Cambiar a 'responsable' para coincidir con el nombre del campo en el formulario HTML

            try:
                elemento_entrega = ElementoConsumible.objects.get(pk=elemento_entrega_id)
                responsable_entrega = Usuario.objects.get(pk=responsable_entrega_id)
            except ElementoConsumible.DoesNotExist:
                return HttpResponse("Error: Elemento de entrega no válido")
            except Usuario.DoesNotExist:
                return HttpResponse("Error: Responsable de entrega no válido")

            if int(cantidad_entregada) > elemento_entrega.cantidad_total:
                print("Error: La cantidad entregada excede la cantidad total en stock")
                return HttpResponse("Error: La cantidad entregada excede la cantidad total en stock")

            # Establecer la fecha de entrega en el momento actual
            entrega_nueva = form.save(commit=False)
            entrega_nueva.elemento_entrega = elemento_entrega
            entrega_nueva.responsable_entrega = responsable_entrega
            entrega_nueva.fecha_Entrega = timezone.now()

            elemento_entrega.cantidad_total -= int(cantidad_entregada)
            elemento_entrega.save()
            entrega_nueva.save()
            return redirect('list_entregas')
        else:
            print("Error en el formulario:", form.errors)  # Imprimir errores de validación del formulario
    else:
        form = EntregaForm()

    entregas = entrega.objects.all()
    elementos_consumibles = ElementoConsumible.objects.all()
    usuarios = Usuario.objects.all()
    data = {'elementos_consumibles': elementos_consumibles, 'entregas': entregas, 'usuarios': usuarios, 'form': form}
    return render(request, 'senaback/index_entregas.html', data)
# # Usuarios
# @login_required
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

@login_required
def get_list_prestamos():
    prestamos_data = list(prestamos.objects.values())
    data = {'prestamos': prestamos_data}
    return JsonResponse(data)

@login_required
def list_prestamos(request):
    prestamos_data = prestamos.objects.all()
    data = {'prestamos': prestamos_data}
    return render(request, 'senaback/index_prestamo.html', data)

@login_required
def crear_prestamo(request):
    elementos_devolutivos = ElementoDevolutivo.objects.all()
    usuarios = Usuario.objects.all()
    return render(request, 'senaback/crear_prestamo.html', {'elementos_devolutivos': elementos_devolutivos, 'usuarios': usuarios})