from rest_framework import serializers
from .models import Students


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Students
        fields = ("pk", "name", "email", "document", "phone", "registrationDate")
