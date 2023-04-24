from django.urls import path
from .views import AddMoistureData

urlpatterns = [
    path('add_moisture_data/', AddMoistureData.as_view())
]