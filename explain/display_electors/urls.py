from django.urls import path
from . import views

app_name = 'display_electors'

urlpatterns = [
    path('', views.index, name="index")
]

