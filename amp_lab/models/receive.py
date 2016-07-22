from django.core.urlresolvers import reverse
from django.db import models

from edc_base.model.models import BaseUuidModel
from edc_registration.models import RegisteredSubject

from lis.specimen.lab_receive.models import BaseReceive


class Receive(BaseReceive, BaseUuidModel):

    registered_subject = models.ForeignKey(RegisteredSubject, null=True, related_name='microbiome_receive')

    requisition_model_name = models.CharField(max_length=25, null=True, editable=False)

    subject_type = models.CharField(max_length=25, null=True, editable=False)

#     def save(self, *args, **kwargs): kell
#         self.subject_type = self.registered_subject.subject_type
#         super(Receive, self).save(*args, **kwargs)

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
