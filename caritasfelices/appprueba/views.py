# appprueba/views.py

from django.shortcuts import render, redirect
from .models import CampanaActiva
from .forms import CampanaForm


def crear_campana(request):
    if request.method == 'POST':
        form = CampanaForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()  # Guardar la nueva campaña en la base de datos
            #return redirect('campanas_activas')  # Redirigir a una página después de guardar
    else:
        form = CampanaForm()

    return render(request, 'appprueba/create_campaign.html', {'form': form})


def campanas_activas_view(request):
    campanas = CampanaActiva.objects.all()
    return render(request, 'appprueba/campanas_activas.html', {'campanas': campanas})



