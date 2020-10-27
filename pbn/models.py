from django.db import models


class List(models.Model):
    item = models.CharField(max_length=200)
    completed = models.BooleanField(default=False)

    def __str__(self):
        return self.item


class Person(models.Model):
    name = models.CharField(max_length=100, verbose_name="full name")
