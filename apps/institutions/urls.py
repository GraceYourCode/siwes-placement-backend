from rest_framework.routers import DefaultRouter
from apps.institutions.views import (
    InstitutionViewSet,
    InstitutionStudentsViewSet,
    InstitutionSupervisorsViewSet,
)
from django.urls.conf import include, path

router = DefaultRouter()

router.register(r"institutions", InstitutionViewSet, basename="institution")
router.register(
    r"institutions/students",
    InstitutionStudentsViewSet,
    basename="institution-students",
)
router.register(
    r"institutions/supervisors",
    InstitutionSupervisorsViewSet,
    basename="institution-supervisors",
)

urlpatterns = [path("", include(router.urls))]
