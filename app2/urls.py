from django.urls import path
from app2.views import *
app_name='something'

urlpatterns=[
    path('specificstatic2/',specificstatic2,name='specificstatic2'),
]