from django.conf.urls import url

from project.apps.users.views import UsersView


app_name = 'users'
urlpatterns = [
    url(
        r'users/detail/$',
        UsersView.as_view(),
        name='detail',
    )
]
