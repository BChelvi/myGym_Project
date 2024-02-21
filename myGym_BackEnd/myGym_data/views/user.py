from django.contrib.auth.models import User
from rest_framework import serializers, viewsets
from rest_framework.authtoken.models import Token
from rest_framework.permissions import IsAuthenticated
# from rest_framework.authentication import TokenAuthentication
from rest_framework_simplejwt.authentication import JWTAuthentication

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'password', 'email']
        extra_kwargs = {'password': {'write_only': True}}



class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    
    # Exclure l'authentification et la permission pour l'action de création
    def create(self, request, *args, **kwargs):
        self.authentication_classes = []
        self.permission_classes = []
        return super().create(request, *args, **kwargs)

    # Définir explicitement l'authentification et la permission pour les autres actions
    def update(self, request, *args, **kwargs):
        self.authentication_classes = []
        self.permission_classes = []
        return super().update(request, *args, **kwargs)