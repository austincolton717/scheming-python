from rest_framework import serializers
from .models import data, pbnlist


class dataserializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = data
        fields = ('id', 'url', 'name', 'language', 'price')


class pbnlistserializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = data
        fields = ('id', 'domain', 'built', 'builder')
