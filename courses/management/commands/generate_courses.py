from courses.models import Course

from django.core.management.base import BaseCommand, CommandError


class Command(BaseCommand):
    help = "Generate random courses."

    def add_arguments(self, parser):
        parser.add_argument('count', nargs='?', default=10, type=int)

    def handle(self, *args, **options):
        count = options['count']
        try:
            Course.generate_courses(count)
        except Exception:
            raise CommandError('Cannot create courses')
        self.stdout.write(self.style.SUCCESS(f'{count} courses were successfully created'))
