from django.urls import path
from .views import MoistureData

urlpatterns = [
    path('add_moisture_data/', MoistureData.as_view())
]