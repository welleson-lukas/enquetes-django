from django.db import models


class Questao(models.Model):
    questao_texto = models.CharField(max_length=200)
    pub_data = models.DateTimeField('Data de publicação')

    def __str__(self):
        return self.questao_texto


class Choice(models.Model):
    questao = models.ForeignKey(Questao, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votos = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text
