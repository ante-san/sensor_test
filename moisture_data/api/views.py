from datetime import datetime
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import AddMoistureDataSerializer
from moisture_data.models import MoistureData, Plant

class MoistureDataAccess(APIView):

    def post(self, request):
        serializer = AddMoistureDataSerializer(data=request.data)
        if serializer.is_valid():
            moisture_data = serializer.save()
            if moisture_data:
                json = serializer.data
                return Response(json, status = status.HTTP_201_CREATED)
            
    def get(self, request):
        moisture_data = MoistureData.objects.all()
        serializer = AddMoistureDataSerializer(moisture_data, many=True)
        return Response(serializer.data)