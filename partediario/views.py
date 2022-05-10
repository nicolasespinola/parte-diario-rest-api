from venv import create
from django.shortcuts import render
from rest_framework import viewsets
from .serializers import *
from .models import *
from partediario import serializers


class EmpresaViewSet(viewsets.ModelViewSet):
    queryset = Empresa.objects.all()
    serializer_class = EmpresaSerializer


class ParteDiarioViewSet(viewsets.ModelViewSet):
    queryset = parteDiario.objects.all()
    serializer_class = parteDiarioSerializer


class InventarioViewSet(viewsets.ModelViewSet):
    queryset = Inventario.objects.all()
    serializer_class = InventarioSerializer


class CategoriaViewSet(viewsets.ModelViewSet):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer

class dateViewSet(viewsets.ModelViewSet):
    queryset = date.objects.all()
    serializer_class = dateSerializer


class LluviaViewSet(viewsets.ModelViewSet):
    queryset = lluvia.objects.all()
    serializer_class = LluviaSerializer


class CapatazViewSet(viewsets.ModelViewSet):
    queryset = Capataz.objects.all()
    serializer_class = CapatazSerializer


class EntradaViewSet(viewsets.ModelViewSet):
    queryset = entrada.objects.all()
    serializer_class = EntradaReadSerializer

    def get_serializer_class(self):
        if (self.action == 'create'):
            return(EntradaWriteSerializer)
        return(self.serializer_class)


class SalidaViewSet(viewsets.ModelViewSet):
    queryset = salida.objects.all()
    serializer_class = SalidaSerializer


class TipoEntradaViewSet(viewsets.ModelViewSet):
    queryset = Entradas.objects.all()
    serializer_class = TipoEntradaSerializer


class TipoSalidaViewSet(viewsets.ModelViewSet):
    queryset = Salidas.objects.all()
    serializer_class = TipoSalidaSerializer


class RecategorizacionViewSet(viewsets.ModelViewSet):
    queryset = recategorizacion.objects.all()
    serializer_class = RecategorizacionSerializer


class RecorridaViewSet(viewsets.ModelViewSet):
    queryset = recorrida.objects.all()
    serializer_class = RecorridoSerializer


class SanitacionViewSet(viewsets.ModelViewSet):
    queryset = sanitacion.objects.all()
    serializer_class = SanitacionSerializer


class RotacionViewSet(viewsets.ModelViewSet):
    queryset = rotacion.objects.all()
    serializer_class = RotacionSerializer


class ContratistasViewSet(viewsets.ModelViewSet):
    queryset = contratistas.objects.all()
    serializer_class = ContratistasSerializer


class opcionSanitacionViewSet(viewsets.ModelViewSet):
    queryset = opcionSanitacion.objects.all()
    serializer_class = OpcionSantiacionSerializer
