from django.core.management.base import BaseCommand, CommandError

from students.models import Student


class Command(BaseCommand):
    help = "Generate random students."

    def add_arguments(self, parser):
        parser.add_argument('count', nargs='+', type=int)

    def handle(self, *args, **options):
        for count in options['count']:
            try:
                Student.generate_students(count)
            except Exception:
                raise CommandError('Cannot create students')
            self.stdout.write(self.style.SUCCESS(f'{count} students were successfully created'))
