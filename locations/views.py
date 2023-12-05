from rest_framework import generics, permissions
from django_filters.rest_framework import DjangoFilterBackend
from main.permissions import IsOwnerOrReadOnly
from .models import Location
from .serializers import LocationSerializer, LocationDetailSerializer


class LocationList(generics.ListCreateAPIView):
    """
    List location or create a location if logged in.
    """
    serializer_class = LocationSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Location.objects.all()
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['post']

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class LocationDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve a location, or update or delete it by id if you own it.
    """
    permission_classes = [IsOwnerOrReadOnly]
    serializer_class = LocationDetailSerializer
    queryset = Location.objects.all()