from ..models import DayProgram
from rest_framework import serializers, viewsets

class DayProgramSerializer(serializers.ModelSerializer):
    class Meta:
        model = DayProgram
        fields = ['day_number','workout_week','exercises']



class DayProgramViewSet(viewsets.ModelViewSet):
    queryset = DayProgram.objects.all()
    serializer_class = DayProgramSerializer