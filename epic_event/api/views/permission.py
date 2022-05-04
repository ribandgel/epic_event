from rest_framework.permissions import SAFE_METHODS, BasePermission


class UserPermission(BasePermission):
    def has_permission(self, request, view):
        if request.user:
            if request.method in SAFE_METHODS and request.role != "Client":
                return True
            elif request.user.role == "Gestion":
                return True
            elif request.user.role == "Vente" and view.action in ["partial_update", "update"]:
                return True
        return False


class ContractPermission(BasePermission):
    def has_permission(self, request, view):
        if request.user:
            if request.method in SAFE_METHODS and request.role != "Client":
                return True
            elif request.user.role == "Gestion":
                return True
            if request.user.role == "Vente" and view.action in [
                "create",
                "update",
                "partial_update",
            ]:
                return True
        return False


class EventPermission(BasePermission):
    def has_permission(self, request, view):
        if request.user:
            if request.method in SAFE_METHODS and request.role != "Client":
                return True
            elif request.user.role == "Gestion":
                return True
            elif (
                request.user.role == "Vente" or request.user.role == "Support"
            ) and view.action in ["create", "update", "partial_update"]:
                return True
        return False
