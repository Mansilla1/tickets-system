# -*- coding: utf-8 -*-
from rest_framework import (
    fields,
    serializers,
)

from project.apps.tickets.models import Ticket


class TicketsCreateSerializer(serializers.Serializer):
    STATUS_CHOICES = (
        ('ABIERTO', 'Abierto'),
        ('PENDIENTE', 'Pendiente'),
        ('EN PROCESO', 'En proceso'),
        ('RESUELTO', 'Resuelto'),
        ('CERRADO', 'Cerrado'),
    )

    title = fields.CharField(max_length=255, required=False)
    description = fields.CharField(required=False)
    status = fields.ChoiceField(choices=STATUS_CHOICES, required=False, default='ABIERTO')


class TicketsListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Ticket
        fields = '__all__'
