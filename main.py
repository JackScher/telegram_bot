import sys
from typing import Union
from telethon import TelegramClient


api_id = 'your_api_id'
api_hash = 'your_api_hash'

client = TelegramClient('sender', api_id, api_hash)


async def main(message: str, chat_id: Union[None, int]):
   me = await client.get_me()

   if chat_id is None:
      dialogs = client.iter_dialogs()
      async for dialog in dialogs:
         print(dialog.name, ' --- has ID ---', dialog.id)

      chat_id = input('Choose chat id: ')

   participants = await client.get_participants(int(chat_id))
   for participant in participants:
      if me.id != participant.id:
         await client.send_message(participant.id, message)


if __name__ == '__main__':
   if (len(sys.argv)) == 3:
      message = sys.argv[-2]
      chat_id = sys.argv[-1]
   elif (len(sys.argv)) == 2:
      message = sys.argv[-1]
      chat_id = None
   else:
      print('Wrong atr count')
      sys.exit()

   with client:
      client.loop.run_until_complete(main(message, chat_id))
