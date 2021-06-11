from django.core.management.base import BaseCommand

from students.models import Student


class Command(BaseCommand):
    help = "Generate random students."

    def add_arguments(self, parser):
        parser.add_argument('count', nargs='+', type=int)

    def handle(self, *args, **options):
        print(options['count'])
        for count in options['count']:
            Student.generate_students(count)
            self.stdout.write(self.style.SUCCESS(f'{count} students were successfully created'))
