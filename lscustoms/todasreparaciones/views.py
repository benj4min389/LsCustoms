from django.shortcuts import render


#vistas
def main(request):
    template = loader.get_template('index.html')
    return HttpResponse(template.render())


# vamos a rescatar este bloque para hacer el detalle de cada reparacion
def detalle_reparacion(request, patente):
    mymember = Member.objects.get(patente=patente)
    template = loader.get_template('detallerep.html')
    context = {'patente': patente}
    return HttpResponse(template.render(context, request))