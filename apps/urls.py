from django.urls import path, include

urlpatterns = [
    path("", include("apps.logbooks.urls")),
    path("", include("apps.accounts.urls")),
    path("", include("apps.students.urls")),
    path("", include("apps.institutions.urls")),
    path("", include("apps.companies.urls")),
    path("", include("apps.supervisors.urls")),
]
