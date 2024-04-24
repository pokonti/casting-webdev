from django.shortcuts import render

# Create your views here.

# Create your views here.
from django.http import HttpResponse
from django.http.response import HttpResponse, JsonResponse
from .models import Casting
from django.views.decorators.csrf import csrf_exempt 
import json

@csrf_exempt
def get_castings(request):
    if request.method == 'GET':
        castings = Casting.objects.all()
        castings_json = [casting.to_json() for casting in castings]
        return JsonResponse(castings_json , safe = False)
    elif request.method == 'POST':
        data = json.loads(request.body)
        casting = Casting.objects.create(name=data.data("name"))
        return JsonResponse(casting.to_json)
