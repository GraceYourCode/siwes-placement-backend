from rest_framework.viewsets import ModelViewSet
from apps.institutions.models import InstitutionProfile
from apps.institutions.serializers import InstitutionSerializer
from rest_framework.permissions import IsAuthenticated
from apps.institutions.permissions import IsInstitution


class InstitutionViewSet(ModelViewSet):
    serializer_class = InstitutionSerializer
    permission_classes = [IsAuthenticated, IsInstitution]

    def perform_create(self, serializer):
        user = self.request.user

        serializer.save(user=user)

    def get_queryset(self):
        user = self.request.user
        return InstitutionProfile.objects.filter(user=user)
