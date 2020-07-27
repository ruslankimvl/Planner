"""pra URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from Blog.views import post_list, post_details, post_creation, room_list, room_creation

urlpatterns = [
    path('admin/', admin.site.urls),
    path('post_list/', post_list),
    path("post_details/<slug:post_title>", post_details, name='post_detail'),
    path("create_post/", post_creation, name="post_creation"),
    path('room/', room_creation, name='room_list')

]
