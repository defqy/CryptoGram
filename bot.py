from telebot import types
from datetime import datetime
import telebot

print('Bot is working now!')

bot = telebot.TeleBot('6571108770:AAEQwras-bZI_N49i6V4bRfOjHvZLvfJxQs', threaded=True, num_threads=300)
sender = telebot.TeleBot('6740671437:AAGR9Yekw2VlgUdAJdsBQWBkxIcjsXv8oCs', threaded=True, num_threads=300)

id = ''
init_vector = ''

@bot.message_handler(commands=['start'])
def hello(message):
    global id
    keyboard = types.ReplyKeyboardMarkup(row_width = 1, resize_keyboard = True)
    crypted_message = types.KeyboardButton(text = 'Отправить зашифрованное сообщение')
    ID_user = types.KeyboardButton(text = "Узнать свой ID")
    help = types.KeyboardButton(text = "🛟Помощь")
    escape = types.KeyboardButton(text = "⬇Скрыть")

    keyboard.row(crypted_message)
    keyboard.row(ID_user, help)
    keyboard.row(escape)
    bot.send_message(message.chat.id, "Привет, <b>{0.first_name}</b>\nДобро пожаловать в CryptoGram. Данный бот поможет Вашим сообщениям, которые проходят через Telegram оставаться зашифрованными. Переписка осуществляется в @defqy_cryptogram_chat_bot. Запустите его, чтобы получать сообщения".format(message.from_user, bot.get_me()), reply_markup = keyboard, parse_mode='HTML')
    bot.send_message(message.chat.id, 'Перед началом работы, убедитесь в том, что у вашего собеседника хоть раз был запущен данный бот (если нет, то перешлите ему ссылку на бота) или уберите его из заблокированных, чтобы собеседник получал сообщения')
    keyboard.add(crypted_message, ID_user, escape)

def send_id(message):
    global ID_send
    ID_send = message.chat.id
    bot.send_message(message.forward_from.id, f'Name: <strong>{message.from_user.username}\nID: {ID_send}</strong> sent you his ID\nID: {ID_send}', parse_mode = 'HTML')

@bot.message_handler(content_types = ['text'])
def start(message):
    if message.text == 'Узнать свой ID':
        bot.send_message(message.chat.id, f'Name - @{message.from_user.username}\nID - <code>{message.from_user.id}</code>\nFirst name - {message.from_user.first_name}\nLast name - {message.from_user.last_name}', parse_mode='HTML')

    elif message.text == 'Отправить зашифрованное сообщение':
        bot.send_message(message.from_user.id, "Напишите id своего получателя (напишите <code>stop</code> - если передумали)", parse_mode = 'HTML')
        bot.register_next_step_handler(message, get_id)

    elif message.text == '🛟Помощь':
        bot.send_message(message.chat.id, "CryptoGram - бот, который поможет Вашим сообщениям, которые проходят через Telegram оставаться зашифрованными")
    
    elif message.text == '⬇Скрыть':
        bot.send_message(message.chat.id, "Спасибо, что воспользовались ботом!", reply_markup = types.ReplyKeyboardRemove())


def get_id(message):
    global id_user
    id_user = message.text
    try:
        current_datetime = datetime.now()
        current_datetime = current_datetime.strftime("%H:%M:%S %d.%m.%Y")
        sender.send_message(id_user, f'<b>{message.from_user.first_name}</b> is writing you a new message 😉\n\nName - @{message.from_user.username}\nID - <code>{message.from_user.id}</code>\nFirst name - {message.from_user.first_name}\nLast name - {message.from_user.last_name}\n\nTime of typing: {current_datetime}', parse_mode = 'HTML')
        bot.send_message(message.from_user.id, 'Отправьте <strong>зашифрованное</strong> сообщение', parse_mode = 'HTML')
        bot.register_next_step_handler(message, get_msg)
    except:
        if id_user == 'stop':
            bot.send_message(message.chat.id, 'Хорошо, поиск пользователя остановлен')

        else:    
            bot.send_message(message.chat.id, 'Такого пользователя не существует, введите сообщение заново!')
            bot.send_message(message.from_user.id, "Напишите id своего получателя")
            bot.register_next_step_handler(message, get_id)

def get_msg(message):
    global msg
    msg = message.text
    bot.send_message(message.from_user.id, 'Отправьте вектор инициализации')
    bot.register_next_step_handler(message, get_init_vector)

def get_init_vector(message):
    global init_vector
    init_vector = message.text
    current_datetime = datetime.now()
    current_datetime = current_datetime.strftime("%H:%M:%S %d.%m.%Y")
    sender.send_message(id_user, f'<b>You have a new message: <code>{msg}</code></b>\nInitialization vector - <code>{init_vector}</code>\n\nSender:\nName - @{message.from_user.username}\nID - <code>{message.from_user.id}</code>\nFirst name - {message.from_user.first_name}\nLast name - {message.from_user.last_name}\n\nSending time: {current_datetime}', parse_mode='HTML')
    sender.send_message(message.from_user.id, f'<b>Your</b> message to <code>{id_user}</code>\n\n<b>Message: <code>{msg}</code></b>\nInitialization vector - <code>{init_vector}</code>\n\nSending time: {current_datetime}', parse_mode='HTML')
    bot.send_message(message.chat.id, 'Сообщение успешно отправлено!')
bot.infinity_polling()