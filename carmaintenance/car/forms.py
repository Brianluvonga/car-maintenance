from django.forms import ModelForm

from .models import Car,User


class CarForm(ModelForm):
    class Meta:
        model = Car
        fields = '__all__'


class UserForm(ModelForm):
    class Meta:
        model = User
        fields = '__all__'