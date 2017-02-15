from django.core.management import BaseCommand
from myfunctions import file_import

class Command(BaseCommand):
    help = "Imports channels's categories"

    def add_arguments(self, parser):
        parser.add_argument('import_arguments',nargs='*')

    def handle(self, *args, **options):
        import_arguments = options['import_arguments']

        channel_name = import_arguments[0]
        file_name = import_arguments[1]

        file_import(channel_name,file_name)
