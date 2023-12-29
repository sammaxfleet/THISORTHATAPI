from .views import SavedViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'saved', SavedViewSet, basename='saved')
urlpatterns = router.urls