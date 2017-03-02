import sys
import django.db
from workatolist.channel import count_channel, get_channel
from workatolist.file import read_file
from workatolist.models import Channel,Category

def file_import(channel_name,file_name):
    try:
        channel_number = count_channel(channel_name)

        if channel_number == 0:
            channel_obj = Channel(name = channel_name)
            channel_obj.save()

        file_csv = read_file(file_name)

        for line in file_csv:
            if not 'Category' in line:
                categories_lines = line.replace("\n","").split("/")
                channel = get_channel(channel_name)
                parent_id = None

                for index, category_name in enumerate(categories_lines):
                    category_name = category_name.strip()
                    category = Category.objects.filter(parent_id = parent_id, name = category_name,
                                channel = channel.id).first()

                    if category == None:
                        category = Category(parent_id = parent_id, name = category_name, channel = channel)
                        category.save()

                   parent_id = category.id
    except IOError as error:
        print("Error: {0}".format(error))
    except:
        print("Unexpected error:", sys.exc_info()[0])
        raise
