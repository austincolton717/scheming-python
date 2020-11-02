from django.db import models


class clientData (models.Model):
    name = models.CharField(max_length=150)
    address = models.CharField(max_length=150)
    cityZip = models.CharField(max_length=150)
    project_type = models.CharField(max_length=150)
    project_start = models.CharField(max_length=150)
    billing_date = models.CharField(max_length=150)
    status = models.CharField(max_length=150)
    amount_invoiced = models.CharField(max_length=150)

    def __str__(self):
        return self.name


class clientTasks (models.Model):
    task_item = models.CharField(max_length=150)
    due_date = models.CharField(max_length=150)

    def __str__(self):
        return self.task_item


class clientProject (models.Model):
    project = models.CharField(max_length=150)
    starts = models.CharField(max_length=150)
    status = models.CharField(max_length=150)
    amount_due = models.CharField(max_length=150)

    def __str__(self):
        return self.project


class expenseInfo (models.Model):
    total = models.CharField(max_length=150)
    bill_date = models.CharField(max_length=150)
    merchant = models.CharField(max_length=150)
    purpose = models.CharField(max_length=150)
    tax_category = models.CharField(max_length=150)

    def __str__(self):
        return self.total


class clientNotes (models.Model):
    notes = models.CharField(max_length=2000)
