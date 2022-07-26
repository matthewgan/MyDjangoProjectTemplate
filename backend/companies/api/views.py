from rest_framework.viewsets import ModelViewSet

from ..models import Company
from .serializers import CompanySerializer


class CompanyViewSet(ModelViewSet):
    serializer_class = CompanySerializer
    queryset = Company.objects.all()
