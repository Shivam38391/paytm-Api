from rest_framework import serializers

from recharge.models import Planes

class PlaneSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Planes
        fields = "__all__"
