# coding: utf-8

from __future__ import unicode_literals
from django.db import models


class Order(models.Model):
    description = models.CharField(
        verbose_name='Descrição',
        max_length=500,
        blank=True,
        null=True
    )

    def __unicode__(self):
        return self.description

    """
    def get_price(self):
        ''' Retorna preço total do pedido
        '''
        pass
    """

    class Meta:
        verbose_name = u'Pedido'
        verbose_name_plural = u'Pedidos'


class Product(models.Model):
    name = models.CharField(
        verbose_name='Nome',
        max_length=50,
        blank=True,
        null=True
    )
    description = models.CharField(
        verbose_name='Descrição',
        max_length=500,
        blank=True,
        null=True
    )
    price = models.FloatField(
        verbose_name='Preço',
        blank=True,
        null=True
    )
    order = models.ForeignKey(
        Order,
        verbose_name='Pedido',
        blank=True,
        null=True
    )

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name = u'Produto'
        verbose_name_plural = u'Produtos'
