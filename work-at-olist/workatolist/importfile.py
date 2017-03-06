import sys
import django.db
from workatolist.models import Channel,Category

def file_import(channel_name,file_name):
    try:
        channel = Channel()
        channel_number = channel.count_channel(channel_name)

        if channel_number == 0:
            channel_obj = Channel(name = channel_name)
            channel_obj.save()
        else:
            channel = channel.get_channel(channel_name)
            Category.objects.filter(channel = channel.id).delete()

        directory = "workatolist/"
        file_csv = read_file(directory, file_name)

        for line in file_csv:
            if not 'Category' in line:
                categories_lines = line.replace("\n","").split("/")
                channel = channel.get_channel(channel_name)
                parent_id = None

                for index, category_name in enumerate(categories_lines):
                    category_name = category_name.strip()
                    category = Category.objects.filter(parent_id = parent_id, name = category_name,
                                channel = channel.id).first()

                    if category == None:
                        category = Category.objects.create_category(name = category_name, parent_id = parent_id, channel = channel)
                        category.save()

                    parent_id = category.id
    except IOError as error:
        print("Error: {0}".format(error))
    except:
        print("Unexpected error:", sys.exc_info()[0])
        raise

def read_file(directory,name_file):
    try:
        file_csv = open(directory + name_file, "r")

        return file_csv
    except IOError as error_import:
        print("Error: {0}".format(error_import))
