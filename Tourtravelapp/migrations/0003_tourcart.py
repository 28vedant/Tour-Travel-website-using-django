# Generated by Django 4.2.9 on 2024-02-23 04:53

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Tourtravelapp', '0002_pakage_category'),
    ]

    operations = [
        migrations.CreateModel(
            name='TourCart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('qty', models.PositiveIntegerField(default=0)),
                ('pid', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Tourtravelapp.pakage')),
                ('userid', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]