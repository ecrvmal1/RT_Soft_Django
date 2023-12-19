from django.urls import include, path
from mainapp import views

app_name = MainappConfig.name

urlpatterns = [
    path("", views.MainPageView.as_view(), name="index"),
]
