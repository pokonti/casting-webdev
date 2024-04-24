from django.shortcuts import render
from django.http import HttpResponse
from django.http.response import HttpResponse, JsonResponse
from rest_framework.response import Response
from api.serializers import CastingSerializer, PositionSerializer, PositionSerializer2, AdSerializer
from rest_framework import status
from rest_framework.views import APIView
from .models import Casting, Position, Ad
from rest_framework.decorators import api_view
import json


@api_view(["GET", "POST"])
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


@api_view(["GET", "PUT", "DELETE"])
def casting_details(request, id):
    try:
        casting = Casting.objects.get(id=id)
    except Casting.DoesNotExist as e:
        return Response({"error": str(e)}, status=status.HTTP_404_NOT_FOUND)
    # ошибка 404
    if request.method == "GET":
        serializer = CastingSerializer(casting)
        return Response(serializer.data)

    elif request.method == "PUT":
        serializer = CastingSerializer(
            instance=casting,
            data=request.data
        )
        if serializer.is_valid():
            serializer.save()  # update data...
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_404_NOT_FOUND)

    elif request.method == 'DELETE':
        casting.delete()
        return Response({"deleted": True})


def casting_positions(request, id):
    try:
        casting = Casting.objects.get(id=id)
    except Casting.DoesNotExist as e:
        return JsonResponse({"error": str(e)}, status=404)

    positions = Position.objects.filter(casting=casting)
    serializer = PositionSerializer2(positions, many=True)

    return JsonResponse(serializer.data, safe=False, status=200)


@api_view(["GET", "POST"])
def get_ads(request):
    if request.method == 'GET':
        ad = Ad.objects.all()
        serializer = AdSerializer(ad, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = AdSerializer(serializer.data)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.errors, status=status.HTTP_404_NOT_FOUND)