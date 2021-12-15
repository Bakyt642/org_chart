from django.shortcuts import render
from rest_framework.generics import ListAPIView

from .models import Staff
from .serializer import StaffSerializer


class StaffList(ListAPIView):
    queryset = Staff.objects.filter(parent__isnull=True)
    serializer_class = StaffSerializer