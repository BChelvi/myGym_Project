from ..models import WorkoutProgram
from rest_framework import serializers, viewsets
from rest_framework.authtoken.models import Token
from rest_framework.permissions import IsAuthenticated
# from rest_framework.authentication import TokenAuthentication
from rest_framework_simplejwt.authentication import JWTAuthentication

class WorkoutProgramSerializer(serializers.ModelSerializer):
    class Meta:
        model = WorkoutProgram
        fields = ['name', 'description']

class WorkoutProgramViewSet(viewsets.ModelViewSet):
    queryset = WorkoutProgram.objects.all()
    serializer_class = WorkoutProgramSerializer