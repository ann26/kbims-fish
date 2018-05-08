# coding=utf-8
"""Fish collection record model definition.

"""

from django.db import models

from fish.models.biological_collection_record import \
    BiologicalCollectionRecord


class FishCollectionRecord(BiologicalCollectionRecord):
    """First collection model."""
    HABITAT_CHOICES = (
        ('euryhaline', 'Euryhaline'),
        ('freshwater', 'Freshwater'),
    )

    habitat = models.CharField(
        max_length=50,
        choices=HABITAT_CHOICES,
        blank=True,
    )

    # noinspection PyClassicStyleClass
    class Meta:
        """Meta class for project."""
        app_label = 'fish'
        verbose_name = 'fish'
        verbose_name_plural = 'fishes'
