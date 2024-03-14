from django.db import models


class clpModel(models.Model):
    Sensor = models.BooleanField()
    Botao = models.BooleanField()
    LigaRobo = models.BooleanField()
    ResetContador = models.BooleanField()
    ValorContagem = models.IntegerField()

    def __str__(self) -> str:
        return self.value
