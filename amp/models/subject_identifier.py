from django.db import models
from django.utils import timezone
from edc_base.model_mixins.base_uuid_model import BaseUuidModel


class AlreadyAllocatedError(Exception):
    pass


class SubjectIdentifier(BaseUuidModel):

    subject_identifier = models.CharField(
        max_length=15,
        unique=True
    )

    allocated_datetime = models.DateTimeField(
        null=True,
        blank=True
    )

    def save(self, *args, **kwargs):
        if self.id and self.allocated_datetime:
            raise AlreadyAllocatedError('Identifier already allocated on {}. Got {}.'.format(
                self.allocated_datetime, self.subject_identifier))
        elif self.id:
            self.allocated_datetime = timezone.now()
        super(SubjectIdentifier, self).save(*args, **kwargs)

    def __str__(self):
        return self.subject_identifier

    class Meta:
        app_label = 'amp'
        ordering = ('subject_identifier', )
