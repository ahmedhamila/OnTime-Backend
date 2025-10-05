from rest_framework import status
from rest_framework import viewsets
from rest_framework.parsers import FormParser
from rest_framework.parsers import MultiPartParser
from rest_framework.permissions import AllowAny
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from src.employees.models.ClockRecord import ClockRecord
from src.employees.serializers.ClockRecordSerializer import ClockRecordSerializer
from src.employees.services.ClockService import ClockService


class ClockRecordViewSet(viewsets.ModelViewSet):
    queryset = ClockRecord.objects.all().order_by("-timestamp")
    serializer_class = ClockRecordSerializer
    parser_classes = [MultiPartParser, FormParser]

    def get_permissions(self):
        if self.action == "create":
            return [AllowAny()]
        return [IsAuthenticated()]

    def create(self, request, *args, **kwargs):
        clock_record = ClockService.create_clock_record(request)
        serializer = self.get_serializer(clock_record)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
