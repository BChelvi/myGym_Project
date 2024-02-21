# from django.contrib.auth.models import AbstractUser
# from django.db import models

# class User(AbstractUser):
#     # Spécifiez un nom de relation personnalisé pour le champ de groupe
#     mes_groupes = models.ManyToManyField(
#         'auth.Group',
#         verbose_name='groupes auxquels appartient l\'utilisateur',
#         blank=True,
#         related_name='utilisateurs'
#     )