import factory

from amp.models import ScreeningConsent
from datetime import timezone


class ScreeningConsentFactory(factory.DjangoModelFactory):

    class Meta:
        model = ScreeningConsent

    consent_datetime = timezone.datetime.now()

    identity = factory.Sequences(lambda n: '31791851{}'.format(n))

    identity_type = 'omang'

    confirm_identity = identity

    first_name = factory.Sequences(lambda n: 'TEST{}'.format(n))

    last_name = factory.Sequences(lambda n: 'TEST{}'.format(n))
