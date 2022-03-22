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
    fields = "__all__"


class CategoriaViewSet(viewsets.ModelViewSet):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer
    fields = "__all__"
