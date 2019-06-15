# -*- coding: utf-8 -*-
from rest_framework.generics import (
    CreateAPIView,
    ListAPIView,
)
from rest_framework.response import Response
from rest_framework.renderers import JSONRenderer
from rest_framework import status

from project.apps.tickets.models import Ticket
from project.apps.tickets.serializers import (
    TicketsCreateSerializer,
    TicketsListSerializer,
)


class TicketsCreateView(CreateAPIView):
    renderer_classes = (JSONRenderer,)

    @staticmethod
    def post(request):
        ticket_serializer = TicketsCreateSerializer(data=request.data)

        if ticket_serializer.is_valid():
            ticket = Ticket.objects.create(
                title=ticket_serializer.validated_data['title'],
                description=ticket_serializer.validated_data['description'],
                status=ticket_serializer.validated_data['status'],
            )
            response = Response(
                {
                    'msg': 'OK',
                    'result': 'ticket: #{} has been created'.format(ticket.id),
                },
                status=status.HTTP_201_CREATED,
            )

        else:
            response = Response(
                {
                    'msg': 'Request is not valid',
                    'errors': ticket_serializer.errors,
                },
                status=status.HTTP_400_BAD_REQUEST,
            )

        return response


class TicketsListView(ListAPIView):
    queryset = Ticket.objects.all().order_by('-id')
    serializer_class = TicketsListSerializer
    paginate_by = 10
