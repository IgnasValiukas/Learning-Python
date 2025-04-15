from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.views import generic
from .models import CarModel, Car, Order, OrderLine, Service


def index(request):
    num_service = Service.objects.all().count
    num_order = OrderLine.objects.all().count()
    num_car = Car.objects.all().count()

    context = {
        'num_service': num_service,
        'num_order': num_order,
        'num_car': num_car
    }

    return render(request, 'index.html', context=context)

def cars(request):
    car = Car.objects.all()
    context = {
        'cars': car
    }
    return render(request, 'cars.html', context=context)

def car(request, car_id):
    single_car = get_object_or_404(Car, pk=car_id)
    return render(request, 'car.html', {'car': single_car})

class OrderListView(generic.ListView):
    model = Order
    template_name = 'order_list.html'

class OrderDetailView(generic.DetailView):
    model = Order
    template_name = 'order_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        order = self.get_object()
        context['order_set'] = Order.objects.filter(car_id=order.car_id)
        return context