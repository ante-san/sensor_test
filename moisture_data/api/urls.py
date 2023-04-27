from django.urls import path
from .views import MoistureDataAccess

urlpatterns = [
    path('add_moisture_data/', MoistureDataAccess.as_view())
]