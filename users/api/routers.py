from rest_framework.routers import DefaultRouter
from users.api.views.users_viewsets import UserViewSet


router = DefaultRouter()
router.register(r'', UserViewSet, basename='users')

urlpatterns = router.urls
