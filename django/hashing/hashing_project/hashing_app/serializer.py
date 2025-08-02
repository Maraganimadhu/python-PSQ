from .models import STUDENT
from rest_framework import serializers

class STUDENTSerializer(serializers.ModelSerializer):
    class Meta:
        model=STUDENT
        fields="__all__"
