from django.urls import path
from app_cart_estudante import views

urlpatterns = [
    path("",views.home,name="home"),
]