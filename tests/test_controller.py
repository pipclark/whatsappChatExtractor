from unittest import TestCase
from controller import DataLoader
import pandas as pd

class TestDataLoader(TestCase):

    def setUp(self) -> None:
        self.expected_result = pd.DataFrame(
            {'Date': ['19/07/2022', '19/07/2022', '19/07/2022', '19/07/2022', '29/07/2022'],
             'Time': ['6:31 pm', '6:31 pm', '6:33 pm', '6:33 pm', '6:33 pm'],
             'Name': ['', 'Alice', 'Blob', 'Alice', 'Blob'],
             'Message': ['', 'Where are you?',
                         "I thought we were meeting tomorrow.\n\nDo you still want to see me today?", 'Yes please.',
                         'Sorry I forgot to reply :)']
             })
    def test_load_whatsapp_text_file_success(self):
        dataLoader = DataLoader('test_data/WhatsApp Chat.txt')

        test_messages_df = dataLoader.load_whatsapp_text_file()
        pd.testing.assert_frame_equal(test_messages_df, self.expected_result)

    def test_load_whatsapp_text_file_fail(self):
        dataLoader = DataLoader('test_data/None existent file.txt')

        # expect loading messages to fail
        self.assertFalse(dataLoader.load_whatsapp_text_file())



