# Generated by Django 3.1.2 on 2020-11-02 23:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='clientData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('address', models.CharField(max_length=150)),
                ('cityZip', models.CharField(max_length=150)),
                ('project_type', models.CharField(max_length=150)),
                ('project_start', models.CharField(max_length=150)),
                ('billing_date', models.CharField(max_length=150)),
                ('status', models.CharField(max_length=150)),
                ('amount_invoiced', models.CharField(max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='clientNotes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('notes', models.CharField(max_length=2000)),
            ],
        ),
        migrations.CreateModel(
            name='clientProject',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('project', models.CharField(max_length=150)),
                ('starts', models.CharField(max_length=150)),
                ('status', models.CharField(max_length=150)),
                ('amount_due', models.CharField(max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='clientTasks',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('task_item', models.CharField(max_length=150)),
                ('due_date', models.CharField(max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='expenseInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total', models.CharField(max_length=150)),
                ('bill_date', models.CharField(max_length=150)),
                ('merchant', models.CharField(max_length=150)),
                ('purpose', models.CharField(max_length=150)),
                ('tax_category', models.CharField(max_length=150)),
            ],
        ),
    ]