from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from reservations.models import Reservation

@admin.register(Reservation)
class ReservationAdmin(admin.ModelAdmin):
    list_display = ['reservation_number', 'user', 'room', 'payment_method','check_in','check_out']
    fieldsets = (
        (None, {'fields': ('reservation_number', 'user', 'room', 'payment_method','check_in','check_out')}),
    )

    def __str__(self):
        return self.payment_method