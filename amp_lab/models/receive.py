from django.core.urlresolvers import reverse
from django.db import models
from edc_lab.receive.model_mixins import ReceiveModelMixin
from edc_lab.receive.managers import ReceiveManager


class Receive(ReceiveModelMixin):

    objects = ReceiveManager()

    def __unicode__(self):
        return self.receive_identifier or u''

    def requisition(self):
        url = reverse('admin:amp_lab_subjectrequisition_changelist')
        return '<a href="{0}?q={1}">{1}</a>'.format(url, self.requisition_identifier)
    requisition.allow_tags = True

    def natural_key(self):
        return (self.receive_identifier, )

    class Meta:
        app_label = 'amp_lab'
