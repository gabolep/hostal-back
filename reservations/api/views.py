from rest_framework.viewsets import ModelViewSet
from reservations.models import Reservation
from reservations.api.serializers import ReservationSerializer

class ReservationViewSet(ModelViewSet):
    serializer_class = ReservationSerializer
    queryset= Reservation.objects.all()