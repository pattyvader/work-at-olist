from django.test import TestCase
from workatolist.models import Channel

class ChannelTestCase(TestCase):
    def setUp(self):
        Channel.objects.create(name="wallmart")

    def test_count_channel(self):
        channel_count = Channel.objects.filter(name = 'wallmart').count()

        self.assertEqual(channel_count, 1)

    def test_get_channel(self):
        channel = Channel.objects.get(name = 'wallmart')

        self.assertEqual(channel.name, 'wallmart')
