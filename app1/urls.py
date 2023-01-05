from django.urls import path
from app1.views import *
app_name='something'

urlpatterns=[
    path('specificstatic1/',specificstatic1,name='specificstatic1'),
]