from django.db import models

class Series(models.Model):
    performance = models.ForeignKey('Performance',related_name='series', on_delete=models.CASCADE)
    number_serie = models.IntegerField()
    number_repetitions = models.IntegerField()
    weight = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return f"Numero de serie : {self.number_serie} Nombre de répétitions : {self.number_repetitions}, Poids :{self.weight}"