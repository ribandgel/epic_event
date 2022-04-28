from django.utils import timezone


class DateUpdatedMixin:
    def create(self, validated_data):
        validated_data["date_updated"] = timezone.now()
        return super().create(validated_data)

    def update(self, instance, validated_data):
        validated_data["date_updated"] = timezone.now()
        return super().update(instance, validated_data)
