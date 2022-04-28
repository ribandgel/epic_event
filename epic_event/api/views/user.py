from rest_framework.permissions import SAFE_METHODS, IsAuthenticated
from rest_framework.viewsets import GenericViewSet

from epic_event.api.models import Contract, Event, User
from epic_event.api.serializers import ContractSerializer, EventSerializer, UserSerializer

from .common import AtomicModelViewSet


class UserViewSet(GenericViewSet):
    permission_classes = (IsAuthenticated,)
    serializer_class = UserSerializer

    def get_queryset(self):
        if self.request and not self.request.user.is_anonymous:
            queryset = User.objects.get(id=self.request.user.id)
        else:
            queryset = User.objects.none()
        return queryset.order_by("-id")


class ContractViewSet(AtomicModelViewSet):
    permission_classes = (IsAuthenticated,)
    serializer_class = ContractSerializer

    def get_queryset(self):
        if self.request and not self.request.user.is_anonymous:
            if self.request.method in SAFE_METHODS:
                queryset = Contract.objects.all()
            else:
                queryset = Contract.objects.filter(sales_contact=self.request.user)
        else:
            queryset = Contract.objects.none()
        return queryset.order_by("-id")


class EventViewSet(AtomicModelViewSet):
    permission_classes = (IsAuthenticated,)
    serializer_class = EventSerializer

    def get_queryset(self):
        if self.request and not self.request.user.is_anonymous:
            if self.request.method in SAFE_METHODS:
                queryset = Event.objects.all()
            else:
                queryset = Event.objects.filter(contract__sales_contact=self.request.user)
        else:
            queryset = Event.objects.none()
        return queryset.order_by("-id")
