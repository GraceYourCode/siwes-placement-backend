from rest_framework.routers import DefaultRouter
from apps.supervisors.views import SupervisorViewSet
from django.urls.conf import include, path

router = DefaultRouter()

router.register(r"supervisors", SupervisorViewSet, basename="supervisor")

urlpatterns = [path("", include(router.urls))]
