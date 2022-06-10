from django.contrib import admin
from rooms.models import Room

@admin.register(Room)
class RoomAdmin(admin.ModelAdmin):
    list_display = ['number','type','bed','floor','price','deluxe','reserved']
