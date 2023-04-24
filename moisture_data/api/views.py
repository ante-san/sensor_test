from datetime import datetime
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import AddMoistureDataSerializer

class AddMoistureData(APIView):

    def post(self, request):
        data = request.data
        serializer = AddMoistureDataSerializer(data=request.data)
        if serializer.is_valid():
            moisture_data = serializer.save()
            if moisture_data:
                json = serializer.data
                return Response(json, status = status.HTTP_201_CREATED)