
from django.urls import path
import webIndex.views as wv


urlpatterns = [
    path('', wv.index),
]