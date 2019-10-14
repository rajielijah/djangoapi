from django.shortcuts import render
from rest_framework import routers, serializers, viewsets
from ticketapi.serializers import UserSerializer, TicketSerializer, CategorySerializer
from django.contrib.auth.models import User
from tickets.models import Ticket, Category

# Create your views here.

# ViewSets define the view behavior.
class UserView(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

# ViewSets define the view behavior.
class TicketView(viewsets.ModelViewSet):
    queryset = Ticket.objects.all()
    serializer_class = TicketSerializer


# ViewSets define the view behavior.
class CategoryView(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
 