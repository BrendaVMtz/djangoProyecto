# Generated by Django 4.2.1 on 2023-06-25 00:08

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sgu', '0007_alter_padre_delegacion_alter_salud_delegacion'),
    ]

    operations = [
        migrations.AddField(
            model_name='alumno',
            name='apellido',
            field=models.CharField(default='Lopez', max_length=100),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='alumno',
            name='edad',
            field=models.IntegerField(validators=[django.core.validators.MinValueValidator(12), django.core.validators.MaxValueValidator(100)]),
        ),
    ]
