from rest_framework import generics, permissions
from thisorthatpp5.permissions import IsOwnerOrReadOnly
from models import Like
from serializers import LikeSerializer
# Create your views here.


class LikeList(generics.ListCreateAPIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    serializer_class = LikeSerializer
    queryset = Like.objects.all()

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
