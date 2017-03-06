from django.test import TestCase
from workatolist.importfile import read_file, file_import
from workatolist.models import Category, Channel

class ImportFileTestCase(TestCase):
    def test_read_file(self):
        array_file = []
        directory = "workatolist/tests/"
        file_txt = read_file(directory,"test_file.txt")

        array_test = ['AB CD  \n','1234\n']

        for index, line in enumerate(file_txt):
            array_file.append(line)

        self.assertSequenceEqual(array_test,array_file)

    def test_file_import(self):
        file_import("wallmart","categories.csv")
        channel = Channel.objects.get(name = 'wallmart')
        self.assertEqual(channel.name, 'wallmart')

        categories_count = Category.objects.filter(channel = channel.id).count()
        self.assertEqual(categories_count, 23)

        category_parent = Category.objects.get(name = 'Books', parent_id = None)
        category_parent = Category.objects.get(name = 'National Literature',parent_id = category_parent.id)
        category = Category.objects.get(name = 'Fiction Fantastic',parent_id = category_parent.id)
        self.assertEqual(category.name, 'Fiction Fantastic')
