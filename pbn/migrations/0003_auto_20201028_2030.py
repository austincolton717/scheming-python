# Generated by Django 3.1.2 on 2020-10-28 20:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pbn', '0002_person'),
    ]

    operations = [
        migrations.CreateModel(
            name='PBNsite',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('domain_name', models.CharField(max_length=150)),
                ('category', models.CharField(max_length=50)),
                ('status', models.CharField(max_length=50)),
            ],
        ),
        migrations.DeleteModel(
            name='List',
        ),
        migrations.DeleteModel(
            name='Person',
        ),
    ]
