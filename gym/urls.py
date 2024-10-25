from django.contrib import admin
from django.urls import path
from gym import views

urlpatterns = [
    path("",views.home,name="home"),
    path('register', views.register, name='register'),
    path('data', views.data, name='data'),
    path("about_us",views.about_us,name="about_us"),
    path("contact",views.contact,name="contact"),
    path("update/<id>",views.update,name="update"),
    path("delete/<id>",views.delete,name="delete"),
]
