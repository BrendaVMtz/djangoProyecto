# Generated by Django 4.2.1 on 2023-06-20 19:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Ejercicio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Leccion',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='progresoLecciones',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('leccionCompleta', models.BooleanField(default=False)),
                ('idLeccion', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sgl.leccion')),
            ],
        ),
        migrations.CreateModel(
            name='progresoEjercicios',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ejercicioCompleto', models.BooleanField(default=False)),
                ('idEjercicio', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sgl.ejercicio')),
            ],
        ),
        migrations.AddField(
            model_name='ejercicio',
            name='idLeccion',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sgl.leccion'),
        ),
    ]
