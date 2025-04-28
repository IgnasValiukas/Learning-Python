from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.http import HttpResponse
from django.views import generic
from django.core.paginator import Paginator
from django.db.models import Q
from .models import CarModel, Car, Order, OrderLine, Service
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.mixins import UserPassesTestMixin
from django.contrib.auth.forms import User
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import OrderReviewForm, UserUpdateForm, ProfileUpdateForm, UserOrderCreateForm
from django.views.decorators.csrf import csrf_protect
from django.views.generic.edit import FormMixin
from django.utils.translation import gettext as _
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)


def index(request):
    num_service = Service.objects.all().count
    num_order = OrderLine.objects.all().count()
    num_car = Car.objects.all().count()

    num_visits = request.session.get('num_visits', 1)
    request.session['num_visits'] = num_visits + 1
    context = {
        'num_service': num_service,
        'num_order': num_order,
        'num_car': num_car,
        'num_visits': num_visits
    }

    return render(request, 'index.html', context=context)


def cars(request):
    paginator = Paginator(Car.objects.all(), 3)
    page_number = request.GET.get('page')
    car = paginator.get_page(page_number)
    context = {
        'cars': car
    }
    return render(request, 'cars.html', context=context)


def car(request, car_id):
    single_car = get_object_or_404(Car, pk=car_id)
    return render(request, 'car.html', {'car': single_car})


class OrderListView(generic.ListView):
    model = Order
    paginate_by = 3
    template_name = 'order_list.html'


class OrderDetailView(FormMixin, generic.DetailView):
    model = Order
    template_name = 'order_detail.html'
    form_class = OrderReviewForm

    def get_success_url(self):
        return reverse('order-detail', kwargs={'pk': self.object.id})

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form = self.get_form()
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def form_valid(self, form):
        form.instance.order = self.object
        form.instance.reviewer = self.request.user
        form.save()
        return super(OrderDetailView, self).form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        order = self.get_object()
        context['order_set'] = Order.objects.filter(car_id=order.car_id)
        return context


def search(request):
    query = request.GET.get('query')
    search_results = Car.objects.filter(
        Q(license_plate__icontains=query) | Q(vin_code__icontains=query) | Q(client__icontains=query)
        | Q(car_model_id__model__icontains=query) | Q(car_model_id__brand__icontains=query))
    return render(request, 'search.html', {'cars': search_results, 'query': query})


class OrdersByUserListView(LoginRequiredMixin, generic.ListView):
    model = Order
    template_name = 'user_orders.html'
    paginate_by = 3

    def get_queryset(self):
        return Order.objects.filter(customer=self.request.user).order_by('due_back')


@csrf_protect
def register(request):
    if request.method == "POST":
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']
        if password == password2:
            if User.objects.filter(username=username).exists():
                messages.error(request, _('Username \'%s\' already exists!') % username)
                return redirect('register')
            else:
                if User.objects.filter(email=email).exists():
                    messages.error(request, _('User with email \'%s\' already exists!' % email))
                    return redirect('register')
                else:
                    User.objects.create_user(username=username, email=email, password=password)
                    messages.info(request, _('User \'%s\' successfully registered!') % username)
                    return redirect('login')
        else:
            messages.error(request, _('Passwords do not match!'))
            return redirect('register')
    return render(request, 'register.html')


@login_required
def profile(request):
    if request.method == "POST":
        user_form = UserUpdateForm(request.POST, instance=request.user)
        profile_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, f"Profile updated!")
            return redirect('profile')
    else:
        user_form = UserUpdateForm(instance=request.user)
        profile_form = ProfileUpdateForm(instance=request.user.profile)
    context = {
        'user_form': user_form,
        'profile_form': profile_form,
    }
    return render(request, 'profile.html', context)


class OrderByUserDetailView(LoginRequiredMixin, DetailView):
    model = Order
    template_name = 'user_order.html'


class OrderByUserCreateView(LoginRequiredMixin, CreateView):
    model = Order
    # fields = ['car_id', 'due_back']
    success_url = "/autoservice/myorders/"
    template_name = 'user_order_form.html'
    form_class = UserOrderCreateForm

    def form_valid(self, form):
        form.instance.customer = self.request.user
        return super().form_valid(form)


class OrderByUserUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Order
    fields = ['car_id', 'due_back']
    success_url = "/autoservice/myorders/"
    template_name = 'user_order_form.html'

    def form_valid(self, form):
        form.instance.customer = self.request.user
        return super().form_valid(form)

    def test_func(self):
        order = self.get_object()
        return self.request.user == order.customer


class OrderByUserDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Order
    success_url = "/autoservice/myorders/"
    template_name = 'user_order_delete.html'

    def test_func(self):
        order = self.get_object()
        return self.request.user == order.customer