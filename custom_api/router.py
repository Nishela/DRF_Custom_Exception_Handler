from rest_framework.routers import SimpleRouter

from custom_api.views import CustomViewSet

router = SimpleRouter()
router.register('custom', CustomViewSet, basename='custom')
