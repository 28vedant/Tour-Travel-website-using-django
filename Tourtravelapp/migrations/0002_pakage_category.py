# Generated by Django 5.0.2 on 2024-02-17 17:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Tourtravelapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='pakage',
            name='category',
            field=models.CharField(choices=[('India', 'India'), ('Europe', 'Europe'), ('Thailand', 'Thailand'), ('Malaysia', 'Malaysia')], default='', max_length=50),
        ),
    ]
