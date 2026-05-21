# Rotas do projeto
from django.contrib import admin
from django.urls import path
from monitorias.views import (
    MonitoriaListView,
    MonitoriaInscricaoView,
    MonitoriaInscritoListView,
    NovaMonitoriaCreateView,
    MonitoriaUpdateView,
    MonitoriaDeleteView,
    painel_view,
)
from contas.views import register_view, login_view, logout_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('monitorias/', MonitoriaListView.as_view(), name='monitorias_list'),
    path('monitorias/<int:pk>/inscricao/', MonitoriaInscricaoView.as_view(), name='inscricao_monitoria'),
    path('monitorias/<int:pk>/inscritos/', MonitoriaInscritoListView.as_view(), name='inscritos_monitoria'),
    path('criar_monitoria/', NovaMonitoriaCreateView.as_view(), name='criar_monitoria'),
    path('painel/<int:pk>/editar_monitoria', MonitoriaUpdateView.as_view(), name='editar_monitoria'), 
    path('painel/<int:pk>/excluir_monitoria', MonitoriaDeleteView.as_view(), name='excluir_monitoria'), 
    path('registro/', register_view, name='registro'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('painel/', painel_view, name='painel'),
] 
