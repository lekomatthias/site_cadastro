from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('cadastrar/', views.cadastrar_cliente, name='cadastrar_cliente'),
    path('apagar/<int:cliente_id>/', views.apagar_cliente, name='apagar_cliente'),
    path('modificar/<int:cliente_id>/', views.modificar_cliente, name='modificar_cliente'),
    path('interacoes_cliente/', views.interacoes_cliente, name='interacoes_cliente'),
    path('login_admin/', views.login_admin, name='login_admin'),
    path('logout_admin/', views.logout_admin, name='logout_admin'),
    path('listar_clientes/', views.listar_clientes, name='listar_clientes'),
    path('cadastrar_administrador/', views.cadastrar_administrador, name='cadastrar_administrador'),
    path('listar_administradores/', views.listar_administradores, name='listar_administradores'),
    path('apagar_administrador/<str:email>/', views.apagar_administrador, name='apagar_administrador'),
]
