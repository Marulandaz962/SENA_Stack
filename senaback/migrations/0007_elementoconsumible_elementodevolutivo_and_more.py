# Generated by Django 4.2.4 on 2023-09-28 23:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('senaback', '0006_rename_usuarios_usuario'),
    ]

    operations = [
        migrations.CreateModel(
            name='ElementoConsumible',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=15, unique=True)),
                ('serial', models.CharField(max_length=20, unique=True)),
                ('cantidad_elementos_total', models.CharField(max_length=15)),
                ('cantidad_elementos_disponibles', models.CharField(max_length=15)),
                ('valor', models.IntegerField()),
                ('categoria', models.CharField(max_length=20)),
                ('descripcion_elemento', models.CharField(max_length=15)),
            ],
        ),
        migrations.CreateModel(
            name='ElementoDevolutivo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=25)),
                ('codigo_placa_sena', models.CharField(max_length=15)),
                ('serial', models.CharField(max_length=20)),
                ('cantidad_elementos_total', models.CharField(max_length=15)),
                ('cantidad_elementos_disponibles', models.CharField(max_length=15)),
                ('descripcion_elemento', models.CharField(max_length=16)),
                ('valor', models.IntegerField()),
                ('garantia', models.DateField()),
                ('estado', models.CharField(max_length=20)),
                ('categoria', models.CharField(max_length=20)),
            ],
        ),
        migrations.RenameModel(
            old_name='PruebaSenaback',
            new_name='Login',
        ),
        migrations.RenameField(
            model_name='usuario',
            old_name='nombre_1',
            new_name='nombre',
        ),
        migrations.RemoveField(
            model_name='usuario',
            name='firma_digital',
        ),
        migrations.RemoveField(
            model_name='usuario',
            name='nombre_2',
        ),
        migrations.AlterField(
            model_name='usuario',
            name='apellido_1',
            field=models.CharField(max_length=12),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='apellido_2',
            field=models.CharField(max_length=12),
        ),
        migrations.CreateModel(
            name='prestamo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cantidad', models.IntegerField()),
                ('fecha_Prestamo', models.DateField()),
                ('fecha_Devolucion', models.DateField()),
                ('estado', models.CharField(max_length=20)),
                ('elemento', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='prestamos_elemento', to='senaback.elementodevolutivo')),
                ('responsable', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='prestamos_responsable', to='senaback.usuario')),
                ('serial', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='prestamos_serial', to='senaback.elementodevolutivo')),
            ],
        ),
        migrations.CreateModel(
            name='Garantia',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateField()),
                ('Descripcion', models.CharField(max_length=150)),
                ('elemento', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='garantias_elemento', to='senaback.elementodevolutivo')),
                ('responsable', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='garantias_responsable', to='senaback.usuario')),
                ('serial', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='garantias_serial', to='senaback.elementodevolutivo')),
            ],
        ),
        migrations.CreateModel(
            name='entrega',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cantidad', models.IntegerField()),
                ('elemento', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='entregas_elemento', to='senaback.elementoconsumible', to_field='nombre')),
                ('responsable', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='entregas_responsable', to='senaback.usuario')),
                ('serial', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='entregas_serial', to='senaback.elementoconsumible', to_field='serial')),
            ],
        ),
        migrations.CreateModel(
            name='Baja',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateField()),
                ('Descripcion', models.CharField(max_length=150)),
                ('elemento_devolutivo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='bajas_elemento_devolutivo', to='senaback.elementodevolutivo')),
                ('responsable', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='bajas_responsable', to='senaback.usuario')),
                ('serial', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='bajas_serial', to='senaback.elementodevolutivo')),
            ],
        ),
    ]
