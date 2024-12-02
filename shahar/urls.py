from django.urls import path, include
from .import views


urlpatterns = [
    path('', views.product_list, name="list"),
    path('product/<int:slug>', views.product, name="pr"),
    path('login/', views.login_page, name="login"),
    path('logout/', views.logout_page, name="logout"),
    path('register/', views.register_page, name="register"),
    path('search', views.search, name="search"),
    path('catagory/<str:cat>', views.catagoryView, name="catagory"),
    path('catagory_partial', views.catagory_partcial, name="catagory_partial"),
    
]
