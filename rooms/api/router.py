from rest_framework.routers import DefaultRouter
from rooms.api.views import RoomApiViewSet

router_rooms = DefaultRouter()

router_rooms.register(prefix = 'rooms', basename='rooms',viewset = RoomApiViewSet)