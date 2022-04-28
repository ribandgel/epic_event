from django.contrib.auth.models import AbstractUser
from django.db import models

from .constants import ROLE


class User(AbstractUser):
    phone = models.CharField(max_length=20)
    mobile = models.CharField(max_length=20)
    compagny_name = models.CharField(max_length=250)
    date_updated = models.DateTimeField(auto_now_add=True)
    sales_contact = models.ForeignKey(
        "User", related_name="client_contacts", on_delete=models.SET_NULL, null=True
    )
    role = models.CharField(choices=ROLE, max_length=50)

    class Meta:
        app_label = "api"


class Contract(models.Model):
    sales_contact = models.ForeignKey(
        "User", related_name="agent_contracts", on_delete=models.DO_NOTHING
    )
    client = models.ForeignKey("User", related_name="client_contracts", on_delete=models.DO_NOTHING)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now_add=True)
    status = models.BooleanField(default=True)
    amount = models.DecimalField(decimal_places=2, max_digits=8, null=True)
    payement_due = models.DateTimeField()


class Event(models.Model):
    client = models.ForeignKey("User", related_name="events", on_delete=models.DO_NOTHING)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now_add=True)
    contract = models.ForeignKey("Contract", related_name="events", on_delete=models.DO_NOTHING)
    status = models.BooleanField(default=True)
    attendees = models.PositiveIntegerField(default=0)
    date = models.DateTimeField()
    notes = models.TextField(blank=True, default="")
