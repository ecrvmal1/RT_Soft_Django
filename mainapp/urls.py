from django.urls import include, path

from mainapp import views
from mainapp.apps import MainappConfig

app_name = "mainapp"

urlpatterns = [
    path("", views.MainPageView.as_view(), name="index"),
]
