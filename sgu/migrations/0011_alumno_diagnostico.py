# Generated by Django 4.2.1 on 2023-06-25 02:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sgu', '0010_remove_alumno_diagnostico'),
    ]

    operations = [
        migrations.AddField(
            model_name='alumno',
            name='diagnostico',
            field=models.FileField(default='default.pdf', upload_to='users/'),
        ),
    ]
