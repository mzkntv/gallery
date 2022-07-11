from rest_framework import viewsets

from . import serializers, permissions
from .models import Picture


class PictureViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.PictureSerializer
    queryset = Picture.objects.all()
    permission_classes = (permissions.PictureAccessPermission,)

    def perform_create(self, serializer: serializers.PictureSerializer) -> None:
        serializer.save(owner=self.request.user)
