from django.urls import include, path

from mainapp import views
from mainapp.apps import MainappConfig

app_name = MainappConfig.name

urlpatterns = [
    path("", views.MainPageView.as_view(), name="index"),
    path("static/", views.StaticPageView.as_view(), name="static"),
]
