from django.core.management import BaseCommand

class Command(BaseCommand):
    help = "Imports channels's categories"

    def handle(self, *args, **options):
        self.stdout.write("Import categories!")
