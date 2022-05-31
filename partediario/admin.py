from django.contrib import admin
from .models import *
from django.contrib.auth.admin import UserAdmin


@admin.register(Empresa)
class EmpresaAdmin(admin.ModelAdmin):
    list_display = ["id", "representante", "empresa"]
    list_display_links = ["id", "representante"]
    list_filter = ["inventarios"]
    search_fields = ["categoria"]
    filter_horizontal = ["inventarios"]




admin.site.register(Categoria)
admin.site.register(Entradas)
admin.site.register(entrada)
admin.site.register(salida)
admin.site.register(rotacion)
admin.site.register(recorrida)
admin.site.register(otraActividad)
admin.site.register(Salidas)
admin.site.register(Inventario)
admin.site.register(sanitacion)
admin.site.register(recategorizacion)
admin.site.register(contratistas)
admin.site.register(opcionSanitacion)
admin.site.register(opcionActividad)
admin.site.register(lluvia)


class entradaInLine(admin.TabularInline):
    model = entrada
    fields = ["entradas", "categoria", "cantidad",
              "cantidad_M", "cantidad_H", "pesoTotal"]
    extra = 0


class salidaInLine(admin.TabularInline):
    model = salida
    fields = ["salidas", "categoria_madre", "cantidad", "causa"]
    extra = 0


class recatInLine(admin.TabularInline):
    model = recategorizacion
    fields = ["categoria_inicial", "categoria_final", "cantidad"]
    extra = 0


class rotInLine(admin.TabularInline):
    model = rotacion
    fields = ["potrero_inicial", "potrero_final"]
    extra = 0


class recorridaInLine(admin.TabularInline):
    model = recorrida
    fields = ["potrero", "observacion"]
    extra = 0


class sanitacionInLine(admin.TabularInline):
    model = sanitacion
    fields = ["elemento", "potrero", "observacion"]
    extra = 0


class pesajeInLine(admin.TabularInline):
    model = pesaje
    fields = ["categoria", "cantidad", "peso_minimo", "peso_maximo"]
    extra = 0



class contratistaInLine(admin.TabularInline):
    model = contratistas
    fields = ["trabajos_realizados", "insumos"]
    extra = 0


@admin.register(parteDiario)
class parteDiarioAdmin(admin.ModelAdmin):
    list_display = ["id", "empresa", "fecha", "lluvia"]


class CapatazInline(admin.StackedInline):
    model = Capataz


UserAdmin.inlines = [CapatazInline]
