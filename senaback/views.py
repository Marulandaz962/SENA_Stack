from django.shortcuts import render, redirect, get_object_or_404
from django.http.response import JsonResponse, HttpResponse
from .forms import * 
from .models import * 
from django.db.models import Q
from django.utils import timezone
from django.forms import ValidationError
from .models import ElementoConsumible
from .models import ElementoDevolutivo
from django.contrib import messages
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
        cantidad_total = request.POST['txtcantidad_total']
        valor = request.POST['txtvalor']
        descripcion_elemento = request.POST['txtdescripcion_elemento']
        
        element_cosumible = ElementoConsumible.objects.get(id=_id)
        element_cosumible.nombre_consumible = nombre_consumible
        element_cosumible.categoria = categoria
        element_cosumible.cantidad_total = cantidad_total
        element_cosumible.valor = valor
        element_cosumible.descripcion_elemento = descripcion_elemento
        element_cosumible.save()

        return redirect('list_consumables')
    # Aqui pueden obtener y visualizar
    else:
        element_consumible = ElementoConsumible.objects.get(id=id)
        return render(request, "senaback/editarElementos.html", {"element_cosumible": element_consumible})


@login_required


#devolutivos
@login_required

def crear_elemento_devolutivo(request):
    if request.method == 'POST':
        form = ElementoDevolutivoForm(request.POST)
        if form.is_valid():
            form.save()  # Guardar el nuevo elemento consumible en la base de datos
            return redirect('list_devolutivos')
    else:
        form = ElementoDevolutivoForm()
    return render(request, 'senaback/index_devolutivos.html', {'form': form})

@login_required
def Edicion_Elementos_Devolutivos(request, id): 
    # Aqui pueden editar
    if request.method == 'POST':
        print("A ver si edita o no")
        id = request.POST['id']
        nombre_devolutivo = request.POST['txt_nombre_devolutivo']
        categoria_devolutivo = request.POST['txt_categoria_devolutivo']
        serial = request.POST['txt_serial']
        serial_sena = request.POST['txt_serial_sena']
        valor_devolutivo = request.POST['txt_valor_devolutivo']
        descripcion_devolutivo = request.POST['txt_descripcion_devolutivo']
        
        element_devolutivo = ElementoDevolutivo.objects.get(id=id)
        element_devolutivo.nombre_devolutivo = nombre_devolutivo
        element_devolutivo.categoria_devolutivo = categoria_devolutivo
        element_devolutivo.serial = serial
        element_devolutivo.serial_sena = serial_sena
        element_devolutivo.valor_devolutivo = valor_devolutivo
        element_devolutivo.descripcion_devolutivo = descripcion_devolutivo
        element_devolutivo.save()

        return redirect('list_devolutivos')
    # Aqui pueden obtener y visualizar
    else:
        element_devolutivo = ElementoDevolutivo.objects.get(id=id)
        return render(request, "senaback/editar_elementos_devolutivos.html", {"element_devolutivo": element_devolutivo})








@login_required
def get_list_devolutivos(request):
    elementos_devolutivos = list(ElementoDevolutivo.objects.values())
    data = {'devolutivos':elementos_devolutivos}
    return JsonResponse(data)

@login_required
def list_devolutivos(request):
    elementos_devolutivos = ElementoDevolutivo.objects.all()
    data = {'devolutivos':elementos_devolutivos}
    return render(request, 'senaback/index_devolutivos.html', data)

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
        
        def evaluar(datos):
            for campos in datos:
                if campos == None or  '':
                    return False
            return True
            

        cantidad_entregada = request.POST.get('cantidad')
        elemento_entrega_id = request.POST.get('elemento_entrega')
        responsable_entrega_id = request.POST.get('responsable_entrega')
            
        
        evaluacion = [
            cantidad_entregada,
            elemento_entrega_id,
            responsable_entrega_id,
        ]
        
        if evaluar(evaluacion):
            cantidad_entregada = int(request.POST.get('cantidad'))
            elemento_entrega_id = request.POST.get('elemento_entrega')
            responsable_entrega_id = request.POST.get('responsable_entrega')  
            observaciones_cosa = request.POST.get('descripcion')
            
            variable = ElementoConsumible.objects.get(id = elemento_entrega_id)
            variable_suma = variable.cantidad_total

            
            
            elemento_entrega_id = ElementoConsumible.objects.filter(id = elemento_entrega_id)[:1].get()
            responsable_entrega_id = Usuario.objects.filter(id=responsable_entrega_id)[:1].get()
                
            if int(cantidad_entregada) > variable_suma:
                messages.success(request, '¡La acción se realizó con éxito!')
                return redirect ("list_entregas")

                    


            
            fecha_entrega_consumible = timezone.now()
            variable_suma -= cantidad_entregada
            variable.cantidad_total = variable_suma
            variable.save()
            
            guardar = entrega(elemento_entrega = elemento_entrega_id, fecha_Entrega = fecha_entrega_consumible, cantidad = cantidad_entregada,  responsable_entrega = responsable_entrega_id, observaciones = observaciones_cosa)
            guardar.save()
            
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