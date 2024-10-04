from django.urls import path
from .views import sort_array

urlpatterns = [
    path('sort/', sort_array, name='sort_array'),
]