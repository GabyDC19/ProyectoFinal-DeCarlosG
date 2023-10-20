from django.shortcuts import render
from TurismoApp.forms import formulario_f, UserRegisterForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login,authenticate

# Create your views here.
def inicio(request):
    return render (request, "TurismoApp/index.html")

def paquetes(request):
    return render (request,"TurismoApp/paquetes.html")

def tailandia(request):
    return render (request, "TurismoApp/tailandia.html")

def natal(request):
    return render (request, "TurismoApp/natal.html")


def formulario (request):
 
      if request.method == "POST":
 
            miFormulario = formulario_f (request.POST) 
            print(miFormulario)
 
            if miFormulario.is_valid():
                  informacion = miFormulario.cleaned_data
               
                  paquetes = paquetes(nombre=informacion["nombre"], cantidad=informacion["cantidad"])
                  paquetes.save()
                  return render(request, "TurismoApp/index.html")
      else:
            miFormulario = formulario_f()
 
      return render(request, "TurismoApp/formulario.html", {"miFormulario": miFormulario})


def login_request (request):


      if request.method == "POST":
            form = AuthenticationForm(request, data = request.POST)

            if form.is_valid():
                  usuario = form.cleaned_data.get('username')
                  contra = form.cleaned_data.get('password')

                  user = authenticate(username=usuario, password=contra)

            
                  if user is not None:
                        login(request, user)
                       
                        return render(request,"TurismoApp/index.html",  {"mensaje":f"Bienvenido {usuario}"} )
                  else:
                        
                        return render(request,"TurismoApp/index.html", {"mensaje":"Error, datos incorrectos"} )

            else:
                        
                        return render(request,"TurismoApp/index.html" ,  {"mensaje":"Error, formulario erroneo"})

      form = AuthenticationForm()

      return render(request,"TurismoApp/login.html", {'form':form} )


def register (request):

      if request.method == 'POST':

            form = UserRegisterForm(request.POST)
            if form.is_valid():
                username = form.cleaned_data['username']
                form.save()
                return render(request,"TurismoApp/index.html" ,  {"mensaje":f"{username} Usuario Creado :)"})


      else:
            form = UserRegisterForm()          

      return render(request,"TurismoApp/register.html" ,  {"form":form})
