from django.conf import settings
from django.urls import path


from .views import index


urlpatterns = [
    path("", index),

]
