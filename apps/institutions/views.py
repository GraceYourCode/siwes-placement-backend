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
from apps.students.serializers import StudentPlacementSerializer
from apps.students.models import StudentPlacement


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


class InstitutionStudentsViewSet(ModelViewSet):
    serializer_class = StudentPlacementSerializer
    permission_classes = [IsInstitution, IsAuthenticated]

    def get_queryset(self):
        institution = self.request.user.institutionprofile

        return StudentPlacement.objects.filter(institution=institution)


class InstitutionSupervisorsViewSet(ModelViewSet):
    serializer_class = SupervisorSerializer
    permission_classes = [IsInstitution, IsAuthenticated]

    def get_queryset(self):
        institution = self.request.user.institutionprofile

        return SupervisorProfile.objects.filter(
            institution=institution, is_verified=True
        )
