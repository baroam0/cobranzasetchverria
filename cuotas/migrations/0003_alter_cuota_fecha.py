# Generated by Django 3.2 on 2022-09-05 23:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cuotas', '0002_cuota_importecomision'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cuota',
            name='fecha',
            field=models.DateField(),
        ),
    ]
