from django.contrib.auth.models import User
from rest_framework import serializers
from tickets.models import Category, Ticket

class TicketSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Ticket
        fields = '__all__'

class CategorySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model =Category
        fields = ('name', 'slug')

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'email', 'username', 'is_staff')