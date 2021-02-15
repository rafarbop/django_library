"""Models to Database."""

from django.db import models

# Create your models here.

MES = (
        ('janeiro', 'Janeiro'),
        ('fevereiro', 'Fevereiro'),
        ('marco', 'Março'),
        ('abril', 'Abril'),
        ('maio', 'Maio'),
        ('junho', 'Junho'),
        ('julho', 'Julho'),
        ('agosto', 'Agosto'),
        ('setembro', 'Setembro'),
        ('outubro', 'Outubro'),
        ('novembro', 'Novembro'),
        ('dezembro', 'Dezembro'),
        )


class Receitas(models.Model):
    """Cria Novo Modelo de dados de Receitas."""

    list_salario = models.TextField(null=True)
    mes_receitas = models.CharField(max_length=10,
                                    choices=MES,
                                    default='Janeiro')

    def __str__(self):
        """Representar Objeto com o mês do próprio objeto."""
        return self.mes_receitas


class Despesas(models.Model):
    """Cria Novo Modelo de dados de Despesas."""

    list_despesas = models.TextField(null=True)
    mes_despesas = models.CharField(max_length=10,
                                    choices=MES,
                                    default='Janeiro')

    def __str__(self):
        """Representar Objeto com o mês do próprio objeto."""
        return self.mes_despesas


class Aplicacoes(models.Model):
    """Cria Novo Modelo de dados de Aplicações."""

    list_aplicacoes = models.TextField(null=True)
    mes_aplicacoes = models.CharField(max_length=10,
                                      choices=MES,
                                      default='Janeiro')

    def __str__(self):
        """Representar Objeto com o mês do próprio objeto."""
        return self.mes_aplicacoes
