from rest_framework.routers import DefaultRouter
from apps.companies.views import CompanyViewSet
from django.urls.conf import include, path

router = DefaultRouter()

router.register(r"companies", CompanyViewSet, basename="company")

urlpatterns = [path("", include(router.urls))]
