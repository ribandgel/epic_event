from django_filters import rest_framework as filters
from rest_framework.permissions import SAFE_METHODS, IsAuthenticated

from epic_event.api.models import Contract, Event, User
from epic_event.api.serializers import ContractSerializer, EventSerializer, UserSerializer

from .common import AtomicModelViewSet
from .permission import ContractPermission, EventPermission, UserPermission


class UserFilter(filters.FilterSet):
    search = filters.CharFilter(method="filter_search")

    def filter_search(self, queryset, name, value):
        return queryset.objects.filter(username__icontains=value)

    class Meta:
        model = User
        fields = [
            "username",
            "first_name",
            "last_name",
            "email",
            "phone",
            "mobile",
            "compagny_name",
            "date_updated",
            "role",
        ]


class UserViewSet(AtomicModelViewSet):
    filterset_class = UserFilter
    permission_classes = (
        IsAuthenticated,
        UserPermission,
    )
    serializer_class = UserSerializer

    def get_queryset(self):
        queryset = User.objects.none()
        if self.request and not self.request.user.is_anonymous:
            if self.request.user.role == "Gestion" or self.request.method in SAFE_METHODS:
                queryset = User.objects.all()
            elif self.request.user.role == "Vente":
                queryset = User.objects.filter(sales_contact=self.request.user)
        return queryset.order_by("-id")


class ContractFilter(filters.FilterSet):
    search = filters.CharFilter(method="filter_search")

    def filter_search(self, queryset, name, value):
        return queryset.objects.filter(client__first_name__icontains=value)

    class Meta:
        model = Contract
        fields = [
            "client",
            "date_created",
            "date_updated",
            "status",
            "amount",
            "payement_due",
        ]


class ContractViewSet(AtomicModelViewSet):
    filterset_class = ContractFilter
    permission_classes = (
        IsAuthenticated,
        ContractPermission,
    )
    serializer_class = ContractSerializer

    def get_queryset(self):
        queryset = Contract.objects.none()
        if self.request and not self.request.user.is_anonymous:
            if self.request.user.role == "Gestion" or self.request.method in SAFE_METHODS:
                queryset = Contract.objects.all()
            elif self.request.user.role == "Vente":
                queryset = Contract.objects.filter(sales_contact=self.request.user)
        return queryset.order_by("-id")


class EventFilter(filters.FilterSet):
    search = filters.CharFilter(method="filter_search")

    def filter_search(self, queryset, name, value):
        return queryset.objects.filter(client__first_name__icontains=value)

    class Meta:
        model = Event
        fields = [
            "client",
            "date_created",
            "date_updated",
            "contract",
            "status",
            "attendees",
            "date",
            "notes",
        ]


class EventViewSet(AtomicModelViewSet):
    filterset_class = EventFilter
    permission_classes = (
        IsAuthenticated,
        EventPermission,
    )
    serializer_class = EventSerializer

    def get_queryset(self):
        queryset = Event.objects.none()
        if self.request and not self.request.user.is_anonymous:
            if self.request.user.role == "Gestion" or self.request.method in SAFE_METHODS:
                queryset = Event.objects.all()
            else:
                queryset = Event.objects.filter(contract__sales_contact=self.request.user)
        return queryset.order_by("-id")
