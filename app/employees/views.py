from rest_framework import generics, permissions
from .models import Employee, Vote
from .serializers import EmployeeSerializer, VoteSerializer
from datetime import date

class CreateEmployeeView(generics.CreateAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class VoteView(generics.CreateAPIView):
    queryset = Vote.objects.all()
    serializer_class = VoteSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def perform_create(self, serializer):
        employee = Employee.objects.get(user=self.request.user)
        serializer.save(employee=employee, date=date.today())

class GetResultsView(generics.ListAPIView):
    serializer_class = VoteSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def get_queryset(self):
        return Vote.objects.filter(date=date.today())