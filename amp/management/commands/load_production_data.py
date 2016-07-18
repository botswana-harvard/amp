import csv
import os

from amp.models import SubjectIdentifier
from dateutil import parser
from django.apps import apps as django_apps
from django.core.management.base import BaseCommand, CommandError
from django.db.utils import IntegrityError
from edc_constants.constants import NOT_APPLICABLE


class Command(BaseCommand):

    """Import model data from CSV.

    For example:
        python manage.py load_production_data bcpp_interview.rawdata /Users/erikvw/Documents/bcpp/qualitative_substudy/qualitative_substudy_subject_list10may2016_with_plots.csv

        python manage.py load_production_data bcpp_interview.rawdata /home/django/qualitative_substudy_subject_list10may2016_with_plots.csv
    """

    help = 'Load CSV data into a model'

    def add_arguments(self, parser):
        parser.add_argument('model', type=str, help='A model\'s app_label.model_name')
        parser.add_argument('csv_filename', type=str, help='Full path to CSV file')

    def handle(self, *args, **options):
        csv_filename = options['csv_filename']
        if not os.path.exists(csv_filename):
            raise CommandError('Csv file does not exist. Got {}'.format(csv_filename))
        try:
            app_label, model_name = options['model'].split('.')
        except ValueError:
            raise CommandError('Expected app_label.modelname got \'{}\''.format(options['model']))
        model = django_apps.get_model(app_label, model_name)
        self.stdout.write(
            self.style.NOTICE('Data source: csv \'{}\''.format(csv_filename.split('/')[-1:][0])))
        self.stdout.write(
            self.style.NOTICE('Target model: \'{}\''.format(model._meta.verbose_name)))
        added = 0
        with open(csv_filename, 'r', newline='') as csvfile:
            reader = csv.reader(csvfile)
            data = list(reader)
            csv_row_count = len(data)
        with open(csv_filename, 'r', newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            header = None
            for recs, row in enumerate(reader):
                if not header:
                    header = row
                else:
                    try:
                        obj = model.objects.create(**row)
                        added += 1
                        self.stdout.write(
                            self.style.NOTICE('  adding record {} / {} / {}{}'.format(added, recs, csv_row_count, ' ' * 35)), ending='\r')
                    except IntegrityError:
                        obj = model.objects.get(subject_identifier=row.get('subject_identifier'))
                        self.stdout.write(
                            self.style.NOTICE('  processing existing record {} / {} / {}{}'.format(added, recs, csv_row_count, ' ' * 35)), ending='\r')
                    self.create_handler(obj, row)
        self.stdout.write(
            self.style.SUCCESS('Successfully added {} / {} / {} records{}'.format(added, recs, csv_row_count, ' ' * 35)))

    def create_handler(self, obj, row):
        try:
            SubjectIdentifier.objects.create(
                subject_identifier=obj.subject_identifier)
        except IntegrityError as e:
            self.stdout.write(
                self.style.WARNING('IntegrityError: {}. Got {}.'.format(
                    obj.subject_identifier, str(e))))
