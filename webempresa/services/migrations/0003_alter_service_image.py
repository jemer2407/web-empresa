# Generated by Django 5.1.2 on 2024-11-01 08:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0002_remove_service_link'),
    ]

    operations = [
        migrations.AlterField(
            model_name='service',
            name='image',
            field=models.ImageField(upload_to='services', verbose_name='Imagen'),
        ),
    ]
