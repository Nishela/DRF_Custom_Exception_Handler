from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet

from .serializers import CustomSerializer


class CustomViewSet(GenericViewSet):
    serializer_class = CustomSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        return Response(serializer.data)
