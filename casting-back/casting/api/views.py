from django.shortcuts import render

# Create your views here.

# Create your views here.
from django.http import HttpResponse
from django.http.response import HttpResponse, JsonResponse
from rest_framework.response import Response
from api.serializers import CastingSerializer, PositionSerializer
from rest_framework import status
from rest_framework.views import APIView
from .models import Casting,Position
from rest_framework.decorators import api_view 
import json

@api_view(["GET","POST"])
def get_castings(request):
    if request.method == 'GET':
        castings = Casting.objects.all()
        serializer = CastingSerializer(castings, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = CastingSerializer(serializer.data)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.errors, status=status.HTTP_404_NOT_FOUND)
    


    # тут по id будет или по position name-> casting/dance/card1, casting/filming/card2????
@api_view(["GET", "PUT","DELETE"])
def casting_details(request, id):
    try:
        casting=Casting.objects.get(id=id)
    except Casting.DoesNotExist as e :
        return Response({"error": str(e)}, status=status.HTTP_404_NOT_FOUND)
    # ошибка 404
    if request.method == "GET":
        serializer = CastingSerializer(casting)
        return Response(serializer.data)
    
    elif request.method == "PUT":
        serializer = CastingSerializer(
            instance = casting,
            data=request.data
        )
        if serializer.is_valid():
            serializer.save()# update data...
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_404_NOT_FOUND)

    elif request.method  == 'DELETE':
        casting.delete()
        return Response({"deleted": True})
    

def casting_positions(request, id):
    casting = Casting.objects.get(id=id)
    positions = Position.objects.filter(casting=casting)
    positions_json = [position.to_json() for position in positions]
    return JsonResponse(positions_json, safe = False)

  


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
        
        serializer = PositionSerializer(position)
        return Response(serializer.data)
    
    def put(self, request,pk=None):
        try:
            position = Position.objects.get(id=id)
        except Position.DoesNotExist as e:
            return Response({"error": str(e)}, status.HTTP_404_NOT_FOUND)
        
        serializer = PositionSerializer(instance=position, data=request.data)
    
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_404_NOT_FOUND)
    

    def delete(self, request,id=None):
        try:
            position = Position.objects.get(id=id)
        except Position.DoesNotExist as e:
            return Response({"error": str(e)}, status.HTTP_404_NOT_FOUND)
        
        position.delete()
        return Response({"deleted": True})
