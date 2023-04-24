from django.contrib import admin
from .models import Plant, MoistureData

class PlantInfo(admin.ModelAdmin):
    pass

admin.site.register(Plant, PlantInfo)
admin.site.register(MoistureData, PlantInfo)