from django.contrib import admin

from amp.base_model_admin import MembershipBaseModelAdmin

from ..actions import create_order, reject_aliquot_label
from ..classes.aliquot_label import print_aliquot_label
from ..models import Aliquot


class AliquotAdmin(MembershipBaseModelAdmin):
    date_hierarchy = 'created'

    actions = [print_aliquot_label, create_order, reject_aliquot_label]

    list_display = ("aliquot_identifier", 'subject_identifier',
                    'to_receive', 'drawn', "aliquot_type",
                    'aliquot_condition', 'is_packed', 'is_rejected', 'created',
                    'user_created', 'hostname_created')

    search_fields = ('aliquot_identifier', 'receive__receive_identifier',
                     'receive__registered_subject__subject_identifier')

    list_filter = ('aliquot_type', 'aliquot_condition',
                   'created', 'user_created', 'hostname_created')

    list_per_page = 15

admin.site.register(Aliquot, AliquotAdmin)
