import uuid
from django.db import models


class TimestampedModel(models.Model):
    """
    Abstract model that adds 'created_at' and 'updated_at' fields.
    Useful for any resource that needs history tracking.
    """
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Дата создания"
    )
    updated_at = models.DateTimeField(
        auto_now=True,
        verbose_name="Дата обновления"
    )

    class Meta:
        abstract = True


class UUIDModel(models.Model):
    """
    Abstract model that uses UUID as primary key instead of standard ID.
    Preferred for public-facing URLs and API safety.
    """
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False
    )

    class Meta:
        abstract = True


class BaseModel(TimestampedModel, UUIDModel):
    """
    Universal Base Model for all project entities.
    Combines UUID and Timestamp logic.
    """
    class Meta:
        abstract = True
