from dataclasses import field, fields
from rest_framework import serializers
from partediario.models import *


class EmpresaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Empresa
        fields = '__all__'


class parteDiarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = parteDiario
        fields = '__all__'


class InventarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Inventario
        fields = '__all__'


class CategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categoria
        fields = '__all__'


class LluviaSerializer(serializers.ModelSerializer):
    class Meta:
        model = lluvia
        fields = '__all__'


class EntradaSerializer(serializers.ModelSerializer):
    class Meta:
        model = entrada
        fields = '__all__'


class SalidaSerializer(serializers.ModelSerializer):
    class Meta:
        model = salida
        fields = '__all__'


class TipoEntradaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Entradas
        fields = '__all__'


class TipoSalidaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Salidas
        fields = '__all__'


class RecategorizacionSerializer(serializers.ModelSerializer):
    class Meta:
        model = recategorizacion
        fields = '__all__'


class RecorridoSerializer(serializers.ModelSerializer):
    class Meta:
        model = recorrida
        fields = '__all__'


class RotacionSerializer(serializers.ModelSerializer):
    class Meta:
        model = rotacion
        fields = '__all__'


class SanitacionSerializer(serializers.ModelSerializer):
    class Meta:
        model = sanitacion
        fields = '__all__'


class ContratistasSerializer(serializers.ModelSerializer):
    class Meta:
        model = contratistas
        fields = '__all__'


class OpcionSantiacionSerializer(serializers.ModelSerializer):
    class Meta:
        model = opcionSanitacion
        fields = '__all__'
