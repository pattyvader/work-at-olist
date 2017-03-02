from workatolist.models import Channel

def count_channel(name_channel):
    number_channel = Channel.objects.filter(name = name_channel).count()

    return number_channel

def get_channel(channel_name):
    channel = Channel.objects.get(name = channel_name)

    return channel
