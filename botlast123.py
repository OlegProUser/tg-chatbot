import telebot
import g4f

bot = telebot.TeleBot('*TOKEN*')

def ask_anithing_mode(m):
    response = g4f.ChatCompletion.create(
        model=g4f.models.gpt_4,
        messages=m)
    return response

def ask_anithing(message):
    response = g4f.ChatCompletion.create(
        model=g4f.models.gpt_4,
        messages=[{"role": "user", "content": message}],
    )
    return response



mode = {}
chat_data = {}


def toggle_mode():
    global mode
    mode = not mode

@bot.message_handler(commands=['start','help', 'info', 'history','mode','modinfo','yyyyyyyyyyy','lkawjnf'])

def main(message):
    chat_id = message.chat.id
    if chat_id not in chat_data:
        chat_data[chat_id] = []
    if chat_id not in mode:
        mode[chat_id] = False
    if message.text == '/start':
        if (message.from_user.last_name):
            bot.send_message(message.chat.id,f'Привет, <b>{message.from_user.first_name} {message.from_user.last_name}!</b> Я - виртуальный помощник, созданный для решения сложных вопросов и предоставления информации. \nМоя основная задача - помогать пользователям, отвечая на их вопросы. Если у вас есть какие-либо вопросы, не стесняйтесь обращаться - я готов помочь. ', parse_mode='html')
            print(f'New user - {message.from_user.first_name} {message.from_user.last_name}')
        else:
            bot.send_message(message.chat.id,f'Привет, <b>{message.from_user.first_name}!</b> Я - виртуальный помощник, созданный для решения сложных вопросов и предоставления информации. \nМоя основная задача - помогать пользователям, отвечая на их вопросы. Если у вас есть какие-либо вопросы, не стесняйтесь обращаться - я готов помочь.\n<b>Бот работает не всегда! Пишите создателю, если хотите, чтобы он его включил /help</b>',parse_mode='html')
            print(f'New user - {message.from_user.first_name}')
    elif message.text == '/help':
        bot.send_message(message.chat.id, 'https://t.me/deletu1844')
    elif message.text == "/info":
        print(f'"{message.from_user.first_name}"')
        bot.send_message(message.chat.id,f'Меня создал Deletu(/help) 15 октября в 2023 года.\nЯ ChatGPT встроенный в этого телеграмм бота.\nG4F_FB - GPT for Free _ First Bot. \n Сегодня я работаю до 21:00.')
    elif message.text == '/history':
        bot.send_message(message.chat.id, 'v1.0 - Бот создан \'Deletu\' \\ 15.10.2023 \nv2.0 - Меню, фильтрация запросов\\16.10.2023\nv2.1 - Улучшена производительность\\16.10.2023\nv3.0 beta - Добавлены функции /mode /modinfo\\17.10.23\nv3.0 - Исправлены баги, mode более стабилен\\22.10.23')
    elif message.text == "/mode":
        chat_data[chat_id]=[]
        mode[chat_id] = not mode[chat_id]
        if mode[chat_id]:
            bot.send_message(message.chat.id,  f'mode is ON: ИИ - программист', parse_mode='html')
        else:
            bot.send_message(message.chat.id, f'mode is OFF: Обычный ИИ', parse_mode='html')
    elif message.text == '/modinfo':
        if mode[chat_id]:
            bot.send_message(message.chat.id, "Now mode is ON")
        else:
            bot.send_message(message.chat.id,  "Now mode is OFF")
     
    elif message.text == '/yyyyyyyyyyy': #for develop-test
        print(chat_data)
    elif message.text == '/lkawjnf':
        for x in chat_data:
            print(x)


@bot.message_handler()
def info(message):
    chat_id = message.chat.id
    print(f'{message.from_user.first_name} {message.from_user.last_name}: {message.text}')
    if chat_id not in mode:
        mode[chat_id] = False
    if chat_id not in chat_data:
        chat_data[chat_id] = []
    if ((message.text.count('секс') > 0)or(message.text.lower().count("порн") > 0)or(message.text.lower().count("porn") > 0)or(message.text.lower().count("fuck") > 0)or(message.text.lower().count("наркот") > 0) or(message.text.lower().count("сука") > 0)or(message.text.lower().count("drug") > 0)):
        bot.send_message(message.chat.id, "я не буду отвечать на такой вопрос")
    else:
        if mode[chat_id]:
            bot.send_message(message.chat.id, "***Обработка запроса*mode*")
            chat_data[chat_id].append({"role": "user", "content": f'Ты - программист, твои коллеги задают вот этот вопрос, помоги: {message.text}'})
            ans = ask_anithing_mode(chat_data[chat_id])
            bot.send_message(message.chat.id, 'Ответ: ' + f'{ans}')
            chat_data[chat_id].append({"role": "assistent", "content": ans})
        else:
            bot.send_message(message.chat.id, "***Обработка запроса***")
            chat_data[chat_id].append({"role": "user", "content": message.text})
            ans = ask_anithing_mode(chat_data[chat_id])
            bot.send_message(message.chat.id, 'Ответ: ' + f'{ans}')
            chat_data[chat_id].append({"role": "assistent", "content":ans})


bot.infinity_polling()


