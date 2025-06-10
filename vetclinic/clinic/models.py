from django.db import models

class Service(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    icon = models.CharField(max_length=50)  # Ej: "fa-paw"

    def __str__(self):
        return self.name

class Veterinarian(models.Model):
    name = models.CharField(max_length=100)
    specialty = models.CharField(max_length=100)
    bio = models.TextField()
    photo = models.ImageField(upload_to='vets/')

    def __str__(self):
        return f"Dr. {self.name}"

class Appointment(models.Model):
    pet_name = models.CharField(max_length=100)
    owner_name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    date = models.DateField()
    service = models.ForeignKey(Service, on_delete=models.CASCADE)
    notes = models.TextField(blank=True)

    def __str__(self):
        return f"Cita para {self.pet_name} ({self.date})"
