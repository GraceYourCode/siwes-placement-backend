from rest_framework.viewsets import ModelViewSet
from apps.institutions.models import InstitutionProfile
from apps.institutions.serializers import InstitutionSerializer
from rest_framework.permissions import IsAuthenticated
from apps.institutions.permissions import IsInstitution
from rest_framework.decorators import action
from apps.institutions.utils import get_supervisors
from apps.supervisors.models import SupervisorProfile
from rest_framework.response import Response
from rest_framework import status
from apps.supervisors.serializers import SupervisorSerializer


class InstitutionViewSet(ModelViewSet):
    serializer_class = InstitutionSerializer
    permission_classes = [IsAuthenticated, IsInstitution]

    def perform_create(self, serializer):
        user = self.request.user

        serializer.save(user=user)

    def get_queryset(self):
        user = self.request.user
        return InstitutionProfile.objects.filter(user=user)

    @action(detail=False, methods=["post"])
    def verify_supervisors(self, request):
        supervisors = get_supervisors(request)
        supervisors.update(is_verified=True)
        return Response(status=status.HTTP_200_OK)

    @action(detail=False, methods=["post"])
    def reject_supervisors(self, request):
        supervisors = get_supervisors(request)
        supervisors.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    @action(detail=False, methods=["get"])
    def supervisors(self, request):
        institution = request.user.institutionprofile
        supervisors = SupervisorProfile.objects.filter(institution=institution)
        serializer = SupervisorSerializer(supervisors, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)
