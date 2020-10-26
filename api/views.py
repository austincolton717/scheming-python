from django.shortcuts import render
from rest_framework import viewsets
from .models import data, pbnlist
from .serializers import dataserializer, pbnlistserializer


class projectview(viewsets.ModelViewSet):
    queryset = data.objects.all()
    serializer_class = dataserializer


class pbnlistview(viewsets.ModelViewSet):
    queryset = pbnlist.objects.all()
    serializer_class = pbnlistserializer
