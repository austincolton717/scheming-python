from django.db import models


class PBNsite (models.Model):
    domain_name = models.CharField(max_length=150)
    category = models.CharField(max_length=50)
    status = models.CharField(max_length=50)

    def __str__(self):
        return self.domain_name
