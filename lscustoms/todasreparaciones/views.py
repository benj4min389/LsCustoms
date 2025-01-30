from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.template import loader
from .models import Miembro
from .forms import MiembroForm,RegistroForm,LoginForm



#vistas
def principal(request):
    template = loader.get_template('index.html')
    return HttpResponse(template.render())

def miembro(request):
    miembros = Miembro.objects.all().values()
    template = loader.get_template('all_members.html')
    context = {'miembros': miembros}
    return HttpResponse( template.render(context,request) )


# vamos a rescatar este bloque para hacer el detalle de cada reparacion
def detalle_reparacion(request, patente):
    miembros = Miembro.objects.get(patente=patente)
    template = loader.get_template('detallerep.html')
    context = {'patente': patente}
    return HttpResponse(template.render(context, request))

def requiere_usuario(tipo_requerido):
    def decorator(func):
        def wrapper(request, *args, **kwargs):
            if 'usuario_tipousuario' not in request.session or request.session['usuario_tipousuario'] != tipo_requerido:
                return redirect('main')
            return func(request, *args, **kwargs)
        return wrapper
    return decorator

@requiere_usuario('admin')
def crear_miembro(request):
    template = loader.get_template("formulario-tipusuario.html")
    if request.method == 'GET':
        form = MiembroForm (request.GET)
        if form.is_valid():
            #rescatando los datos
            firstname = form.cleaned_data['firstname']
            lastname = form.cleaned_data['lastname']
            phone = form.cleaned_data['phone']
            joined_date = form.cleaned_data['joined_date']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            rep_password = form.cleaned_data['rep_password']
            tipo_usuario = form.cleaned_data['tipo_usuario']
            if password!=rep_password:
                #debería enviar una alerta de error de contraseñas: misión de ustedes:
                form = MiembroForm()
                context = {'form': form}
                return HttpResponse(template.render(context, request))
            else:
                miembro = Miembro (firstname=firstname, 
                                lastname=lastname,
                                phone=phone,
                                joined_date=joined_date,
                                email=email,
                                password=rep_password,
                                tipo_usuario=tipo_usuario)
                miembro.save()
                return redirect('index.html')
        else:
            form = MiembroForm()
            context = {'form': form}
            return HttpResponse(template.render(context, request))
    else:
        form = MiembroForm()
        context = {'form': form}
        return HttpResponse( template.render(context, request) )
    
def login(request):
    template = loader.get_template('login.html')
    form = LoginForm()
    context = {'form': form}
    if request.method=='GET':
        form = LoginForm(request.GET)
        if form.is_valid():
            try:
                correo = form.cleaned_data['email']
                clave = form.cleaned_data['password']
                usuario_logueado = Miembro.objects.get(email=correo, password=clave)
                request.session['usuario_id'] = usuario_logueado.id
                request.session['usuario_tipousuario'] = usuario_logueado.tipo_usuario
                request.session['usuario_firstname'] = usuario_logueado.firstname
                return redirect('main')
            except:
                
                pass
    return HttpResponse(template.render(context, request))
    
def logout(request):
    request.session.flush()
    return redirect('index.html')

def registro(request):
    template = loader.get_template("registro.html")
    if request.method == 'GET':
        form = RegistroForm(request.GET)
        if form.is_valid():

            firstname = form.cleaned_data['firstname']
            lastname = form.cleaned_data['lastname']
            phone = form.cleaned_data['phone']
            joined_date = form.cleaned_data['joined_date']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            rep_password = form.cleaned_data['rep_password']
            tipo_usuario = "mecanico"
            if password!=rep_password:

                form = RegistroForm()
                context = {'form': form}
                return HttpResponse(template.render(context, request))
            else:
                miembro = Miembro(firstname=firstname, 
                                lastname=lastname,
                                phone=phone,
                                joined_date=joined_date,
                                email=email,
                                password=rep_password,
                                tipo_usuario=tipo_usuario)
                miembro.save()
                return redirect('login')
        else:
            form = RegistroForm()
            context = {'form': form}
            return HttpResponse(template.render(context, request))
    else:
        form = RegistroForm()
        context = {'form': form}
        return HttpResponse( template.render(context, request) )
    
def todas_reparaciones(request):
    template = loader.get_template('todasreparaciones.html')
    context = {'valor': 10}
    return HttpResponse( template.render(context, request) )


