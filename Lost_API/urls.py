from django.urls import path
from .views import api_data_view

urlpatterns = [
    path('data/', api_data_view, name='api-data'),                  # Handles GET (all) and POST
    path('data/<int:id>/', api_data_view, name='api-data-detail'),  # Handles GET (by ID) and PATCH
]

