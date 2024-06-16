
from rest_framework.response import Response
from api.serializers import FormSerializer, PositionSerializer
from rest_framework import status, mixins, generics
from rest_framework.permissions import IsAuthenticated
from api.models import Ad, Casting, Position, Form



class PositionList(generics.ListCreateAPIView):
    queryset = Position.objects.all()
    serializer_class = PositionSerializer

    # permission_classes = (IsAuthenticated,)

    # def get_queryset(self):
    #     return Position.objects.all()

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
    

# class FormList(mixins.ListModelMixin,
#                 mixins.CreateModelMixin,
#                 generics.GenericAPIView):
#     queryset = Form.objects.all()
#     serializer_class = FormSerializer

#     permission_classes = (IsAuthenticated,)

#     def get(self, request):
#         return self.list(request)
    
#     def post(self, request):
#         return self.create(request)
    
#     # saving user 
#     def perform_create(self, serializer):
#         serializer.save(user=self.request.user)
    
class FormList(generics.ListCreateAPIView):
    queryset = Form.objects.all()
    serializer_class = FormSerializer
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        return self.list(request)
    
    def post(self, request):
        return self.create(request)
    
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    