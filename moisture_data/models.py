from django.db import models
from django.db.models.deletion import CASCADE
from django.utils import timezone

# Create your models here.
class Plant(models.Model):

    plant_name = models.CharField(max_length=255)

    class Meta:
        verbose_name_plural = "Plants"

    def __str__(self):
        return self.plant_name
    
class MoistureData(models.Model):

    plant = models.ForeignKey(Plant, on_delete=CASCADE)
    moisture = models.FloatField()

    class Meta:
        verbose_name_plural = "Moisture Data"

    def __str__(self):
        return f"{self.plant} {self.moisture}%"