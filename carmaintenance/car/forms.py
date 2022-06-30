from django.forms import ModelForm

from .models import Car,User,BookAppointment,TestDrive


class CarForm(ModelForm):
    class Meta:
        model = Car
        fields = '__all__'


class UserForm(ModelForm):
    class Meta:
        model = User
        fields = '__all__'



class AppointmentForm(ModelForm):
    class Meta:
        model = BookAppointment
        fields = ['car','appointment_date']


class TestDriveForm(ModelForm):
    class Meta:
        model = TestDrive
        fields = ['car','time']