from rest_framework.viewsets import ModelViewSet
from apps.companies.serializers import CompanySerializer
from rest_framework.permissions import IsAuthenticated
from apps.companies.models import Company


class CompanyViewSet(ModelViewSet):
    serializer_class = CompanySerializer
    permission_classes = [IsAuthenticated]
    queryset = Company.objects.all()
