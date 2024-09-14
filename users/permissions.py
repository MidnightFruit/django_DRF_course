from rest_framework.permissions import BasePermission


class IsModerator(BasePermission):
    def has_permission(self, request, view):
        return request.user.groups.filter(name='moderate').exists()


class IsOwner(BasePermission):
    def has_permission(self, request, view, obj):
        return request.user == obj.user