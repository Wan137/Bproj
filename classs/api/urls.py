from rest_framework import routers
from .views import ClassAPIViewSet

router = routers.DefaultRouter()
router.register(
    "class",
    ClassAPIViewSet
)

urlpatterns = router.urls