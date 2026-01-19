from rest_framework.routers import DefaultRouter
from apps.mentors.views import CompanyMentorViewSet, MentorStudentsViewSet
from django.urls.conf import include, path

router = DefaultRouter()

router.register(r"mentors", CompanyMentorViewSet, basename="mentor")
router.register(r"mentors/students", MentorStudentsViewSet, basename="mentor-students")

urlpatterns = [path("", include(router.urls))]
