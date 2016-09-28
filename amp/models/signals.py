from django.db.models.signals import pre_save
from django.dispatch import receiver
from amp.models.screening_consent import ScreeningConsent
from amp.models.subject_identifier import SubjectIdentifier
from datetime import datetime


@receiver(pre_save, sender=ScreeningConsent, dispatch_uid="screeningconsent_on_post_save")
def screeningconsent_on_post_save(sender, instance, **kwargs):
    SubjectIdentifier.objects.filter(
        subject_identifier=instance.subject_identifier).update(allocated_datetime=datetime.today())
