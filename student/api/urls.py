from rest_framework import routers
from .views import StudentAPIViewSet

router = routers.DefaultRouter()

router.register(
    "student",
    StudentAPIViewSet
)

urlpatterns = router.urls
