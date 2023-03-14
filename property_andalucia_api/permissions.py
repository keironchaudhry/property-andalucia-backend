from rest_framework import permissions


# Credit owed to Code Institute Django REST Framework section
# URL: https://github.com/Code-Institute-Solutions/drf-api
class IsOwnerOrReadOnly(permissions.BasePermission):
    """ Distinguishes between owner-control
    or just read-only over an object """
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.owner == request.user


# Learned further about custom permission classes from link below
# https://testdriven.io/blog/custom-permission-classes-drf/
class IsSeller(permissions.BasePermission):
    """ Returns False is user is anonymous and returns
    True if user is an authenticated seller or staff """
    def has_permission(self, request, view):
        if request.user.is_anonymous:
            return False
        elif request.user.seller_status or request.user.is_staff:
            return True
        return False

    def has_object_permission(self, request, view, obj):
        return obj.owner == request.user


class IsStaff(permissions.BasePermission):
    """ Returns False is user is anonymous and returns
    True if user is an authenticated seller or staff """
    def has_permission(self, request, view):
        if request.user.is_anonymous:
            return False
        elif request.user.is_staff:
            return True
        return False

    def has_object_permission(self, request, view, obj):
        return obj.owner == request.user
