from rest_framework.routers import DefaultRouter
from apps.accounts.views import UserViewSet
from django.urls.conf import path, include
from rest_framework_simplejwt.views import TokenRefreshView

router = DefaultRouter()

router.register(r"users", UserViewSet, basename="user")

urlpatterns = [
    path(
        "users/auth/token_refresh/",
        TokenRefreshView.as_view(permission_classes=[]),
        name="token_refresh",
    ),
]

urlpatterns += router.urls
