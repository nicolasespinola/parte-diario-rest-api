from django.contrib import admin
from .models import *


@admin.register(Empresa)
class EmpresaAdmin(admin.ModelAdmin):
    list_display = ["id", "representante", "empresa"]
    list_display_links = ["id", "representante"]
    list_filter = ["Inventario_de_Empresa"]
    search_fields = ["categoria"]
    filter_horizontal = ["Inventario_de_Empresa"]


@admin.register(Superficie)
class SuperficieAdmin(admin.ModelAdmin):
    list_display = ["id", "empresa", "has_totales", "has_utiles", "actividad"]
    autocomplete_fields = ["empresa"]


admin.site.register(Categoria)
admin.site.register(Entradas)
admin.site.register(Salidas)
admin.site.register(Inventario)
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


class otroInLine(admin.TabularInline):
    model = otraActividad
    fields = ["categoria", "cantidad", "actividad_realizada"]
    extra = 0


class contratistaInLine(admin.TabularInline):
    model = contratistas
    fields = ["trabajos_realizados", "insumos"]
    extra = 0


@admin.register(parteDiario)
class parteDiarioAdmin(admin.ModelAdmin):
    list_display = ["id", "empresa", "fecha", "lluvia"]
    inlines = [otroInLine]
