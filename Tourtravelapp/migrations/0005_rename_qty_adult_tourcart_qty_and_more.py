# Generated by Django 4.2.9 on 2024-02-23 07:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Tourtravelapp', '0004_rename_qty_tourcart_qty_adult_tourcart_qty_child'),
    ]

    operations = [
        migrations.RenameField(
            model_name='tourcart',
            old_name='qty_adult',
            new_name='qty',
        ),
        migrations.RemoveField(
            model_name='tourcart',
            name='qty_child',
        ),
    ]
