from rest_framework.routers import DefaultRouter
from apps.accounts.views import UserViewSet
from django.urls.conf import path, include
from rest_framework_simplejwt.views import TokenRefreshView

router = DefaultRouter()

router.register(r"users", UserViewSet, basename="user")

urlpatterns = [
    path(
        "users/auth/refresh_token/",
        TokenRefreshView.as_view(permission_classes=[]),
        name="refresh_token",
    ),
]

urlpatterns += router.urls
