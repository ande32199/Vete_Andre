from django.shortcuts import render
from django.shortcuts import render, redirect
from .models import Service, Veterinarian, Appointment
from .forms import AppointmentForm

def home(request):
    services = Service.objects.all()
    vets = Veterinarian.objects.all()
    return render(request, 'clinic/home.html', {'services': services, 'vets': vets})

def appointment(request):
    if request.method == 'POST':
        form = AppointmentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = AppointmentForm()
    return render(request, 'clinic/appointment.html', {'form': form})

