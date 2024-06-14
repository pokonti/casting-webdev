
from rest_framework.response import Response
from api.serializers import AdSerializer, PositionSerializer
from rest_framework import status, mixins, generics
from rest_framework.views import APIView
from api.models import Ad, Casting, Position



class PositionList(mixins.ListModelMixin,
                          mixins.CreateModelMixin,
                          generics.GenericAPIView):
    queryset = Position.objects.all()
    serializer_class = PositionSerializer

    def get(self, request):
        return self.list(request)
    
    def post(self, request):
        return self.create(request)
    

class Position(mixins.RetrieveModelMixin,
                mixins.UpdateModelMixin,
                mixins.DestroyModelMixin,
                generics.GenericAPIView):
    queryset = Position.objects.all()
    serializer_class = PositionSerializer

    def get(self, request, pk=None):
        return self.retrieve(request, pk)

    def put(self, request, pk=None):
        return self.update(request, pk)

    def delete(self, request, pk=None):
        return self.destroy(request, pk)