from django.urls import path
from . import views

urlpatterns = [
    path('criar_usuario/', views.criar_usuario, name='criar_usuario'),
    path('login/', views.login, name='login')
]
