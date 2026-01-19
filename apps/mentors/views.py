from rest_framework.viewsets import ModelViewSet
from apps.mentors.serializers import CompanyMentorSerializer
from apps.companies.models import Company
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated, AllowAny
from apps.mentors.permissions import IsMentor
from apps.mentors.models import CompanyMentor, MentorInvitation
from rest_framework.decorators import action

# from apps.logbooks.models import LogbookEntry
from apps.mentors.utils import get_students_entries
from apps.students.serializers import StudentPlacementSerializer
from apps.students.models import StudentPlacement


class CompanyMentorViewSet(ModelViewSet):
    serializer_class = CompanyMentorSerializer

    def get_permissions(self):
        if self.action in ["verify_invitation"]:
            return [AllowAny()]
        return [IsAuthenticated(), IsMentor()]

    def perform_create(self, serializer):
        user = self.request.user
        company_id = self.request.data.get("company_id")

        company = Company.objects.get(pk=company_id)
        if company.DoesNotExist:
            return Response(
                {"error": "Company Not Found!!"}, status=status.HTTP_404_NOT_FOUND
            )
        serializer.save(user=user, company=company)

    def get_queryset(self):
        user = self.request.user

        return CompanyMentor.objects.filter(user=user)

    @action(detail=False, methods=["post"])
    def approve_students_entries(self, request):
        entries = get_students_entries(request)

        entries.update(status="approved")
        return Response(status=status.HTTP_200_OK)

    @action(detail=False, methods=["post"])
    def reject_students_entries(self, request):
        entries = get_students_entries(request)
        entries.update(status="rejected")
        return Response(status=status.HTTP_200_OK)

    @action(detail=True, methods=["get"])
    def verify_invitation(self, request, pk):
        inivation = MentorInvitation.objects.get(pk=pk, is_used=False)

        if inivation.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        return Response(
            {
                "email": inivation.email,
                "role": inivation.role,
                "company": inivation.company,
            },
            status=status.HTTP_200_OK,
        )


class MentorStudentsViewSet(ModelViewSet):
    serializer_class = StudentPlacementSerializer
    permission_classes = [IsMentor, IsAuthenticated]

    def get_queryset(self):
        mentor = self.request.user.mentorprofile

        return StudentPlacement.objects.filter(mentor=mentor)
