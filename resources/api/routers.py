from rest_framework.routers import DefaultRouter
from resources.api.views.resources_viewsets import ResourceViewSet


router = DefaultRouter()
router.register(r'', ResourceViewSet, basename='resources')

urlpatterns = router.urls
