# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-06-09 21:51
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Ticket',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(blank=True, max_length=255, null=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('status', models.CharField(choices=[(b'ABIERTO', b'Abierto'), (b'PENDIENTE', b'Pendiente'), (b'EN PROCESO', b'En proceso'), (b'RESUELTO', b'Resuelto'), (b'CERRADO', b'Cerrado')], default=b'ABIERTO', max_length=20)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'db_table': 'tickets',
                'managed': True,
            },
        ),
    ]
