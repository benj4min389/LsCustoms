from django import forms


class MiembroForm(forms.Form):
    firstname = forms.CharField(max_length=50)
    lastname = forms.CharField(max_length=50)
    phone = forms.IntegerField(required=False)
    joined_date = forms.DateField(required=False)
    email = forms.EmailField()
    password = forms.CharField(max_length=16)
    rep_password = forms.CharField(max_length=16)
    tipo_usuario = forms.CharField(max_length=40)


class LoginForm(forms.Form):
    firstname = forms.CharField(max_length=50)
    email = forms.EmailField()
    password = forms.CharField(max_length=16)
    rep_password = forms.CharField(max_length=16)


class RegistroForm(forms.Form):
    firstname = forms.CharField(max_length=50)
    lastname = forms.CharField(max_length=50)
    phone = forms.IntegerField(required=False)
    joined_date = forms.DateField(required=False)
    email = forms.EmailField()
    password = forms.CharField(max_length=16)
    rep_password = forms.CharField(max_length=16)


class AddrepForm(forms.Form):
    marca = forms.CharField(max_length=20)
    modelo_vehiculo = forms.CharField(max_length=50)
    patente = forms.CharField(max_length=6)
    motivo = forms.CharField(max_length=50)
    
