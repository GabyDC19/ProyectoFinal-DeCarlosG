from django.urls import path
from .views import formulario,login_request,register, editarPerfil
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('form/', formulario, name="Formulario"),
    path('login/',login_request, name="Login"),
    path('reg/',register, name="Register"),
    path('logo/', LogoutView.as_view(template_name='TurismoApp/logout.html'), name='Logout'),
    path('edit/', editarPerfil, name="EditarPerfil"),
]
