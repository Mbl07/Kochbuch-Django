from django.urls import path
from .views import overview, rezept_upload

urlpatterns = [
    path('', overview),
    path('upload/', rezept_upload),
]