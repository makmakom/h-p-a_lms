from django.core.management.base import BaseCommand

from students.models import Student


class Command(BaseCommand):
    help = "Generate random students."

    def add_arguments(self, parser):
        parser.add_argument('count', nargs='+')

    def handle(self, *args, **options):
        print(options['count'])

        # if options['count']:
        #     Student.generate_students(int(options['count']))
        #     print('Ok')

        # raise NotImplementedError()
