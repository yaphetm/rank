from django.conf.urls import url, include
from .views import Rank


urlpatterns=[
    url(r'^rank/$', Rank.as_view(), name='rank'),
]