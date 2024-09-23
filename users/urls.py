from django.urls import path

from .views import HelloWorldView

app_name = "users"

urlpatterns = [
    path("xok", HelloWorldView.as_view(), name="hello_world")
]
