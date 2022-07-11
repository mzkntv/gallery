from django.views import View
from rest_framework import permissions
from rest_framework.request import Request

from .models import Picture


class PictureAccessPermission(permissions.IsAuthenticated):
    def has_object_permission(self, request: Request, view: View, obj: Picture) -> bool:
        user = request.user

        if user.is_staff or obj.owner == user:
            return True

        return False
