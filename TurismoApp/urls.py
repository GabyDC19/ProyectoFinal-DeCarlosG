from django.urls import path
from .views import inicio,paquetes,tailandia, natal,formulario,login_request,register
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('inicio/', inicio, name="Inicio"),
    path ('paq/', paquetes, name="Paquetes"),
    path('tai/', tailandia, name="Tailandia"),
    path('nat/', natal, name="Natal"),
    path('form/', formulario, name="Formulario"),
    path('login/',login_request, name="Login"),
    path('reg/',register, name="Register"),
    path('logo/', LogoutView.as_view(template_name='TurismoApp/logout.html'), name='Logout'),
]