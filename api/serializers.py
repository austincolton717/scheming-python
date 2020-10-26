from rest_framework import serializers
from .models import data


class dataserializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = data
        fields = ('id', 'url', 'name', 'language', 'price')
