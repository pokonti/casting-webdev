
from rest_framework.response import Response
from api.serializers import AdSerializer, PositionSerializer, UserSerializer
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from api.models import Ad, Casting, Position


class PositionListAPIView(APIView):
    def get(self, request):
        positions = Position.objects.all()
        serializer = PositionSerializer(positions, many=True)
        return Response(serializer.data)
    def post(self, request):
        serializer = PositionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_404_NOT_FOUND)


class AdListAPIView(APIView):
    def get(self, request):
        ads = Ad.objects.all()
        serializer = AdSerializer(ads, many=True)
        return Response(serializer.data)
    def post(self, request):
        serializer = AdSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_404_NOT_FOUND)




class CastingPositionsView(APIView):
    permission_classes = (IsAuthenticated,)

    def get_casting(self, id):
        try:
            return Casting.objects.get(id=id)
        except Casting.DoesNotExist as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request, id):
        casting = self.get_casting(id)

        positions = Position.objects.filter(casting=casting)
        serializer = PositionSerializer(positions, many=True)
        return Response(serializer.data)

    def post(self, request, id):
        casting = self.get_casting(id)
      
        serializer = PositionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(casting=casting)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserProfileView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = request.user
        serializer = UserSerializer(user)
        return Response(serializer.data, status=status.HTTP_200_OK)