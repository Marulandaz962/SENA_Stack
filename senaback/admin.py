from django.contrib import admin
from .models import Usuario
admin.site.register(Usuario)

from .models import ElementoConsumible
admin.site.register(ElementoConsumible)

from .models import ElementoDevolutivo
admin.site.register(ElementoDevolutivo)

from .models import Baja
admin.site.register(Baja)

# from .models import Garantia
# admin.site.register(Garantia)

# from .models import prestamo
# admin.site.register(prestamo)

from .models import entrega
admin.site.register(entrega)
# Register your models here.

