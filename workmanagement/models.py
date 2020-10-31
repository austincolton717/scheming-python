from django.db import models


class seoProject (models.Model):
    project_name = models.CharField(max_length=150)
    project_type = models.CharField(max_length=150)
    project_manager = models.CharField(max_length=150)
    client = models.CharField(max_length=150)
    status = models.CharField(max_length=150)

    def __str__(self):
        return self.project_name
