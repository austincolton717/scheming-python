from rest_framework import serializers
from .models import data, pbnlist, pbn_url, seowebmap


class dataserializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = data
        fields = ('id', 'url', 'name', 'language', 'price')


class pbnlistserializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = pbnlist
        fields = ('id', 'domain', 'built', 'builder')


class pbntableserializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = pbn_url
        fields = ('id', 'domain', 'category', 'sitebuilt',
                  'pointed', 'indexfile', 'builder')


class webmapserializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = seowebmap
        fields = ('id', 'url', 'titletag', 'metadescription',
                  'H1', 'primarykw', 'pagetype')
