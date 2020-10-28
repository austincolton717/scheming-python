from django.shortcuts import render
from rest_framework import viewsets
from .models import data, pbnlist, pbn_url, seowebmap
from .serializers import dataserializer, pbnlistserializer, pbntableserializer, webmapserializer


class projectview(viewsets.ModelViewSet):
    queryset = data.objects.all()
    serializer_class = dataserializer


class pbnlistview(viewsets.ModelViewSet):
    queryset = pbnlist.objects.all()
    serializer_class = pbnlistserializer


class pbntableview(viewsets.ModelViewSet):
    queryset = pbn_url.objects.all()
    serializer_class = pbntableserializer


class webmapview(viewsets.ModelViewSet):
    queryset = seowebmap.objects.all()
    serializer_class = webmapserializer
