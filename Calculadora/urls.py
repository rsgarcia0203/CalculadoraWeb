from django.urls import path
from .views import CalculadoraView

app_name = 'Calculadora'

urlpatterns = [
    path('', CalculadoraView.as_view(), name='home'),
]