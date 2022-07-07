from rest_framework import viewsets

from . import serializers
from .models import Picture


class PictureViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.PictureSerializer
    queryset = Picture.objects.all()

    def get_queryset(self):
        return Picture.objects.filter(owner=self.request.user)
