from rest_framework.routers import DefaultRouter
from apps.supervisors.views import SupervisorViewSet, SupervisorStudentsViewSet
from django.urls.conf import include, path

router = DefaultRouter()

router.register(r"supervisors", SupervisorViewSet, basename="supervisor")
router.register(
    r"supervisors/students", SupervisorStudentsViewSet, basename="supervisor-students"
)

urlpatterns = [path("", include(router.urls))]
