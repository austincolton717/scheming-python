from django.db import models


class data(models.Model):
    name = models.CharField(max_length=50)
    language = models.CharField(max_length=50)
    price = models.CharField(max_length=10)

    def __str__(self):
        return self.name


class pbnlist(models.Model):
    domain = models.CharField(max_length=150)
    built = models.CharField(max_length=5)
    builder = models.CharField(max_length=10)

    def __str__(self):
        return self.domain


class pbn_url(models.Model):
    domain = models.CharField(max_length=50)
    category = models.CharField(max_length=50)
    sitebuilt = models.CharField(max_length=50)
    pointed = models.CharField(max_length=50)
    indexfile = models.CharField(max_length=50)
    builder = models.CharField(max_length=50)

    def __str__(self):
        return self.domain


class seowebmap(models.Model):
    url = models.CharField(max_length=100)
    title_tag = models.CharField(max_length=60)
    meta_description = models.CharField(max_length=160)
    H1 = models.CharField(max_length=100)
    primary_kw = models.CharField(max_length=50)
    page_type = models.CharField(max_length=50)

    def __str__(self):
        return self.url
