# from django.conf import settings
# from django.conf.urls.static import static
# from django.urls import URLPattern
# if settings.DEBUG:
#         URLPattern += static(settings.MEDIA_URL,
#                               document_root=settings.MEDIA_ROOT)
from django.urls import path

from . import views

urlpatterns = [
    path("login/", views.loginPage, name="login"),
    path("logout/", views.logoutUser, name="log-out"),
    path("register/", views.registerPage, name="register"),
    path("", views.home, name="home"),
    path('car/<str:pk>/', views.car, name="car"),
    path('about/', views.aboutCar, name="about"),
    path('contact/', views.contactUs, name="contact"),
    path('services/', views.services, name="services"),
    path('arrivals/', views.arrivals, name="arrivals"),
    path('register-car/', views.registerCar, name="register-car"),
    path('update-car/<str:pk>/', views.updateCarDetails, name="update-car"),
    path('delete-car/<str:pk>/', views.deleteCar, name="delete-car")
]