from rest_framework import serializers
from rooms.models import Room

class RoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Room
        fields = ['number','type','bed','floor','price','deluxe','reserved']