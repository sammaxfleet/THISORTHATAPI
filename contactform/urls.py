# urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ContactFormViewSet

router = DefaultRouter()
router.register(r'', ContactFormViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
