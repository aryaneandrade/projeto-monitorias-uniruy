from django.contrib import admin
from monitorias.models import Monitoria, Categoria, Beneficio, Inscricao


# Register your models here.
class MonitoriaAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'descricao', 'data', 'categoria', 'beneficio', 'owner', 'vagas')
    search_fields = ('titulo', 'categoria__nome')

class CategoriaAdmin(admin.ModelAdmin):
    list_display = ('nome',)
    search_fields = ('nome',)

class BeneficioAdmin(admin.ModelAdmin):
    list_display = ('nome',)
    search_fields = ('nome',)   

class InscricaoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'email', 'monitoria')
    search_fields = ('nome',)       

admin.site.register(Monitoria, MonitoriaAdmin)
admin.site.register(Categoria, CategoriaAdmin)
admin.site.register(Beneficio, BeneficioAdmin)
admin.site.register(Inscricao, InscricaoAdmin)