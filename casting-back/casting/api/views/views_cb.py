
from rest_framework.response import Response
from api.serializers import AdSerializer, PositionSerializer
from rest_framework import status
from rest_framework.views import APIView
from api.models import Ad, Position


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






# class PositionsDetailAPIView(APIView):
#     def get(self, request, id=None):
#         try:
#             position = Position.objects.get(id=id)
#         except Position.DoesNotExist as e:
#             return Response({"error": str(e)}, status.HTTP_404_NOT_FOUND)

#         serializer = PositionSerializer2(position)
#         return Response(serializer.data)

#     def put(self, request, id=None):
#         try:
#             position = Position.objects.get(id=id)
#         except Position.DoesNotExist as e:
#             return Response({"error": str(e)}, status.HTTP_404_NOT_FOUND)

#         serializer = PositionSerializer2(instance=position, data=request.data)

#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_404_NOT_FOUND)

#     def delete(self, request, id=None):
#         try:
#             position = Position.objects.get(id=id)
#         except Position.DoesNotExist as e:
#             return Response({"error": str(e)}, status.HTTP_404_NOT_FOUND)

#         position.delete()
#         return Response({"deleted": True})

