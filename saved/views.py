from rest_framework import generics, permissions,viewsets
from thisorthatpp5.permissions import IsOwnerOrReadOnly
from saved.models import Saved
from saved.serializers import SavedSerializer
from rest_framework.response import Response
from thisorthatpp5.permissions import IsOwnerOrReadOnly


class  SavedViewSet(viewsets.ModelViewSet):
    """
    A simple ViewSet for viewing and editing accounts.
    """
    serializer_class = SavedSerializer
    permission_classes = [IsOwnerOrReadOnly]
    def get_queryset(self):
        return Saved.objects.filter(owner=self.request.user).all()

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
