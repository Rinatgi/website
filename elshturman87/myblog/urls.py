from django.conf import settings
from django.urls import path
from . import views

from .views import index


urlpatterns = [
    path("", index),
    path("blog/", views.PostView.as_view())

]
 