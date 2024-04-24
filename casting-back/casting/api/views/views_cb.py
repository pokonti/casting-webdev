from django.shortcuts import render
from django.http import HttpResponse
from django.http.response import HttpResponse, JsonResponse
from rest_framework.response import Response
from api.serializers import PositionSerializer, PositionSerializer2
from rest_framework import status
from rest_framework.views import APIView
from .models import Position
from rest_framework.decorators import api_view
import json


class PositionstListAPIView(APIView):
    def get(sef, request):
        positions = Position.objects.all()
        serializer = PositionSerializer(positions, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = PositionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_404_NOT_FOUND)



class PositionsDetailAPIView(APIView):
    def get(self, request, id=None):
        try:
            position = Position.objects.get(id=id)
        except Position.DoesNotExist as e:
            return Response({"error": str(e)}, status.HTTP_404_NOT_FOUND)

        serializer = PositionSerializer2(position)
        return Response(serializer.data)

    def put(self, request, id=None):
        try:
            position = Position.objects.get(id=id)
        except Position.DoesNotExist as e:
            return Response({"error": str(e)}, status.HTTP_404_NOT_FOUND)

        serializer = PositionSerializer2(instance=position, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_404_NOT_FOUND)

    def delete(self, request, id=None):
        try:
            position = Position.objects.get(id=id)
        except Position.DoesNotExist as e:
            return Response({"error": str(e)}, status.HTTP_404_NOT_FOUND)

        position.delete()
        return Response({"deleted": True})

