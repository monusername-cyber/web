from django.contrib import admin
from .models import Appointment
 
# Register your models here.
# admin.site.register(Appointment)
 
# class AppointmentAdminPers(admin.ModelAdmin):
#     list_display=("reason","status","duration_minutes","appointment_date")
# admin.site.register(Appointment,AppointmentAdminPers)
@admin.action(description="make them confirmed")
def confirm_appointments(model,req,queryset):
    queryset.update(status="CONFIRMED")

@admin.register(Appointment)
class AppointmentAdminPers(admin.ModelAdmin):
    list_display=("reason","status","duration_minutes","appointment_date")
    list_filter=("status","appointment_date")
    list_editable=("status",)
    search_fields=("reason","status")
    ordering=("-appointment_date",)
    list_per_page=2
    fieldsets=('description',{'fields':('reason','status','prescription')}),
    ('date + DUration',{'fields':('appointment_date','duration_minutes')}),
    ('patient/doctors',{'fields':('doctor','patient')})
    ('planification',{'fields':('created_at','updated_at')})
readonly_fields=('created_at','updated_at')