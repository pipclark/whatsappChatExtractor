from controller import Controller

if __name__ == '__main__':
    controller = Controller('tests/test_data/Music Chat.txt', 'https://open.spotify.com')
    controller.print_sample_messages_with_extraction_key()







