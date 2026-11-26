
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import MinLengthValidator, MaxLengthValidator, RegexValidator
from django.utils import timezone
from django.core.exceptions import ValidationError


class User(AbstractUser):
    user_id = models.CharField(primary_key=True, max_length=20)


class Specialty(models.Model):
    name = models.CharField(max_length=255)
    Created_at = models.DateTimeField(auto_now_add=True)
    Update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Specialty'
        verbose_name_plural = 'Specialties'
    def __str__(self):
            return self.name


number_validator = RegexValidator(
    regex=r'^\d{8}$',
    message='This number must contain 8 digits'
)


def validate_birthdate(value):
    if value >= timezone.localdate():
        raise ValidationError("La date de naissance n'est pas valide")
    


class Doctor(User):
    licence_numbre = models.CharField(
        max_length=6,
        unique=True,
        validators=[MinLengthValidator(6), MaxLengthValidator(6)]
    )

    phone = models.CharField(
        max_length=8,
        validators=[number_validator]
    )

    Created_at = models.DateTimeField(auto_now_add=True)
    Update_at = models.DateTimeField(auto_now=True)

    specialties = models.ManyToManyField(
        Specialty,
        related_name="doctors"
    )

    class Meta:
        verbose_name = 'Doctor'
        verbose_name_plural = 'Doctors'


class Patient(User):
    national_id = models.CharField(
        max_length=8,
        unique=True,
        validators=[number_validator]
    )

    phone = models.CharField(
        max_length=8,
        validators=[number_validator]
    )

    birth_date = models.DateField(
        validators=[validate_birthdate]
    )

    Created_at = models.DateTimeField(auto_now_add=True)
    Update_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Patient'
        verbose_name_plural = 'Patients'
