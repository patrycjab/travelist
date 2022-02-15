import csv
import os
from django.apps import apps
from django.core.management.base import BaseCommand
from account.models import CustomUser as User


class Command(BaseCommand):
    workbook_name = 'account/management/commands/users.csv'

    def add_arguments(self, parser):
        parser.add_argument('filename', type=str, help='filename for csv file')

    def get_current_app_path(self):
        return apps.get_app_config('account').path

    def get_csv_file(self, filename):
        app_path = self.get_current_app_path()
        file_path = os.path.join(app_path, "management",
                                 "commands", filename)
        return file_path

    def handle(self, *args, **kwargs):
        filename = kwargs['filename']
        file_path = self.get_csv_file(filename)
        with open(file_path, newline='') as csvfile:
            spamreader = csv.reader(csvfile,  quotechar='|')
            row1 = next(spamreader)
            data = list()
            for line, row in enumerate(spamreader):
                helper = {'username': ''}
                for a, b in zip(row1, row):
                    helper[a] = b
                data.append(User(**helper))
            User.objects.bulk_create(data)
        referrer_users = User.objects.filter(referrer_email__isnull=False).exclude(referrer_email__exact="")
        for x in referrer_users:
            obj = User.objects.get(email=x.referrer_email)
            obj.balance += 20
        User.objects.bulk_update(referrer_users, ['balance'])
