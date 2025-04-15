from django.db import models
from django.core.validators import MinLengthValidator


class CarModel(models.Model):
    brand = models.CharField('Brand', max_length=200, help_text='Add car brand', blank=False, null=False)
    model = models.CharField('Model', max_length=200, help_text='Add car model', blank=False, null=False)

    def __str__(self):
        return f'{self.brand}, {self.model}'


class Car(models.Model):
    license_plate = models.CharField('License_plate', max_length=200, help_text='Add car license plate', blank=False,
                                     null=False, unique=True)
    car_model_id = models.ForeignKey(CarModel, on_delete=models.SET_NULL, null=True, blank=False)
    vin_code = models.CharField('Vin_code', max_length=17,
                                validators=[MinLengthValidator(17, message='Length has to be 17')],
                                help_text='Add car VIN code', blank=False, null=False, unique=True)
    client = models.CharField('Client', max_length=200, help_text='Add client', blank=False, null=False)

    def __str__(self):
        return f'{self.license_plate}, {self.car_model_id}, {self.vin_code}, {self.client}'


class Order(models.Model):
    date = models.DateField('Order_date', blank=False, null=False)
    car_id = models.ForeignKey(Car, on_delete=models.SET_NULL, null=True, blank=False)

    def __str__(self):
        return f'{self.date}, {self.car_id}'


class OrderLine(models.Model):
    service_id = models.ForeignKey('Service', on_delete=models.SET_NULL, null=True, blank=False)
    order_id = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True, blank=False)
    quantity = models.IntegerField('Quantity', help_text='Add quantity', blank=False, null=False)

    def __str__(self):
        return f'{self.service_id}, {self.order_id}, {self.quantity}'


class Service(models.Model):
    name = models.CharField('Service_name', max_length=200, help_text='Add autoservice name', blank=False, null=False)
    price = models.FloatField('Service_price', help_text='Add autoservice price', blank=False,
                              null=False)

    def __str__(self):
        return f'{self.name}, {self.price}'
