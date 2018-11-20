from django.core.management.base import BaseCommand, CommandError
from tours.seeder import seed_data


class Command(BaseCommand):
    help = 'seed random data to database'

    def handle(self, *args, **kwargs):
        seed_data()
        self.stdout.write(self.style.SUCCESS('Successfully seeded the database'))
