from rest_framework.permissions import BasePermission


class OwnerPermission(BasePermission):
    """Право доступа пользователя, который является владельцем (создателем) сущности"""
    def has_object_permission(self, request, view, obj):
        return obj.owner == request.user
