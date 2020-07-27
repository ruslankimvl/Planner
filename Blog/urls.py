from django.urls import path
from . import views
app_name = 'Blog'

urlpatterns = [

 path('room/', views.room_list, name = 'room_list')

 ]