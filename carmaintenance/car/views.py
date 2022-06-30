from django.shortcuts import render,redirect
from django.db.models import Q
from django.http import HttpResponse, HttpResponseForbidden
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.forms import UserCreationForm
from .models import BookAppointment, Car,User,TestDrive
from .forms import CarForm


# Create your views here.

# USER SECTION

def loginPage(request):
    page = 'login'
    if request.user.is_authenticated:
        return redirect('home')

    if request.method == 'POST':
        username = request.POST.get('username').lower()
        password = request.POST.get('password')

        try:
            user = User.objects.get(username=username)
        except:
            messages.error(request, 'Invalid username or password')

        user = authenticate(request,username = username, password = password)

        if user is not None:
            login(request,user)
            return redirect('home')

        else: 
            messages.error(request, 'Invalid username or password')

    context = {'page':page}

    return render(request, 'login_register.html', context)


def logoutUser(request):
    logout(request)
    return redirect('home')


def registerPage(request):
    # page = 'register'
    form = UserCreationForm()
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit = False)
            user.username = user.username.lower()
            user.save()
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'Invalid Registration')
    return render(request, 'login_register.html', {'form':form})


# CAR SECTION 


def home(request):
    q = request.GET.get('q') if request.GET.get('q') != None else ''
    # cars = Car.objects.filter(
    #     Q(topic__name__icontains=q) | Q(name__icontains = q)| Q(description__icontains = q)
    # )
    cars = Car.objects.all()
    # topics = Topic.objects.all()
    # room_count = rooms.count()
    context = {'cars': cars}
    return render(request, 'home.html', context)

def car(request, pk):
    car = Car.objects.get(id=pk)
    context = {'car': car}
    return render(request, 'car.html', context)


def aboutCar(request):
    return render(request, 'about.html')


def contactUs(request):
    return render(request, 'contact.html')

def services(request):
    return render(request, 'services.html')

def arrivals(request):
    return render(request, 'new_arrivals.html') 

# @login_required(login_url="login")
def registerCar(request):
    form = CarForm()
    if request.method == "POST":
       form = CarForm(request.POST)
       if form.is_valid():
           form.save()
           return redirect("home")
    context = {'form': form}
    return render(request, 'car_form.html', context)



# @login_required(login_url="login")
def updateCarDetails(request,pk):
    car = Car.objects.get(id=pk)
    form = CarForm(instance=car)

    if request.user != car.client:
        return HttpResponse("Not Allowed")
    if request.method == 'POST':
        form = CarForm(request.POST,instance=car)
        if form.is_valid():
            form.save()
            return redirect('home')
 
    context = {'form': form}

    return render(request,'car_form.html',context)


def carDetails(request, pk):
    car = Car.objects.get(id=pk)
    form = TestDrive(initial = {'car':car})
    context = {
        'car': car,
        'form': form,
    }
    return render(request,'car_info.html',context)


# @login_required(login_url="login")
def deleteCar(request, pk):
    car = Car.objects.get(id=pk)
    if request.user != car.regno:
        return HttpResponse("Not Allowed")
    if request.method == 'POST':
        car.delete()
        return redirect('home')
    return render(request,'delete.html', {'obj': car})


def bookAppointment(request,pk):
    if not request.user.is_authenticated:
        return redirect('login')

    user = request.user
    car = Car.objects.get(pk=pk)

    if request.method == 'POST':
        try:
            BookAppointment(
                user = user,
                car = car,
                

            ).save()
            return HttpResponse("Your Appointment Has Been Booked")
        except Exception as exc:
            return HttpResponse("Not Allowed" + exc.message)
    return HttpResponseForbidden() 