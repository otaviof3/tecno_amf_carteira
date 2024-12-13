from django.urls import path
from app_cart_estudante import views

urlpatterns = [
    path('', views.home, name='home'),
    path('perfil/', views.perfil_estudante, name='perfil_estudante'),
    path('login/', views.login_view, name='login'),  
]