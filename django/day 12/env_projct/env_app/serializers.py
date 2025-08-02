from rest_framework import serializers
from .models import EMPLOY

class EmpSerializer(serializers.ModelSerializer):
    class Meta:
        model=EMPLOY
        fields="__all__"
