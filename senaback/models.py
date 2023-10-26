from django.db import models
#from PIL import image
#from django.contrib.auth.forms import AuthenticationForm
# Create your models here.

class ElementoDevolutivo(models.Model):
    nombre_devolutivo = models.CharField(max_length=25)
    categoria_devolutivo = models.CharField(max_length=20)
    serial_devolutivo  = models.CharField(max_length=20)
    cantidad_devolutivo_total = models.CharField(max_length=15)
    descripcion_devolutivo =  models.CharField(max_length= 16)
    valor_devolutivo = models.IntegerField()


class ElementoConsumible(models.Model):
    nombre =  models.CharField(max_length=15, unique=True)
    categoria = models.CharField(max_length=20)
    serial = models.CharField(max_length=20, unique=True)
    cantidad_total = models.CharField(max_length=15)
    valor = models.IntegerField()
    descripcion_elemento =  models.CharField(max_length=30)

    def __str__(self):
        return self.nombre


class Usuario(models.Model): 
    #usuarios = models.CharField(max_length=10)
    nombre = models.CharField(max_length=12)
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

class prestamo(models.Model):
    elemento = models.ForeignKey(ElementoDevolutivo, on_delete=models.CASCADE, related_name='prestamos_elemento')
    serial = models.ForeignKey(ElementoDevolutivo, on_delete=models.CASCADE, related_name='prestamos_serial')
    cantidad = models.IntegerField()
    responsable = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name='prestamos_responsable')
    fecha_Prestamo = models.DateField()
    fecha_Devolucion = models.DateField()
    estado = models.CharField(max_length=20) # En curso, Devuelto, No devuelto

class entrega(models.Model):
    elemento = models.ForeignKey(ElementoConsumible, on_delete=models.CASCADE, related_name='entregas_elemento', to_field='nombre')
    serial = models.ForeignKey(ElementoConsumible, on_delete=models.CASCADE, related_name='entregas_serial', to_field='serial')
    cantidad = models.IntegerField()
    responsable = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name='entregas_responsable', to_field='id')

#--------------------------------------------------------------------------------------------------------------------------------------------------------------


class Login(models.Model):
    #rol = models.CharField(max_length=15, default='rol')
    nombre = models.CharField(max_length=50)
    contrasena = models.CharField(max_length=50)
    #token = models.CharField(max_length=50)