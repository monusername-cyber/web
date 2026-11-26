
from django.db import models
from accountApp.models import Doctor, Patient
from django.utils import timezone
from django.core.exceptions import ValidationError


class Appointment(models.Model):

    reason = models.TextField()

    prescription = models.FileField(
        blank=True,
        upload_to='prescriptions/'
    )

    class Status(models.TextChoices):
        PENDING = 'PENDING', 'En attente'
        CONFIRMED = 'CONFIRMED', 'Confirmé'
        CANCELLED = 'CANCELLED', 'Annulé'

    status = models.CharField(
        max_length=10,
        choices=Status.choices,
        default=Status.PENDING
    )

    duration_minutes = models.PositiveIntegerField(default=30)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    appointment_date = models.DateTimeField()

    doctor = models.ForeignKey(
        Doctor,
        on_delete=models.CASCADE,
        related_name='appointments'
    )

    patient = models.ForeignKey(
        Patient,
        on_delete=models.CASCADE,
        related_name='appointments'
    )

    def clean(self):
        if self.appointment_date and self.appointment_date < timezone.now():
            raise ValidationError(
                "The appointment date cannot be in the past."
            )

    class Meta:
        ordering = ['appointment_date']

        constraints = [
            models.UniqueConstraint(
                fields=['doctor', 'appointment_date'],
                name='unique_doctor_appointment',
                violation_error_message='This doctor already has an appointment at this time'
            )
        ]

    def __str__(self):
        return f"LE RDV EST POUR LA RAISON {self.reason}"