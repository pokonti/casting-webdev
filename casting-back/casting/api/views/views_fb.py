
from rest_framework.response import Response
from api.serializers import ApplicationsSerializer, CastingSerializer, FormSerializer, PositionSerializer
from rest_framework import status
from api.models import ApplicantToPosition, Casting, Form, Position, Ad
from rest_framework.decorators import api_view

# list of castings 
@api_view(["GET", "POST"])
def castings_list(request):
    if request.method == 'GET':
        castings = Casting.objects.all()
        serializer = CastingSerializer(castings, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = CastingSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# one casting
@api_view(["GET", "PUT", "DELETE"])
def casting_details(request, id=None):
    try:
        casting = Casting.objects.get(id=id)
    except Casting.DoesNotExist as e:
        return Response({"error":str(e)}, status=status.HTTP_400_BAD_REQUEST)
    
    if request.method == "GET":
        serializer = CastingSerializer(casting)
        return Response(serializer.data)
    elif request.method == "PUT":
      
        serializer = CastingSerializer(
            instance=casting,
            data=request.data
        )
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == "DELETE":
        casting.delete()
        return Response({"deleted": True})


# positions of a casting
@api_view(["GET", "POST"])
def casting_positions(request, id):
    try:
        casting = Casting.objects.get(id=id)
    except Casting.DoesNotExist as e:
        return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)
    
    if request.method == 'GET':
        positions = Position.objects.filter(casting=casting)
        serializer = PositionSerializer(positions, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = PositionSerializer(data=request.data, context={'casting': casting})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

  

# list of profile
@api_view(["GET", "POST"])
def form_list(request):
    if request.method == 'GET':
        forms = Form.objects.all()
        serializer = FormSerializer(forms, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = FormSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(["GET", "PUT", "DELETE"])
def form_details(request, id=None):
    try:
        form = Form.objects.get(user=id)
    except Casting.DoesNotExist as e:
        return Response({"error":str(e)}, status=status.HTTP_400_BAD_REQUEST)
    
    if request.method == "GET":
        serializer = FormSerializer(form)
        return Response(serializer.data)
    elif request.method == "PUT":
      
        serializer = FormSerializer(
            instance=form,
            data=request.data
        )
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == "DELETE":
        form.delete()
        return Response({"deleted": True})



# a table of Profile and Position      
@api_view(["GET", "POST"])
def appToPos(request):
    if request.method == 'GET':
        forms = ApplicantToPosition.objects.all()
        serializer = ApplicationsSerializer(forms, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = ApplicationsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    
