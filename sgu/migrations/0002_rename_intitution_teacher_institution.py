# Generated by Django 4.2.1 on 2023-06-20 23:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sgu', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='teacher',
            old_name='intitution',
            new_name='institution',
        ),
    ]