from .models import OrderReview, Profile, Order
from django import forms
from django.contrib.auth.models import User

class OrderReviewForm(forms.ModelForm):
    class Meta:
        model = OrderReview
        fields = ('content', 'order', 'reviewer',)
        widgets = {'order': forms.HiddenInput(), 'reviewer': forms.HiddenInput()}

class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField

    class Meta:
        model = User
        fields = ['username', 'email']

class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image']


class DateInput(forms.DateInput):
    input_type = 'date'

class UserOrderCreateForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['car_id', 'customer' ,'due_back']
        widgets = {'customer': forms.HiddenInput(), 'due_back': DateInput()}

