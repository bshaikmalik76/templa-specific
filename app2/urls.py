from django.urls import path
from app2.views import *
app_name='some2'


urlpatterns=[
    path('sec/',sec,name='sec')
]