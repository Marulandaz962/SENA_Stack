from django.db import models
#from PIL import image
#from django.contrib.auth.forms import AuthenticationForm
# Create your models here.

class ElementoDevolutivo(models.Model):
    nombre_devolutivo = models.CharField(max_length=25, unique=True)
    categoria_devolutivo = models.CharField(max_length=20)
    serial  = models.CharField(max_length=20)
    serial_sena = models.CharField(max_length=20)
    valor_devolutivo = models.IntegerField()
    descripcion_devolutivo =  models.CharField(max_length= 16)

    def __str__(self):
        return self.nombre_devolutivo


class ElementoConsumible(models.Model):
    nombre_consumible =  models.CharField(max_length=15, unique=True)
    categoria = models.CharField(max_length=25)
    cantidad_total = models.CharField(max_length=15)
    valor = models.IntegerField()
    descripcion_elemento =  models.CharField(max_length=30)

    def __str__(self):
        return self.nombre_consumible


class Usuario(models.Model): 
    #usuarios = models.CharField(max_length=10)
    nombre_usuario = models.CharField(max_length=20, unique=True )
    apellido_1 = models.CharField(max_length=12) 
    apellido_2 = models.CharField(max_length=12)
    tipo_documento = models.CharField(max_length=11)
    numero_documento = models.CharField(max_length=12)
    correo_sena = models.EmailField()
    correo_misena = models.EmailField()
    direccion = models.CharField(max_length=20)
    telefono_1 = models.CharField(max_length=15)
    telefono_2 = models.CharField(max_length=15)
    tipo_contrato = models.CharField(max_length=13)
    fecha_inicio_contrato = models.DateField()
    fecha_fin_contrato = models.DateField()
    #contrasena = models.CharField(max_length=40, null=True, blank=True, default=None)

    def __str__(self):
        return self.nombre_usuario


#CONTRASEÑA Y USUARIO, AMBOS CIFRADOS
class Baja(models.Model):
    elemento_devolutivo = models.ForeignKey(ElementoDevolutivo, on_delete=models.CASCADE, related_name='bajas_elemento_devolutivo')
    serial = models.ForeignKey(ElementoDevolutivo, on_delete=models.CASCADE, related_name='bajas_serial')
    fecha = models.DateField()
    responsable = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name='bajas_responsable')
    Descripcion = models.CharField(max_length=150)

class Garantia(models.Model):
    elemento = models.ForeignKey(ElementoDevolutivo, on_delete=models.CASCADE, related_name='garantias_elemento')
    serial = models.ForeignKey(ElementoDevolutivo, on_delete=models.CASCADE, related_name='garantias_serial')
    fecha = models.DateField()
    responsable = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name='garantias_responsable')
    Descripcion = models.CharField(max_length=150)

class prestamos(models.Model):
    elemento_prestamo = models.ForeignKey(ElementoDevolutivo, on_delete=models.CASCADE, related_name='prestamos_elemento', to_field='nombre_devolutivo')
    responsable_prestamo = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name='prestamos_responsable', to_field='nombre_usuario')
    fecha_Prestamo = models.DateField()
    fecha_Devolucion = models.DateField()
    observaciones = models.TextField(blank=True, null= True)
    estado = models.CharField(max_length=20) # En curso, Finalizado

class entrega(models.Model):
    elemento_entrega = models.ForeignKey(ElementoConsumible, on_delete=models.CASCADE, related_name='entregas_elemento', to_field='nombre_consumible')
    fecha_Entrega = models.DateField(auto_now_add=True)
    cantidad = models.PositiveIntegerField()
    responsable_entrega = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name='entregas_responsable', to_field='nombre_usuario')
    observaciones = models.TextField(blank=True, null= True)
#--------------------------------------------------------------------------------------------------------------------------------------------------------------


class Login(models.Model):
    #rol = models.CharField(max_length=15, default='rol')
    nombre = models.CharField(max_length=50)
    contrasena = models.CharField(max_length=50)
    #token = models.CharField(max_length=50)
    
    
#     def get_list_prestamos():
#     prestamos_data = list(prestamos.objects.values())
#     data = {'prestamos': prestamos_data}
#     return JsonResponse(data)

# def list_prestamos(request):
#     prestamos_data = prestamos.objects.all()
#     data = {'prestamos': prestamos_data}
#     return render(request, 'senaback/index_prestamo.html', data)

# def crear_prestamo(request):
#     elementos_devolutivos = ElementoDevolutivo.objects.all()
#     usuarios = Usuario.objects.all()
#     return render(request, 'senaback/crear_prestamo.html', {'elementos_devolutivos': elementos_devolutivos, 'usuarios': usuarios})