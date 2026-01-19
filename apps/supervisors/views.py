from rest_framework.viewsets import ModelViewSet
from apps.supervisors.models import SupervisorProfile
from rest_framework.permissions import IsAuthenticated
from apps.supervisors.permissions import IsSupervisor
from apps.supervisors.serializers import SupervisorSerializer
from apps.institutions.models import InstitutionProfile
from rest_framework.decorators import action
from apps.supervisors.utils import get_placements
from rest_framework.response import Response
from rest_framework import status
from apps.students.models import StudentPlacement
from apps.students.serializers import StudentPlacementSerializer


class SupervisorViewSet(ModelViewSet):
    permission_classes = [IsAuthenticated, IsSupervisor]
    serializer_class = SupervisorSerializer

    def perform_create(self, serializer):
        user = self.request.user
        institution_id = self.request.data.get("institution_id")

        institution = InstitutionProfile.objects.get(pk=institution_id)
        if institution.DoesNotExist:
            return Response(
                {"error": "Institution Not Found!!"}, status=status.HTTP_404_NOT_FOUND
            )
        serializer.save(user=user, institution=institution)

    def get_queryset(self):
        user = self.request.user

        return SupervisorProfile.objects.filter(user=user)

    @action(detail=False, methods=["post"])
    def verify_students_placement(self, request):
        placements = get_placements(request)
        placements.update(is_verified=True)
        return Response(status=status.HTTP_200_OK)

    @action(detail=False, methods=["post"])
    def reject_students_placement(self, request):
        placements = get_placements(request)
        placements.delete()

        return Response(status=status.HTTP_204_NO_CONTENT)


class SupervisorStudentsViewSet(ModelViewSet):
    serializer_class = StudentPlacementSerializer
    permission_classes = [IsSupervisor, IsAuthenticated]

    def get_queryset(self):
        supervisor = self.request.user.supervisorprofile

        return StudentPlacement.objects.filter(supervisor=supervisor)
