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
