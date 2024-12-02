from django.urls import path
from .import views

urlpatterns = [
    path('contact/', views.contact_views, name="contact_us"),
    path('about', views.about, name="about"),

]