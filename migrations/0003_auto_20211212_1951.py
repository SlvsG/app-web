# Generated by Django 3.1.2 on 2021-12-13 01:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0002_cliente_prestamo'),
    ]

    operations = [
        migrations.RenameField(
            model_name='prestamo',
            old_name='id_Cliente',
            new_name='cliente',
        ),
        migrations.RenameField(
            model_name='prestamo',
            old_name='id_libro',
            new_name='libro',
        ),
    ]