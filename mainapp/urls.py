from django.urls import include, path

from mainapp import views

app_name = "mainapp"

urlpatterns = [
    path("", views.MainPageView.as_view(), name="index"),
]
