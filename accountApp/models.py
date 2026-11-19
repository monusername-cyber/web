from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import MinLengthValidator , MaxLengthValidator, RegexValidator
from django.utils import timezone
from django.core.exceptions import ValidationError
# Create your models here.
class User(AbstractUser):
    user_id = models.CharField(primary_key=True)
   
    pass
class Specialty(models.Model):
    name = models.CharField(max_length=255)
    Created_at=models.DateTimeField(auto_now_add=True)
    Update_at=models.DateTimeField(auto_now=True)

class Doctor(User):
    licence_numbre = models.CharField(max_length=6 , unique=True, validators=[MinLengthValidator(6),MaxLengthValidator(6)])
    phone = models.CharField(max_length=8)
    Created_at=models.DateTimeField(auto_now_add=True)
    Update_at=models.DateTimeField(auto_now=True)
    #Specialties = models.ManyToManyField("accountApp.Specialty")
    specialties = models.ManyToManyField(Specialty,
    related_name="doctors"
)
number-validator =RegexValidator(regex=r'^\d{8}$',
                                 message='this number mustcontain 8 digits')
def validate_birthdate(v):
    if v>=timezone.localdate():
        raise ValidationError("la date de naissance n'est pas valide")
class Patient(User):
    national_id = models.CharField(max_length=8, unique=True,validators='number-validator')
    phone = models.CharField(max_length=8)
    birth_date = models.CharField(validators=[validate_birthdate])
    Created_at=models.DateTimeField(auto_now_add=True)
    Update_at=models.DateTimeField(auto_now=True)




    