# Generated by Django 4.2.4 on 2023-09-29 01:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('senaback', '0008_rename_cantidad_elementos_disponibles_elementoconsumible_cantidad_total_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='elementoconsumible',
            name='descripcion_elemento',
            field=models.CharField(max_length=30),
        ),
    ]
