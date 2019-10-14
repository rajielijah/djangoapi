from rest_framework import routers
from django.contrib import admin
from django.urls import path,include
from tickets import views

router = routers.DefaultRouter()
router.register(r'api/users', views.UserView)
router.register(r'api/tickets', views.TicketView)
router.register(r'api/categorys', views.CategoryView)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include(router.urls)),
    path('api-auth', include('rest_framework.urls', namespace='rest_framework'))
]
