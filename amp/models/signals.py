from django.db.models.signals import post_save
from django.dispatch import receiver

from django.utils import timezone

from .screening_consent import ScreeningConsent
from .subject_identifier import SubjectIdentifier


@receiver(post_save, sender=ScreeningConsent, dispatch_uid="screeningconsent_on_post_save")
def screeningconsent_on_post_save(sender, instance, raw, **kwargs):
    SubjectIdentifier.objects.filter(
        subject_identifier=instance.subject_identifier).update(allocated_datetime=timezone.now())

    if not raw:
        if isinstance(instance, (ScreeningConsent, )):
            instance.create_enrollment()
