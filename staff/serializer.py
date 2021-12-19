from rest_framework import serializers
from .models import Staff
from rest_framework_recursive.fields import RecursiveField


class StaffSerializer(serializers.ModelSerializer) :
    children = RecursiveField(many=True)

    class Meta :
        model = Staff
        fields = ('__all__')  # all fields to be displayed by API call
