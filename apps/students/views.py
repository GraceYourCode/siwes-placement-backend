from rest_framework.viewsets import ModelViewSet

from .models import StudentInstitutionProfile
from .serializers import StudentInstitutionProfileSerializer
from rest_framework.permissions import IsAuthenticated
from apps.students.permissions import IsStudent
from apps.logbooks.models import Logbook
from apps.institutions.models import InstitutionProfile
from apps.students.models import StudentPlacement
from apps.students.serializers import StudentPlacementSerializer
from apps.students.services import assign_supervisor
from apps.students.utils import get_company
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status
from apps.mentors.models import MentorInvitation


class StudentInstitutionProfileViewSet(ModelViewSet):
    queryset = StudentInstitutionProfile.objects.all()
    serializer_class = StudentInstitutionProfileSerializer
    permission_classes = [IsAuthenticated, IsStudent]

    def perform_create(self, serializer):
        user = self.request.user
        institution_id = self.request.data.get("institution_id")

        institution = InstitutionProfile.objects.get(pk=institution_id)
        student = serializer.save(user=user, institution=institution)

        Logbook.objects.create(student=student)

    def get_queryset(self):
        user = self.request.user
        return StudentInstitutionProfile.objects.filter(user=user)


class StudentPlacementViewSet(ModelViewSet):
    permission_classes = [IsAuthenticated, IsStudent]
    serializer_class = StudentPlacementSerializer

    def perform_create(self, serializer):
        company_id = self.request.data.get("company_id")

        student = self.request.user.studentinstitutionprofile
        supervisor = assign_supervisor(student)
        company = get_company(company_id)

        serializer.save(supervisor=supervisor, student=student, company=company)

    def get_queryset(self):
        user = self.request.user

        return StudentPlacement.objects.filter(student=user.studentinstitutionprofile)

    @action(detail=False, methods=["post"])
    def invite_mentor(self, request):
        email = request.data.get("mentor_email")
        company = request.user.studentplacement.company
        invitation = MentorInvitation.objects.create(email=email, company=company)

        return Response(
            {"message": f"Invitation email sent to {email}", invitation: invitation},
            status=status.HTTP_200_OK,
        )
