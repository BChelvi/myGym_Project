from ..models import Series
from rest_framework import serializers, viewsets

class SeriesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Series
        fields = ['number_serie','number_repetitions','weight']



class SeriesViewSet(viewsets.ModelViewSet):
    queryset = Series.objects.all()
    serializer_class = SeriesSerializer