from ..models import ProgressUser
from rest_framework import serializers, viewsets

class ProgressUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProgressUser
        fields = ['user','performance','day']




class ProgressUserViewSet(viewsets.ModelViewSet):
    queryset = ProgressUser.objects.all()
    serializer_class = ProgressUserSerializer