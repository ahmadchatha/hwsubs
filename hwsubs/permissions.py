from rest_framework import permissions


class IsOwnerOrIsStaff(permissions.BasePermission):
    """
    Custom permission to only allow owners of an object to edit it or staff members.
    """

    def has_object_permission(self, request, view, obj):
        # Permissions are allowed for staff members
        if request.user.is_staff:
            return True

        # Otherwise permissions are only allowed to the owner of the snippet.
        return obj.creator == request.user

class StudentReadOnly(permissions.BasePermission):
    """
        Custom permission to only allow students read and staff members van do anything.
    """
    def has_permission(self, request, view):
        # Permissions are allowed for staff members
        if request.user.is_staff:
            return True

        # Only allow READ methods for students
        if request.method in permissions.SAFE_METHODS:
            return True

        return False

