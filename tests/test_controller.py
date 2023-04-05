from unittest import TestCase
from controller import Controller


class TestModel(TestCase):

    def test_print_chat_sample_fail(self):
        controller = Controller('test_data/None existent file.txt', 'blob')

        # expect loading messages to fail
        self.assertEquals(controller.load_chat_sample(), 'No file found')
