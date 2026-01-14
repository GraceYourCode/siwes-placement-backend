from rest_framework.viewsets import ModelViewSet
from .models import LogbookEntry, Reviews, Logbook
from .serializers import LogbookEntrySerializer, ReviewSerializer, LogbookSerializer
from apps.students.models import StudentInstitutionProfile, StudentPlacement
from rest_framework.exceptions import PermissionDenied
from rest_framework.permissions import IsAuthenticated
from apps.logbooks.utils import if_not_student_restrict_other_users
from apps.supervisors.permissions import IsSupervisor
from apps.students.permissions import IsStudent, IsPlacementValid


class LogbookEntryViewset(ModelViewSet):
    queryset = LogbookEntry.objects.all()
    serializer_class = LogbookEntrySerializer

    def get_permissions(self):
        user = self.request.user

        if user.role == "supervisor":
            return [IsAuthenticated(), IsSupervisor()]
        elif user.role == "student":
            return [IsAuthenticated(), IsStudent(), IsPlacementValid()]
        return False

    def get_queryset(self):
        user = self.request.user

        if user.role == "student":
            return LogbookEntry.objects.filter(logbook__student__user=user)

        if user.role == "supervisor":
            print("Na supervisor Ibe")
            return LogbookEntry.objects.filter(placement__supervisor__user=user)

        return LogbookEntry.objects.none()

    def perform_create(self, serializer):
        user = self.request.user

        if_not_student_restrict_other_users(user, "add")

        student = StudentInstitutionProfile.objects.get(user=user)

        logbook = Logbook.objects.get(student=student)
        placement = StudentPlacement.objects.get(student=student, is_active=True)

        serializer.save(logbook=logbook, placement=placement)

    def perform_update(self, serializer):
        entry = self.get_object()
        user = self.request.user

        if_not_student_restrict_other_users(user, "update")

        if entry.status == "approved":
            raise PermissionDenied("You can't edit an already approved entry")

        if user != entry.logbook.student.user:
            raise PermissionDenied("You can only edit your logbook entries")

        serializer.save()

    def perform_destroy(self, instance):
        user = self.request.user

        if_not_student_restrict_other_users(user, "delete")

        if instance.status == "approved":
            raise PermissionDenied("You can't delete an already approved entry")

        if user != instance.logbook.student.user:
            raise PermissionDenied("You can only delete your logbook entries")

        instance.delete()


class ReviewViewset(ModelViewSet):
    queryset = Reviews.objects.all()
    serializer_class = ReviewSerializer


class LogbookViewset(ModelViewSet):
    queryset = Logbook.objects.all()
    serializer_class = LogbookSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user

        if user.role == "institution":
            return Logbook.objects.filter(student__institution__user=user)

        if user.role == "student":
            return Logbook.objects.filter(student__user=user)
