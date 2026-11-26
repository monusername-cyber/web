
from django.contrib import admin
from .models import *
from AppointmentApp.models import Appointment


admin.site.register(User)

#class appointmentstacked(admin.tabularInline):
class AppointmentStackedInline(admin.StackedInline):
    model = Appointment
    extra = 1


class DoctorAdmin(admin.ModelAdmin):
    inlines = [AppointmentStackedInline]


admin.site.register(Doctor, DoctorAdmin)
admin.site.register(Patient)
admin.site.register(Specialty)
