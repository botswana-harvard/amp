from django.db import models
from django.utils import timezone

from edc_base.model.models import BaseUuidModel

from .aliquot import Aliquot
from .order import Order
from .panel import Panel


class OrderItem(BaseUuidModel):

    order = models.ForeignKey(Order)

    aliquot = models.ForeignKey(Aliquot)

    panel = models.ForeignKey(
        Panel,
        null=True,
        blank=False,
    )

    order_identifier = models.CharField(
        max_length=25,
        null=True,
        help_text='',
    )

    order_datetime = models.DateTimeField(
        default=timezone.now
    )

    subject_identifier = models.CharField(
        max_length=50,
        null=True,
        help_text="non-user helper field to simplify search and filtering")

    def save(self, *args, **kwargs):
        self.subject_identifier = self.aliquot.receive.registered_subject.subject_identifier
        super(OrderItem, self).save(*args, **kwargs)

    def natural_key(self):
        return (self.order_identifier, )

    class Meta:
        app_label = 'amp_lab'
        ordering = ['-order_datetime', ]
