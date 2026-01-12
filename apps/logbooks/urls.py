from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import LogbookEntryViewset, LogbookViewset

router = DefaultRouter()
router.register(r"logbook-entries", LogbookEntryViewset, basename="logbook-entry")
router.register(r"logbooks", LogbookViewset, basename="logbook")

urlpatterns = [
    path("", include(router.urls)),
]
