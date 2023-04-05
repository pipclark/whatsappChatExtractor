from model import WhatsappMessageLoader, WhatsappMessages

class Controller:
    # TODO take filepath as user input
    def __init__(self, data_filepath: str, extraction_key, second_extraction_key=None):
        self.whatsappMessages = WhatsappMessageLoader(data_filepath)
        self.data_filepath = data_filepath
        self.extraction_key = extraction_key

        # optional arguments
        self.second_extraction_key = second_extraction_key if second_extraction_key is not None else extraction_key

    def load_chat_sample(self):
        try:
            messages_df = self.whatsappMessages.load_whatsapp_text_file()
        except FileNotFoundError:
            print(f'No file found at {self.data_filepath}')
            return 'No file found'  # TODO more suitable error

        return messages_df

    def get_sample_messages_with_extraction_key(self):
        all_messages = self.load_chat_sample()
        whatsappMessages = WhatsappMessages(all_messages, self.extraction_key)

        print(whatsappMessages.extract_key_messages())

    def get_key_message_stats(self):
        all_messages = self.load_chat_sample()
        whatsappMessages = WhatsappMessages(all_messages, self.extraction_key)
        print(whatsappMessages.create_statistics_on_who_sent_key_messages())

