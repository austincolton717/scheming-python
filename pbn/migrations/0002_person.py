# Generated by Django 3.1.2 on 2020-10-28 01:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pbn', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='full name')),
            ],
        ),
    ]
