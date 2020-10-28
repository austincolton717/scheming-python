from django.shortcuts import render
from rest_framework import viewsets
from .models import data, pbnlist, pbn_url
from .serializers import dataserializer, pbnlistserializer, pbntableserializer


class projectview(viewsets.ModelViewSet):
    queryset = data.objects.all()
    serializer_class = dataserializer


class pbnlistview(viewsets.ModelViewSet):
    queryset = pbnlist.objects.all()
    serializer_class = pbnlistserializer


class pbntableview(viewsets.ModelViewSet):
    queryset = data.objects.all()
    serializer_class = pbntableserializer
