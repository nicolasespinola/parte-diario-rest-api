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


class CapatazSerializer(serializers.ModelSerializer):
    class Meta:
        model = Capataz
        fields = '__all__'


class EntradaWriteSerializer(serializers.ModelSerializer):
    cat_e = serializers.CharField(write_only=True)
    tip_e = serializers.CharField(write_only=True)

    class Meta:
        model = entrada
        exclude = ("categoria", "entradas")

    def create(self, validated_data):
        cat_e = validated_data.pop("cat_e")
        tip_e = validated_data.pop("tip_e")
        cat = Categoria.objects.get(categoria=cat_e)
        tip = Entradas.objects.get(tipo=tip_e)
        ent = entrada.objects.create(
            **validated_data, categoria=cat, entradas=tip)
        return(ent)


class EntradaReadSerializer(serializers.ModelSerializer):
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
