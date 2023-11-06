from django.contrib import admin
from django.urls import path
from senaback import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.login_view, name="login"),
    path('logout/', views.logout_view, name='logout'),
    path('index/', views.index, name="index"),  
    # path('edit/<int:id>/', views.edit_form, name="edit_consumible"),  
    path('elementos_consumibles/', views.list_consumables, name='elementos_consumibles'),
    path('getlist_consumables/', views.get_list_consumables, name="get_list_consumables"),
    path('crear_elemento_consumible/', views.crear_elemento_consumible, name='crear_elemento_consumible'),
    path('list_consumables/', views.list_consumables, name="list_consumables"),
    path('edicion_elemento/<int:id>/', views.Edicion_Elementos_Consumibles, name='Edicion_Elementos_Consumibles'),
    path('editarElemento/',views.editarElemento, name="editarElemento"),

    path('Lista-Devolutivo/', views.obtener_elementos_devolutivos, name='obtener_elementos_devolutivos'),
    path('crear_elemento_devolutivo/', views.crear_elemento_devolutivo, name='crear_elemento_devolutivo'),
    path('Listar_devolutivos/', views.listar_devolutivos, name='Listar_devolutivos'),
    path('obtener_elementos_devolutivos/', views.obtener_elementos_devolutivos, name='obtener_elementos_devolutivos'),

    path('getlist_entregas/', views.getlist_entregas, name="getlist_entregas"),
    path('list_entregas/', views.list_entregas, name="list_entregas"),
    path('crear_entrega/', views.crear_entrega, name='crear_entrega'),

    path('getlist_prestamos/', views.get_list_prestamos, name="getlist_prestamos"),
    path('list_prestamos/', views.list_prestamos, name="list_prestamos"),
    path('crear_prestamo/', views.crear_prestamo, name='crear_prestamo'),
        
    path('usuario/', views.usuario, name="usuario"),
    path('editar_usuario/', views.editar_usuario, name="editar_usuario"),
]   