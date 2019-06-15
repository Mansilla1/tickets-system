# -*- coding: utf-8 -*-
from django.db import models
from django.conf import settings


class Ticket(models.Model):
    _DATABASE = 'challenge'
    STATUS_CHOICES = (
        ('ABIERTO', 'Abierto'),
        ('PENDIENTE', 'Pendiente'),
        ('EN PROCESO', 'En proceso'),
        ('RESUELTO', 'Resuelto'),
        ('CERRADO', 'Cerrado'),
    )

    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, default=1)
    title = models.CharField(max_length=255, blank=True, null=True)
    description = models.TextField(null=True, blank=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='ABIERTO')
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        managed = True
        db_table = 'tickets'

    def __unicode__(self):
        return '#{}'.format(self.id)
