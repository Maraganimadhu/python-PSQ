from rest_framework import serializers
from.models import USER

class Userserilizer(serializers.ModelSerializer):
    class Meta:
        model=USER
        fields="__all__"
