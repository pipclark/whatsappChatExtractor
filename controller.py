from model import WhatsappMessages

class Controller:
    # TODO take filepath as user input
    def __init__(self, data_filepath: str):
        self.whatsappMessages = WhatsappMessages(data_filepath)
        self.data_filepath = data_filepath

    def print_chat_sample(self):
        try:
            messages_df = self.whatsappMessages.load_whatsapp_text_file()
        except FileNotFoundError:
            print(f'No file found at {self.data_filepath}')
            return 'No file found'  # TODO more suitable error

        print(messages_df)
        return


