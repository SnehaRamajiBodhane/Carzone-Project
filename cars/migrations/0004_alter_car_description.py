# Generated by Django 4.2.4 on 2023-08-11 06:53

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0003_alter_car_doors_alter_car_fuel_type_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car',
            name='description',
            field=ckeditor.fields.RichTextField(),
        ),
    ]
