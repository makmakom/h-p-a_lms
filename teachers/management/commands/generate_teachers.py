from django.core.management.base import BaseCommand, CommandError

from teachers.models import Teacher


class Command(BaseCommand):
    help = "Generate random teachers."

    def add_arguments(self, parser):
        parser.add_argument('count', nargs='?', default=10, type=int)

    def handle(self, *args, **options):
        count = options['count']
        try:
            Teacher.generate(count)
        except Exception:
            raise CommandError('Cannot create teachers')
        self.stdout.write(self.style.SUCCESS(f'{count} teachers were successfully created'))
