# Generated by Django 3.0.3 on 2023-09-06 23:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PruebaSenaback',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('contrasena', models.CharField(max_length=50)),
                ('token', models.CharField(max_length=50)),
            ],
        ),
    ]