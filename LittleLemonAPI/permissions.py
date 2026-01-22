from rest_framework import permissions


class IsManager(permissions.BasePermission):
    def has_permission(self, request, view):
        # Use the `groups` related manager on User (plural) and return a boolean
        try:
            return request.user.groups.filter(name__iexact="Managers").exists()
        except Exception:
            return False


class IsDeliveryCrew(permissions.BasePermission):
    def has_permission(self, request, view):
        try:
            return request.user.groups.filter(name__iexact="Delivery crew").exists()
        except Exception:
            return False
