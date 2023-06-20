# Generated by Django 4.2.1 on 2023-06-19 11:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('sgu', '0003_alumno_edad'),
    ]

    operations = [
        migrations.CreateModel(
            name='usuario',
            fields=[
                ('nombre', models.CharField(max_length=50)),
                ('apellido', models.CharField(max_length=50)),
                ('nombreDeUsuario', models.CharField(max_length=50, primary_key=True, serialize=False, unique=True)),
                ('contrasena', models.CharField(max_length=50)),
            ],
        ),
        migrations.RemoveField(
            model_name='alumno',
            name='apellido',
        ),
        migrations.RemoveField(
            model_name='alumno',
            name='contrasena',
        ),
        migrations.RemoveField(
            model_name='alumno',
            name='idCuidador',
        ),
        migrations.RemoveField(
            model_name='alumno',
            name='nombre',
        ),
        migrations.RemoveField(
            model_name='cuidador',
            name='apellido',
        ),
        migrations.RemoveField(
            model_name='cuidador',
            name='contrasena',
        ),
        migrations.RemoveField(
            model_name='cuidador',
            name='nombre',
        ),
        migrations.AlterField(
            model_name='alumno',
            name='nombreDeUsuario',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='sgu.usuario'),
        ),
        migrations.AlterField(
            model_name='cuidador',
            name='nombreDeUsuario',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='sgu.usuario'),
        ),
    ]