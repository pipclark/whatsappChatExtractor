from unittest import TestCase
import pandas as pd
from model import WhatsappMessageLoader, WhatsappMessages

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

        self.expected_key_result = pd.DataFrame(
            {'Date': ['19/07/2022', '29/07/2022'],
             'Time': ['6:31 pm', '6:38 pm'],
             'Name': ['Blob', 'Alice'],
             'Message': ["Ooops. Anyway here's a song\n\nhttps://open.spotify.com/track/1tCsI24edBbWnvU7UMeHDZ?si=cedb4ec09f354204\n\nDo you still want to see me today?",
                         "https://open.spotify.com/track/6ylAVPbjRQoNY0khgh63Jf?si=0114f8f44bab4e04\nNo but here's an appropriate song for you."
                         ]
             })

        self.expected_stats = pd.DataFrame(
            {'Name': ['Blob', 'Alice'],
             'Frequency': [1, 1]}
        )

    def test_load_whatsapp_text_file_success(self):
        whatsappMessages = WhatsappMessageLoader('test_data/WhatsApp Chat.txt')

        test_messages_df = whatsappMessages.load_whatsapp_text_file()
        pd.testing.assert_frame_equal(test_messages_df, self.expected_result)

    def test_load_whatsapp_text_file_fail(self):
        whatsappMessages = WhatsappMessageLoader('test_data/None existent file.txt')

        # expect loading messages to fail
        with self.assertRaises(FileNotFoundError):
            whatsappMessages.load_whatsapp_text_file()

    def test_extract_messages_with_key(self):
        key = 'https://open.spotify.com'
        whatsappMessageLoader = WhatsappMessageLoader('test_data/Music Chat.txt')

        whatsappMessages = WhatsappMessages(whatsappMessageLoader.load_whatsapp_text_file(), key, '')
        key_messages = whatsappMessages.extract_key_messages()

        pd.testing.assert_frame_equal(key_messages, self.expected_key_result)

    def test_extract_messages_with_two_keys(self):
        key = 'https://open.spotify.com'
        key_2 = 'Anyway'
        whatsappMessageLoader = WhatsappMessageLoader('test_data/Music Chat.txt')

        whatsappMessages = WhatsappMessages(whatsappMessageLoader.load_whatsapp_text_file(), key, key_2)
        key_messages = whatsappMessages.extract_two_key_messages()
        pd.testing.assert_frame_equal(key_messages, self.expected_key_result[self.expected_key_result['Message']
                                      .str.contains('Anyway')])


    def test_create_statistics_who_sent_key_messages(self):
        key = 'https://open.spotify.com'
        whatsappMessageLoader = WhatsappMessageLoader('test_data/Music Chat.txt')
        whatsappMessages = WhatsappMessages(whatsappMessageLoader.load_whatsapp_text_file(), key, '')

        stats = whatsappMessages.create_statistics_on_who_sent_key_messages()
        print(stats)
        pd.testing.assert_frame_equal(stats, self.expected_stats)



