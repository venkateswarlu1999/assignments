from django.urls import path
from .views import *

urlpatterns = [
    path('createauthor/',createauthor),
    path('createlibrary/',createlibrary),
    path('getnames/',getBooknamesFromAuthor)
]
