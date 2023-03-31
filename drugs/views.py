from rest_framework import viewsets, status
from rest_framework.response import Response
from .models import Drug
from .serializers import DrugSerializer
from restful.database import db

class DrugViewSet(viewsets.ViewSet):

    def list(self, request):
        queryset = db.query(Drug).all()
        serializer = DrugSerializer(queryset, many=True)
        return Response(serializer.data)

    def create(self, request):
        serializer = DrugSerializer(data=request.data)
        if serializer.is_valid():
            drug = Drug(**serializer.validated_data)
            db.add(drug)
            db.commit()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # Add more methods as needed, e.g., retrieve, update, partial_update, destroy
