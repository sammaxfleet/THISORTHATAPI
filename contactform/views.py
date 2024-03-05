# views.py
from rest_framework import viewsets
from .models import ContactForm
from .serializers import ContactFormSerializer
from rest_framework.permissions import IsAuthenticated  # Import IsAuthenticated
class ContactFormViewSet(viewsets.ModelViewSet):
    queryset = ContactForm.objects.all()
    permission_classes = []  # Apply permission class to require authentication
    serializer_class = ContactFormSerializer
    def perform_create(self, serializer):
        if self.request.user.is_authenticated:
            serializer.save(user=self.request.user)
        else:
            # If the user is not authenticated, exclude 'user' field from the serializer's data
            serializer.save(user=None)