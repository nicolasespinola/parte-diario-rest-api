from dataclasses import field, fields
from rest_framework import serializers
from partediario.models import *
from datetime import datetime

class EmpresaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Empresa
        fields = '__all__'


class parteDiarioSerializer(serializers.ModelSerializer):

    fecha = serializers.DateField(required=False)
    class Meta:
        model = parteDiario
        fields = '__all__'

    def create(self, validated_data):
        today = datetime.today().date()
        partediario = parteDiario.objects.create(**validated_data,fecha=today)
        return partediario



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


class dateSerializer(serializers.ModelSerializer):
    class Meta:
        model = date
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


class SalidaWriteSerializer(serializers.ModelSerializer):
    cat_e = serializers.CharField(write_only=True)
    tip_e = serializers.CharField(write_only=True)

    class Meta:
        model = salida
        exclude = ("categoria", "salidas")

    def create(self, validated_data):
        cat_e = validated_data.pop("cat_e")
        tip_e = validated_data.pop("tip_e")
        cat = Categoria.objects.get(categoria=cat_e)
        tip = Salidas.objects.get(salida=tip_e)
        sal = salida.objects.create(
            **validated_data, categoria=cat, salidas=tip)
        return(sal)

class SalidaReadSerializer(serializers.ModelSerializer):
    class Meta:
        model = salida
        fields = '__all__'

class otraWriteSerializer(serializers.ModelSerializer):
    cat_a = serializers.CharField(write_only=True)
    tip_a = serializers.CharField(write_only=True)

    class Meta:
        model = otraActividad
        exclude = ("categoria", "actividad")

    def create(self, validated_data):
        cat_a = validated_data.pop("cat_a")
        tip_a = validated_data.pop("tip_a")
        cat = Categoria.objects.get(categoria=cat_a)
        tip = opcionActividad.objects.get(nombre=tip_a)
        act = otraActividad.objects.create(
            **validated_data, categoria=cat, actividad=tip)
        return(act)

class otraReadSerializer(serializers.ModelSerializer):
    class Meta:
        model = otraActividad
        fields = '__all__'


class TipoEntradaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Entradas
        fields = '__all__'


class TipoSalidaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Salidas
        fields = '__all__'


class recategorizacionWriteSerializer(serializers.ModelSerializer):
    cat_a = serializers.CharField(write_only=True)
    cat_b = serializers.CharField(write_only=True)

    class Meta:
        model = recategorizacion
        exclude = ("categoria_inicial", "categoria_final") 

    def create(self, validated_data):
        cat_a = validated_data.pop("cat_a")
        cat_b = validated_data.pop("cat_b")
        cata = Categoria.objects.get(categoria=cat_a)
        catb = Categoria.objects.get(categoria=cat_b)
        act = recategorizacion.objects.create(
            **validated_data, categoria_inicial=cata, categoria_final=catb)
        return(act)

class recategorizacionReadSerializer(serializers.ModelSerializer):
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

class PalpacionWriteSerializer(serializers.ModelSerializer):
    cat_e = serializers.CharField(write_only=True)

    class Meta:
        model = Palpacion
        exclude = ("categoria",)

    def create(self, validated_data):
        cat_e = validated_data.pop("cat_e")
        cat = Categoria.objects.get(categoria=cat_e)
        ent = Palpacion.objects.create(
            **validated_data, categoria=cat)
        return(ent)


class PalpacionReadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Palpacion
        fields = '__all__'

class MaquinariasSerializer(serializers.ModelSerializer):
    class Meta:
        model = Maquinarias
        fields = '__all__'
