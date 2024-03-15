import json

data_path = 'data_raw/ChatExport_2024-03-11'


def parse_json(filepath):
    with open(f'{filepath}', 'r') as read_file:
        chat_data: dict = json.load(read_file)

    message_data: list = chat_data.get('messages')

    for msg in message_data:
        date, time = msg.get('date').split('T')
        user = msg.get('from')
        text = msg.get('text_entities')[0].get('text')
        with open('data_converted/output.txt', 'a') as out_file:
            out_file.write(f'{date}, {time} - {user}: {text}\n')


if __name__ == "__main__":
    parse_json()
