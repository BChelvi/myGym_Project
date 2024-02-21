from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer



# Définissez un sérialiseur personnalisé pour inclure d'autres données de l'utilisateur dans la réponse JWT si nécessaire
class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        # Vous pouvez ajouter d'autres informations de l'utilisateur ici si nécessaire
        # token['user_id'] = user.id
        # token['email'] = user.email

        return token

class CustomTokenObtainPairView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer