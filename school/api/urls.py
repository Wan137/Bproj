from rest_framework import routers
from .views import SchoolAPIViewSet

router = routers.DefaultRouter()
router.register(
    "school",
    SchoolAPIViewSet
)

urlpatterns = router.urls