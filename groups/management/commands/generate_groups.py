from django.core.management.base import BaseCommand, CommandError

from groups.models import Group


class Command(BaseCommand):
    help = "Generate random groups."

    def add_arguments(self, parser):
        parser.add_argument('count', nargs='?', default=10, type=int)

    def handle(self, *args, **options):
        count = options['count']
        try:
            Group.generate_groups(count)
        except Exception:
            raise CommandError('Cannot create groups')
        self.stdout.write(self.style.SUCCESS(f'{count} groups were successfully created'))
