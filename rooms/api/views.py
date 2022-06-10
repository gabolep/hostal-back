from rest_framework.viewsets import ModelViewSet
from rest_framework.filters import OrderingFilter
from rooms.models import Room
from rooms.api.serializers import RoomSerializer


class RoomApiViewSet(ModelViewSet):
    serializer_class = RoomSerializer
    queryset = Room.objects.all()
    filter_backends = [OrderingFilter]