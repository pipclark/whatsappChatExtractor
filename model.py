import pandas as pd
import pandas as pd
import re


class WhatsappMessageLoader:
    def __init__(self, whatsapp_conversation_filepath):
        self.data = None
        self.whatsapp_conversation_filepath = whatsapp_conversation_filepath

    def load_whatsapp_text_file(self):
        # Define the regular expression pattern for the date format
        date_pattern = r'^(\d{2}\/\d{2}\/\d{4},\s\d{1,2}:\d{2}\s(?:am|pm))\s-\s(.+)$'

        # Initialize variables to store the data
        date, name, message = '', '', ''
        data = []

        # Open the file and replace bad characters
        with open(self.whatsapp_conversation_filepath, 'rb') as f:
            try:
                text = f.read().decode('utf-8')
            except UnicodeDecodeError as e:
                print(f"UnicodeDecodeError: {e}")
                text = e.object[:e.start].decode('utf-8', 'ignore') + '_' + e.object[e.end:].decode('utf-8',
                                                                                                    'ignore')
            for line in text.split('\n'):
                # Strip whitespace from the beginning and end of the line
                line = line.strip()

                # Check if the line starts with a date
                match = re.match(date_pattern, line)
                if match:
                    # If the line starts with a date, store the current data (if any) and start a new row
                    if date:
                        data.append([date, time, name, message])
                    date, time = match.group(1).split(', ')
                    try:
                        name, message = match.group(2).split(': ', 1)
                    except ValueError:
                        pass  # info message from whatsapp

                else:
                    # If the line doesn't start with a date, add it to the message for the current row
                    message += '\n' + line

            # Store the last row of data (if any)
            if date:
                data.append([date, time, name, message])

            # Convert the data to a DataFrame and set the column names
            df = pd.DataFrame(data, columns=['Date', 'Time', 'Name', 'Message'])
            return df


class WhatsappMessages:
    def __init__(self, messages_df, key: str, key_2: str = ''):
        self.key = key
        self.key_2 = key_2
        self.messages_df = messages_df

    def extract_key_messages(self):
        filtered_messages = self.messages_df[self.messages_df['Message'].str.contains(self.key)].reset_index(drop=True)
        return filtered_messages

    def extract_two_key_messages(self):
        filtered_messages = self.messages_df[self.messages_df['Message'].str.contains(self.key) &
                                             self.messages_df['Message'].str.contains(self.key_2)] \
            .reset_index(drop=True)
        return filtered_messages

    def create_statistics_on_who_sent_key_messages(self):
        messages = self.extract_key_messages()
        stats = messages['Name'].value_counts()
        stats_df = stats.to_frame().reset_index()
        stats_df.columns = ['Name', 'Frequency']
        print(stats)
        return stats_df
