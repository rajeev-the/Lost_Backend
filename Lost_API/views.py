from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import ApiData
from .serializers import ApiDataSerializer
from rest_framework import status

@api_view(['GET', 'POST', 'PATCH'])
def api_data_view(request, id=None):
    if request.method == 'GET':
        if id:
            # Retrieve a single item by ID
            try:
                data = ApiData.objects.get(pk=id)
                serializer = ApiDataSerializer(data)
                return Response(serializer.data, status=status.HTTP_200_OK)
            except ApiData.DoesNotExist:
                return Response({"error": "Data not found"}, status=status.HTTP_404_NOT_FOUND)
        else:
            # Retrieve all items
            data = ApiData.objects.all()
            serializer = ApiDataSerializer(data, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
    
    if request.method == 'POST':
        # Create a new item
        serializer = ApiDataSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    if request.method == 'PATCH':
        if id:
            try:
                # Partially update an existing item by ID
                data = ApiData.objects.get(pk=id)
                serializer = ApiDataSerializer(data, data=request.data, partial=True)
                if serializer.is_valid():
                    serializer.save()
                    return Response(serializer.data, status=status.HTTP_200_OK)
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            except ApiData.DoesNotExist:
                return Response({"error": "Data not found"}, status=status.HTTP_404_NOT_FOUND)
        else:
            return Response({"error": "ID is required for PATCH requests"}, status=status.HTTP_400_BAD_REQUEST)
