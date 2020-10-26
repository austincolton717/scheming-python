from django.shortcuts import render
from rest_framework import viewsets
from .models import data
from .serializers import dataserializer


class projectview(viewsets.ModelViewSet):
    queryset = data.objects.all()
    serializer_class = dataserializer
