from rest_framework import serializers
from reservations.models import Reservation

class ReservationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reservation
        fields = ['reservation_number', 'user', 'room', 'payment_method','check_in','check_out']
        