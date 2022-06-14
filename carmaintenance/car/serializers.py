from rest_framework import serializers

from .models import User,Car,ContactSection

class UserSerializer(serializers.ModelSerializer):

    model = User
    fields = "__all__"



class CarSerializer(serializers.ModelSerializer):

    model = Car
    fields = "__all__"


class MessageSerializer(serializers.ModelSerializer):
    model = ContactSection
    fields = "__all__"