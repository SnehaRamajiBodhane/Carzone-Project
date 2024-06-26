# Generated by Django 4.2.4 on 2023-08-11 08:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0005_alter_car_features'),
    ]

    operations = [
        migrations.RenameField(
            model_name='car',
            old_name='features',
            new_name='featuers',
        ),
        migrations.RenameField(
            model_name='car',
            old_name='passanger',
            new_name='passengers',
        ),
        migrations.AddField(
            model_name='car',
            name='interior',
            field=models.CharField(default='NULL', max_length=100),
        ),
        migrations.AlterField(
            model_name='car',
            name='condition',
            field=models.CharField(),
        ),
        migrations.AlterField(
            model_name='car',
            name='doors',
            field=models.CharField(choices=[('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6')], max_length=100),
        ),
        migrations.AlterField(
            model_name='car',
            name='fuel_type',
            field=models.CharField(max_length=10),
        ),
    ]
