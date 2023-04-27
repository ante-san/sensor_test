from rest_framework import serializers
from moisture_data.models import MoistureData, Plant


# Moisture Data
class AddMoistureDataSerializer(serializers.ModelSerializer):

    class Meta:
        fields = '__all__'
        model = MoistureData

    def create(self, validated_data):
        instance = self.Meta.model(**validated_data)
        instance.save()
        return instance
    


# Plants
class AddPlant(serializers.ModelSerializer):

    class Meta:
        fields = '__all__'
        model = Plant

    def create(self, validated_data):
        instance = self.Meta.model(**validated_data)
        instance.save()
        return instance
