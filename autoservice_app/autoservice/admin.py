from django.contrib import admin
from .models import CarModel, Car, Order, OrderLine, Service, OrderReview, Profile


class OrderLineInline(admin.TabularInline):
    model = OrderLine
    extra = 0


class OrderAdmin(admin.ModelAdmin):
    list_display = ('date', 'customer', 'car_id', 'status', 'due_back')
    inlines = [OrderLineInline]


class CarAdmin(admin.ModelAdmin):
    list_display = ('client', 'car_model_id', 'license_plate', 'vin_code')
    list_filter = ('client', 'car_model_id')
    search_fields = ('license_plate', 'vin_code')


class ServiceAdmin(admin.ModelAdmin):
    list_display = ('name', 'price')

class OrderReviewAdmin(admin.ModelAdmin):
    list_display = ('order', 'date_created', 'reviewer', 'content')


admin.site.register(CarModel)
admin.site.register(Car, CarAdmin)
admin.site.register(Order, OrderAdmin)
admin.site.register(Service, ServiceAdmin)
admin.site.register(OrderReview, OrderReviewAdmin)
admin.site.register(Profile)
