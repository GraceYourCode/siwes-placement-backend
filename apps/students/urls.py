from rest_framework.routers import DefaultRouter
from apps.students.views import StudentInstitutionProfileViewSet
from django.urls.conf import include, path

router = DefaultRouter()

router.register(
    r"institution_profile",
    StudentInstitutionProfileViewSet,
    basename="student_institution_profile",
)

urlpatterns = [path("students/", include(router.urls))]
