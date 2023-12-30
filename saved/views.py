from rest_framework import generics, permissions,viewsets
from thisorthatpp5.permissions import IsOwnerOrReadOnly
from saved.models import Saved
from saved.serializers import SavedSerializer
from rest_framework.response import Response
from thisorthatpp5.permissions import IsOwnerOrReadOnly
from rest_framework import status
from django.shortcuts import get_object_or_404
from rest_framework.decorators import action 

class  SavedViewSet(viewsets.ModelViewSet):
    """
    A simple ViewSet for viewing and editing accounts.
    """
    serializer_class = SavedSerializer
    permission_classes = [IsOwnerOrReadOnly]
    def get_queryset(self):
        return Saved.objects.filter(owner=self.request.user).all()

    def create(self,request,*args,**kwargs):
        if request.user.is_authenticated:
            print(request.data,"yoooo")
        
            saved_object = Saved.objects.get_or_create(post_id=request.data["post"],owner=request.user)

           
            print(saved_object,"object yayy")
            return Response("Items Saved",status=status.HTTP_200_OK)

    @action(methods=['get'],detail=False)
    def remove_saved_post(self,request):
        print(request.data,"delte data")
        saved_id=request.GET.get('saved_id')
        if request.user.is_authenticated:
            saved=get_object_or_404(Saved,id=saved_id,owner=request.user)
            if saved:
                saved.delete()
                return Response("Saved deleted",status=status.HTTP_200_OK)
