from django.core.management import BaseCommand

class Command(BaseCommand):
    help = "Imports channels's categories"

    def add_arguments(self, parser):
        parser.add_argument('import_arguments',nargs='*')

    def handle(self, *args, **options):
        import_arguments = options['import_arguments']

        channel_name = import_arguments[0]
        file_name = import_arguments[1]

        #self.stdout.write("Import the channel " + channel_name + " and .csv file " + file_name)
