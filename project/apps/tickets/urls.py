from django.conf.urls import url

from project.apps.tickets.views import (
    TicketsCreateView,
    TicketsListView,
)


app_name = 'tickets'
urlpatterns = [
    url(
        r'tickets/new/$',
        TicketsCreateView.as_view(),
        name='new',
    ),
    url(
        r'tickets/list/$',
        TicketsListView.as_view(),
        name='list',
    ),
]
