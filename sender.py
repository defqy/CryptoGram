from datetime import datetime
from open_file import open_decrypt
import telebot
import open_file

n = 0
open_decrypt('output_encrypt.txt')
bot = telebot.TeleBot('66740671437:AAGR9Yekw2VlgUdAJdsBQWBkxIcjsXv8oCs')
name = input('If you want to specify your name, then write it, if not, just press Enter (default: Anonim): ')

while n == 0:
    id = int(input('Please, send me ID of receiver: '))
    if name == '': name = 'Anonim'

    def check_id(name, id):
        global n
        try:
            current_datetime = datetime.now()
            bot.send_message(id, f'You have a new message from <b>{name}</b> 😉\n\nSending time: {current_datetime}\n\nMessage - <code>{open_file.ot}</code>', parse_mode = 'HTML')
            print('Your message has been sent successfully!')
            n = 1
        except:
            print('There is no such user or he has blocked the bot, enter the ID again!')

    check_id(name, id)