from django.db import models
from django.core.validators import MinLengthValidator
from django.contrib.auth.models import User
from datetime import date
from tinymce.models import HTMLField
from PIL import Image
from django.utils.translation import gettext_lazy as _


class CarModel(models.Model):
    brand = models.CharField(_('Brand'), max_length=200, help_text=_('Add car brand'), blank=False, null=False)
    model = models.CharField(_('Model'), max_length=200, help_text=_('Add car model'), blank=False, null=False)

    def __str__(self):
        return f'{self.brand}, {self.model}'

    class Meta:
        verbose_name = "Car model"
        verbose_name_plural = "Car models"


class Car(models.Model):
    license_plate = models.CharField('License_plate', max_length=200, help_text=_('Add car license plate'), blank=False,
                                     null=False, unique=True)
    car_model_id = models.ForeignKey(CarModel, on_delete=models.SET_NULL, null=True, blank=False)
    vin_code = models.CharField('Vin_code', max_length=17,
                                validators=[MinLengthValidator(17, message=_('Length has to be 17'))],
                                help_text=_('Add car VIN code'), blank=False, null=False, unique=True)
    client = models.CharField('Client', max_length=200, help_text=_('Add client'), blank=False, null=False)
    cover = models.ImageField('Cover', upload_to='covers', null=True)
    description = HTMLField(blank=True, null=True)

    def __str__(self):
        return f'{self.license_plate}, {self.car_model_id}, {self.vin_code}, {self.client}'

    class Meta:
        verbose_name = "Car"
        verbose_name_plural = "Cars"


class Order(models.Model):
    # , blank=False, null=False
    date = models.DateField('Order_date', auto_now_add=True)
    car_id = models.ForeignKey(Car, on_delete=models.SET_NULL, null=True, blank=False)
    customer = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    due_back = models.DateField('Be_returned', null=True, blank=True)

    LOAN_STATUS = (
        ('a', 'Administered'),
        ('c', 'Closed'),
        ('r', 'Ready'),
        ('b', 'Booked'),
    )

    status = models.CharField(
        max_length=1,
        choices=LOAN_STATUS,
        blank=True,
        default='a',
        help_text='Status',
    )

    @property
    def is_overdue(self):
        if self.due_back and date.today() > self.due_back:
            return True
        return False

    def __str__(self):
        return f'{self.date}, {self.car_id}'

    class Meta:
        verbose_name = "Order"
        verbose_name_plural = "Orders"


class OrderLine(models.Model):
    service_id = models.ForeignKey('Service', on_delete=models.SET_NULL, null=True, blank=False)
    order_id = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True, blank=False)
    quantity = models.IntegerField('Quantity', help_text='Add quantity', blank=False, null=False)

    def __str__(self):
        return f'{self.service_id}, {self.order_id}, {self.quantity}'

    class Meta:
        verbose_name = "Order line"
        verbose_name_plural = "Order lines"


class Service(models.Model):
    name = models.CharField('Service_name', max_length=200, help_text='Add autoservice name', blank=False, null=False)
    price = models.FloatField('Service_price', help_text='Add autoservice price', blank=False,
                              null=False)

    def __str__(self):
        return f'{self.name}, {self.price}'

    class Meta:
        verbose_name = "Service"
        verbose_name_plural = "Services"

class OrderReview(models.Model):
    order = models.ForeignKey('Order', on_delete=models.SET_NULL, null=True, blank=True)
    reviewer = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    date_created = models.DateTimeField(auto_now_add=True)
    content = models.TextField('Review', max_length=2000)

    class Meta:
        verbose_name = "Review"
        verbose_name_plural = "Reviews"
        ordering = ['-date_created']

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default="profile_pics/default_profile.jpg", upload_to="profile_pics")

    def __str__(self):
        return f"{self.user.username} profile"

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        img = Image.open(self.image.path)
        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)
