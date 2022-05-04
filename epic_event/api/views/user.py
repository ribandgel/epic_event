from rest_framework.permissions import SAFE_METHODS
from rest_framework.viewsets import GenericViewSet

from epic_event.api.models import Contract, Event, User
from epic_event.api.serializers import ContractSerializer, EventSerializer, UserSerializer

from .common import AtomicModelViewSet
from .permission import ContractPermission, EventPermission, UserPermission


class UserViewSet(GenericViewSet):
    permission_classes = (UserPermission,)
    serializer_class = UserSerializer

    def get_queryset(self):
        queryset = User.objects.none()
        if self.request and not self.request.user.is_anonymous:
            if self.request.user.role == "Gestion" or self.request.method in SAFE_METHODS:
                queryset = User.objects.all()
            elif self.request.user.role == "Vente":
                queryset = User.objects.filter(sales_contact=self.request.user)
        return queryset.order_by("-id")


class ContractViewSet(AtomicModelViewSet):
    permission_classes = (ContractPermission,)
    serializer_class = ContractSerializer

    def get_queryset(self):
        queryset = Contract.objects.none()
        if self.request and not self.request.user.is_anonymous:
            if self.request.user.role == "Gestion" or self.request.method in SAFE_METHODS:
                queryset = Contract.objects.all()
            elif self.request.user.role == "Vente":
                queryset = Contract.objects.filter(sales_contact=self.request.user)
        return queryset.order_by("-id")


class EventViewSet(AtomicModelViewSet):
    permission_classes = (EventPermission,)
    serializer_class = EventSerializer

    def get_queryset(self):
        queryset = Event.objects.none()
        if self.request and not self.request.user.is_anonymous:
            if self.request.user.role == "Gestion" or self.request.method in SAFE_METHODS:
                queryset = Event.objects.all()
            else:
                queryset = Event.objects.filter(contract__sales_contact=self.request.user)
        return queryset.order_by("-id")
