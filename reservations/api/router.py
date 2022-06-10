from rest_framework.routers import DefaultRouter
from reservations.api.views import ReservationViewSet

router_reservations = DefaultRouter()

router_reservations.register(prefix = 'reservations', basename='reservations', viewset=ReservationViewSet)