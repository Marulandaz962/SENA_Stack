from django.contrib import admin
from django.urls import path
from senaback import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.login, name="login"),
    path('index/', views.index, name="index"),  
    path('edit/<int:id>/', views.edit_form, name="edit_consumible"),  
    path('elementos_consumibles/', views.list_consumables, name='elementos_consumibles'),
    path('getlist_consumables/', views.get_list_consumables, name="get_list_consumables"),
    path('crear_elemento_consumible/', views.crear_elemento_consumible, name='crear_elemento_consumible'),
    path('list_consumables/', views.list_consumables, name="list_consumables"),


    path('Lista-Devolutivo/', views.obtener_elementos_devolutivos, name='obtener_elementos_devolutivos'),
    path('crear_elemento_devolutivo/', views.crear_elemento_devolutivo, name='crear_elemento_devolutivo'),
    path('Listar_devolutivos/', views.listar_devolutivos, name='Listar_devolutivos'),
    path('obtener_elementos_devolutivos/', views.obtener_elementos_devolutivos, name='obtener_elementos_devolutivos'),

    path('Lista_entregas/', views.obtener_entregas, name='Listar_entregas'),  
]
