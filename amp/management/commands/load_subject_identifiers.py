import csv
import os

from django.conf import settings
from django.core.management.base import BaseCommand, CommandError
from django.db.utils import IntegrityError

from ...models import SubjectIdentifier
from django.utils import timezone


class Command(BaseCommand):
    help = 'Import CSV'

    def handle(self, *args, **options):
        used_identifier = os.path.join(settings.MEDIA_PATH, 'usedids.csv')
        unused_identifier = os.path.join(settings.MEDIA_PATH, 'unusedids.csv')
        if not os.path.exists(used_identifier):
            raise CommandError('Csv file does not exist. Got {}'.format(used_identifier))
        if not os.path.exists(unused_identifier):
            raise CommandError('Csv file does not exist. Got {}'.format(unused_identifier))
        else:
            added = 0
            print("******************************* Adding unused subject identifier *******************************")
            with open(unused_identifier) as csvfile:
                subject_identifiers_dict = csv.DictReader(csvfile)
                for subject_identifier in subject_identifiers_dict:
                    try:
                        SubjectIdentifier.objects.create(subject_identifier=subject_identifier['subject_identifier'])
                        added += 1
                        self.stdout.write(
                            self.style.NOTICE('Adding record: {}'.format(added)) + '\n')

                    except IntegrityError:
                        self.stdout.write(
                            self.style.WARNING(
                                'Subject Identifier {} already exists'.format(
                                    subject_identifier['subject_identifier'])) + '\n')
            self.stdout.write(
                self.style.SUCCESS('\n' + 'Successfully added {}'.format(added)))
            added = 0
            print("******************************* Adding used subject identifier *******************************")
            with open(used_identifier) as csvfile:
                subject_identifiers_dict = csv.DictReader(csvfile)
                for subject_identifier in subject_identifiers_dict:
                    try:
                        SubjectIdentifier.objects.create(
                            subject_identifier=subject_identifier['subject_identifier'],
                            allocated_datetime=timezone.now())
                        added += 1
                        self.stdout.write(
                            self.style.NOTICE('Adding record: {}'.format(added)) + '\n')

                    except IntegrityError:
                        self.stdout.write(
                            self.style.WARNING(
                                'Subject Identifier {} already exists'.format(
                                    subject_identifier['subject_identifier'])) + '\n')
            self.stdout.write(
                self.style.SUCCESS('\n' + 'Successfully added {}'.format(added)))
