# Generated by Django 5.2 on 2025-04-10 09:44

import django.core.validators
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CarModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('brand', models.CharField(help_text='Add car brand', max_length=200, verbose_name='Brand')),
                ('model', models.CharField(help_text='Add car model', max_length=200, verbose_name='Model')),
            ],
        ),
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Add autoservice name', max_length=200, verbose_name='Service_name')),
                ('price', models.FloatField(help_text='Add autoservice price', max_length=200, verbose_name='Service_price')),
            ],
        ),
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('license_plate', models.CharField(help_text='Add car license plate', max_length=200, verbose_name='License_plate')),
                ('vin_code', models.CharField(help_text='Add car VIN code', max_length=17, validators=[django.core.validators.MinLengthValidator(17, message='Length has to be 17')], verbose_name='Vin_code')),
                ('client', models.CharField(help_text='Add client', max_length=200, verbose_name='Client')),
                ('car_model_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='autoservice.carmodel')),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(verbose_name='Order_date')),
                ('car_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='autoservice.car')),
            ],
        ),
        migrations.CreateModel(
            name='OrderLine',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField(help_text='Add quantity', max_length=200, verbose_name='Quantity')),
                ('order_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='autoservice.order')),
                ('service_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='autoservice.service')),
            ],
        ),
    ]
