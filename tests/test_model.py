from unittest import TestCase
import pandas as pd
from model import WhatsappMessages

class TestWhatsappMessages(TestCase):
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
        whatsappMessages = WhatsappMessages('test_data/WhatsApp Chat.txt')

        test_messages_df = whatsappMessages.load_whatsapp_text_file()
        pd.testing.assert_frame_equal(test_messages_df, self.expected_result)

    def test_load_whatsapp_text_file_fail(self):
        whatsappMessages = WhatsappMessages('test_data/None existent file.txt')

        # expect loading messages to fail
        with self.assertRaises(FileNotFoundError):
            whatsappMessages.load_whatsapp_text_file()
