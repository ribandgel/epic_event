from rest_framework import serializers

from epic_event.api.models import Contract, Event, User

from .common import DateUpdatedMixin


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            "id",
            "username",
            "email",
            "first_name",
            "last_name",
            "phone",
            "mobile",
            "compagny_name",
            "date_updated",
            "sales_contact",
            "role",
        )
        read_only_fields = ("id",)


class ContractSerializer(DateUpdatedMixin, serializers.ModelSerializer):
    class Meta:
        model = Contract
        fields = (
            "sales_contact",
            "client",
            "date_created",
            "date_updated",
            "status",
            "amount",
            "payement_due",
        )
        read_only_fields = ("date_created", "date_updated")


class EventSerializer(DateUpdatedMixin, serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = (
            "client",
            "date_created",
            "date_updated",
            "contract",
            "status",
            "attendees",
            "date",
            "notes",
        )
        read_only_fields = (
            "date_created",
            "date_updated",
        )
