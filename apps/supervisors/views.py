from rest_framework.viewsets import ModelViewSet
from apps.supervisors.models import SupervisorProfile
from rest_framework.permissions import IsAuthenticated
from apps.supervisors.permissions import IsSupervisor
from apps.supervisors.serializers import SupervisorSerializer
from apps.institutions.models import InstitutionProfile


class SupervisorViewSet(ModelViewSet):
    permission_classes = [IsAuthenticated, IsSupervisor]
    serializer_class = SupervisorSerializer

    def perform_create(self, serializer):
        user = self.request.user
        institution_id = self.request.data.get("institution_id")

        institution = InstitutionProfile.objects.get(pk=institution_id)
        serializer.save(user=user, institution=institution)

    def get_queryset(self):
        user = self.request.user

        return SupervisorProfile.objects.filter(user=user)
