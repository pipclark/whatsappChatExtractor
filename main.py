from controller import DataLoader

if __name__ == '__main__':
    dataLoader = DataLoader('tests/test_data/WhatsApp Chat.txt')

    messages_df = dataLoader.load_whatsapp_text_file()

    print(messages_df)



