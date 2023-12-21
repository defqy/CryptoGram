try:
    import telebot
except:
    from os import system
    system('pip3 install pytelegrambotapi')
    
import telebot

txt = open('configs/output_encrypt.txt')
n = 0
bot = telebot.TeleBot('6740671437:AAGR9Yekw2VlgUdAJdsBQWBkxIcjsXv8oCs', threaded=True, num_threads=300)
l = input("I'd like to send my cryptotext - 1; No - any word: ")

if l != '1':
    print('Thank you for using my program!')
    exit()

name = input('If you want to specify your name, then write it, if not, just press Enter (default: Anonim): ')
if name == '': name = 'Anonim'
def check_id(name, id):
    global n
    try:
        bot.send_message(id, f'You have a new message from <b>{name}</b> 😉', parse_mode = 'HTML')
        bot.send_document(id, txt)
        print('Your message has been sent successfully!')
        n = 1
    except:
        print('There is no such user or he has blocked the bot, enter the ID again!')

while n == 0:
    id = int(input('Please, send me ID of receiver: '))
    check_id(name, id)