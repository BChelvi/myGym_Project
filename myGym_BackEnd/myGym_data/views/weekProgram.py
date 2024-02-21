from ..models import WeekProgram
from rest_framework import serializers, viewsets

class WeekProgramSerializer(serializers.ModelSerializer):
    class Meta:
        model = WeekProgram
        fields = ['week_number']




class WeekProgramViewSet(viewsets.ModelViewSet):
    queryset = WeekProgram.objects.all()
    serializer_class = WeekProgramSerializer