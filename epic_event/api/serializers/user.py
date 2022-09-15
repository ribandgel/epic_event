from django.utils import timezone
from rest_framework import serializers

from epic_event.api.models import Contract, Event, User


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


class ContractSerializer(serializers.ModelSerializer):
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

    def create(self, validated_data):
        validated_data["date_updated"] = timezone.now()
        contract = super().create(validated_data)
        if validated_data["status"]:
            Event.objects.create(contract=contract, client=contract.client)
        return contract

    def update(self, instance, validated_data):
        validated_data["date_updated"] = timezone.now()
        contract = super().update(instance, validated_data)
        if validated_data["status"] and not contract.status:
            Event.objects.create(contract=contract, client=contract.client)
        return contract


class EventSerializer(serializers.ModelSerializer):
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

    def create(self, validated_data):
        contract = validated_data["contract"]
        if not contract.status:
            raise serializers.ValidationError(
                f"Contract {contract.id} is not signed yet, creation of event is not permited"
            )
        validated_data["date_updated"] = timezone.now()
        return super().create(validated_data)

    def update(self, instance, validated_data):
        validated_data["date_updated"] = timezone.now()
        return super().update(instance, validated_data)
