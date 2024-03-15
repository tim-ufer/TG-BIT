from telethon import TelegramClient, types
from telethon.tl.functions.messages import CheckHistoryImportRequest, CheckHistoryImportPeerRequest, InitHistoryImportRequest, StartHistoryImportRequest
from dotenv import load_dotenv
import os
from parser import parse_json


async def main():
    # ask user for filepath
    # input_path = input('Enter the relative or full path to your export file:')
    # parse_json(input_path)
    output_path = 'data_converted/output.txt'
    with open(output_path, 'r') as out_file:
        head_lines = [next(out_file) for _ in range(50)]
    head = ''.join(head_lines)

    dialogs = await client.get_dialogs()
    target_id = 0
    for dia in dialogs:
        if dia.name == 'Test import':
            target_id = dia.entity.id
            break
    print(target_id)

    file_check = await client(CheckHistoryImportRequest(import_head=head))
    print(file_check.stringify(), '\n---------\n')
    # add error handling for incorrect id
    peer_check = await client(CheckHistoryImportPeerRequest(peer=target_id))
    print(peer_check.stringify())
    # print(result2.confirm_text)
    import_file = await client.upload_file(output_path)

    import_id = await client(InitHistoryImportRequest(peer=target_id, file=import_file, media_count=0))
    import_success = await client(StartHistoryImportRequest(peer=target_id, import_id=import_id))
    print('\n-------------------------------')
    if import_success:
        print('The import was successful, check your target chat for the imported messages!')
    else:
        input_on_fail = input('The import failed, do you want to start over? [N/y]')
        if input_on_fail.lower() == 'y':
            main()


if __name__ == "__main__":
    load_dotenv()
    api_id = os.getenv('api_id')
    api_hash = os.getenv('api_hash')
    with TelegramClient('anon', api_id, api_hash) as client:
        client.loop.run_until_complete(main())
