from rest_framework.viewsets import ModelViewSet

from .models import StudentInstitutionProfile
from .serializers import StudentInstitutionProfileSerializer
from rest_framework.permissions import IsAuthenticated
from apps.students.permissions import IsStudent
from apps.logbooks.models import Logbook
from apps.institutions.models import InstitutionProfile


class StudentInstitutionProfileViewSet(ModelViewSet):
    queryset = StudentInstitutionProfile.objects.all()
    serializer_class = StudentInstitutionProfileSerializer
    permission_classes = [IsAuthenticated, IsStudent]

    def perform_create(self, serializer):
        user = self.request.user
        institution_id = self.request.data.get("institution")

        institution = InstitutionProfile.objects.get(pk=institution_id)
        student = serializer.save(user=user, institution=institution)

        Logbook.objects.create(student=student)
