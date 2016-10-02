from django.db.models.signals import post_save
from django.dispatch import receiver
from amp.models.screening_consent import ScreeningConsent
from amp.models.subject_identifier import SubjectIdentifier
from datetime import datetime


@receiver(post_save, sender=ScreeningConsent, dispatch_uid="screeningconsent_on_post_save")
def screeningconsent_on_post_save(sender, instance, raw, **kwargs):
    SubjectIdentifier.objects.filter(
        subject_identifier=instance.subject_identifier).update(allocated_datetime=datetime.today())

    if not raw:
        if isinstance(instance, (ScreeningConsent, )):
            instance.registration_update_or_create()
            instance.create_enrollment()
