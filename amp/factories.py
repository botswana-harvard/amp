import factory

from amp.models import ScreeningConsent
from datetime import datetime
from amp.models.enrollment import Enrollment


class ScreeningConsentFactory(factory.DjangoModelFactory):

    class Meta:
        model = ScreeningConsent

    consent_datetime = datetime.today()

    identity = factory.Sequence(lambda n: '31791851{}'.format(n))

    identity_type = 'omang'

    is_literate = 'Yes'

    confirm_identity = identity

    first_name = factory.Sequence(lambda n: 'TEST{}'.format(n))

    last_name = factory.Sequence(lambda n: 'TEST{}'.format(n))


class EnrollmentFactory(factory.DjangoModelFactory):
    class Meta:
        model = Enrollment
