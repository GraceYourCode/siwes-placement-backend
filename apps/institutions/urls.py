from rest_framework.routers import DefaultRouter
from apps.institutions.views import InstitutionViewSet
from django.urls.conf import include, path

router = DefaultRouter()

router.register(r"institutions", InstitutionViewSet, basename="institution")

urlpatterns = [path("", include(router.urls))]
