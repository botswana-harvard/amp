import csv
import os

from django.apps import apps as django_apps
from django.core.management.base import BaseCommand, CommandError
from django.db.utils import IntegrityError


class Command(BaseCommand):
    help = 'Import CSV'

    def add_arguments(self, parser):
        parser.add_argument('csv_filename', type=str, help='Path to CSV file')
        parser.add_argument('model', type=str, help='App_label.model')

    def handle(self, *args, **options):
        csv_filename = options['csv_filename']
        try:
            app_label, model_name = options['model'].split('.')
        except LookupError:
            raise CommandError('Expected app_label.model, instead got {}'.format(options['model']))
        if not os.path.exists(csv_filename):
            raise CommandError('Csv file does not exist. Got {}'.format(csv_filename))
        else:
            added = 0
            model = django_apps.get_model(app_label, model_name)
            with open(csv_filename) as csvfile:
                subject_identifiers_dict = csv.DictReader(csvfile)
                for subject_identifier in subject_identifiers_dict:
                    try:
                        model.objects.create(subject_identifier=subject_identifier['subject_identifier'])
                        added += 1
                        self.stdout.write(
                            self.style.NOTICE('Adding record: {}'.format(added)) + '\n')

                    except IntegrityError:
                        self.stdout.write(
                            self.style.WARNING('Subject Identifier {} already exists'.format(subject_identifier['subject_identifier'])) + '\n')
            self.stdout.write(
                self.style.SUCCESS('\n' + 'Successfully added {}'.format(added)))
