from ..models import Exercice
from rest_framework import serializers, viewsets

class ExerciceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Exercice
        fields = ['name','description','image']




class ExerciceViewSet(viewsets.ModelViewSet):
    queryset = Exercice.objects.all()
    serializer_class = ExerciceSerializer