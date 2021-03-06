# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-08-26 19:24
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(blank=True, max_length=500, null=True, verbose_name='Descri\xe7\xe3o')),
                ('amount', models.IntegerField(blank=True, null=True, verbose_name='Quantidade')),
            ],
            options={
                'verbose_name': 'Pedido',
                'verbose_name_plural': 'Pedidos',
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=50, null=True, verbose_name='Nome')),
                ('description', models.CharField(blank=True, max_length=500, null=True, verbose_name='Descri\xe7\xe3o')),
                ('price', models.FloatField(blank=True, null=True, verbose_name='Pre\xe7o')),
                ('order', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='apploja.Order', verbose_name='Pedido')),
            ],
            options={
                'verbose_name': 'Produto',
                'verbose_name_plural': 'Produtos',
            },
        ),
    ]
