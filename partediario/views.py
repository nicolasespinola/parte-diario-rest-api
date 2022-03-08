from django.shortcuts import render
from rest_framework import viewsets
from .serializers import MusicianSeralizer
from .models import Musician
from partediario import serializers

# class MusicianViewSet(viewsets.ModelViewSet):
#     queryset=Musician.objects.all()
#     serializers_class=MusicianSeralizer
