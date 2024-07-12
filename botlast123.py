import telebot
import g4f

bot = telebot.TeleBot('*TOKEN*')
bad_words = open('words.txt').read().strip().split('\n')
def ask_anything(m):
	response = g4f.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=m,
	)
	return response
mode = {}
lang = {}
chat_data = {}
def toggle_mode():
    global mode
    mode = not mode
def lang_mode():
    global lang
    lang = not lang
@bot.message_handler(commands=['start','help', 'info', 'history','mode','modinfo','lang'])

def main(message):
    chat_id = message.chat.id
    if chat_id not in chat_data:
        chat_data[chat_id] = []
    if chat_id not in mode:
        mode[chat_id] = False
        lang[chat_id] = False
    if message.text == '/start':
        if (message.from_user.last_name):
            bot.send_message(message.chat.id,f'Привет, <b>{message.from_user.first_name} {message.from_user.last_name}!</b> Я - виртуальный помощник, созданный для решения сложных вопросов и предоставления информации. \nМоя основная задача - помогать пользователям, отвечая на их вопросы. Если у вас есть какие-либо вопросы, не стесняйтесь обращаться - я готов помочь. ', parse_mode='html')
        else:
            bot.send_message(message.chat.id,f'Привет, <b>{message.from_user.first_name}!</b> Я - виртуальный помощник, созданный для решения сложных вопросов и предоставления информации. \nМоя основная задача - помогать пользователям, отвечая на их вопросы. Если у вас есть какие-либо вопросы, не стесняйтесь обращаться - я готов помочь.\n<b>Бот работает не всегда! Пишите создателю, если хотите, чтобы он его включил /help</b>',parse_mode='html')
    elif message.text == '/help':
        bot.send_message(message.chat.id, 'https://t.me/deletu1844')
    elif message.text == "/info":
        bot.send_message(message.chat.id,f'Меня создал Deletu(/help) 15 октября в 2023 года.\nЯ ChatGPT встроенный в этого телеграмм бота.\nG4F_FB - GPT for Free _ First Bot. \n Сегодня я работаю до -.')
    elif message.text == '/history':
        bot.send_message(message.chat.id, 'v1.0 - Бот создан \'Deletu\' \\ 15.10.2023 \nv2.0 - Меню, фильтрация запросов\\16.10.2023\nv2.1 - Улучшена производительность\\16.10.2023\nv3.0 beta - Добавлены функции /mode /modinfo\\17.10.23\nv3.0 - Исправлены баги, mode более стабилен\\22.10.23')
    elif message.text == "/mode":
        chat_data[chat_id]=[]
        mode[chat_id] = not mode[chat_id]
        if mode[chat_id]:
            bot.send_message(message.chat.id,  f'mode is ON: ИИ - программист', parse_mode='html')
        else:
            bot.send_message(message.chat.id, f'mode is OFF: Обычный ИИ', parse_mode='html')
    elif message.text == '/lang':
        chat_data[chat_id] = []
        lang[chat_id] = not lang[chat_id]
        if lang[chat_id]:
            bot.send_message(message.chat.id,  f'Russian language', parse_mode='html')
        else:
            bot.send_message(message.chat.id, f'English language', parse_mode='html')
    elif message.text == '/modinfo':
        if mode[chat_id]:
            bot.send_message(message.chat.id, "Now mode is ON")
        else:
            bot.send_message(message.chat.id,  "Now mode is OFF")

@bot.message_handler()
def info(message):
	chat_id = message.chat.id
	print(f'{message.from_user.first_name} {message.from_user.last_name}: {message.text}')
	if chat_id not in mode:
		lang[chat_id] = False
		mode[chat_id] = False
	if chat_id not in chat_data:
		chat_data[chat_id] = []
	if any(bad_word in message.text.lower() for bad_word in bad_words):	
		if lang[chat_id]:
			bot.send_message(message.chat.id, "Я не буду отвечать на этот вопрос.")
		else:
			bot.send_message(message.chat.id, "I will not answer such a question.")
	else:
		if mode[chat_id]:
			if lang[chat_id]:
				bot.send_message(message.chat.id, "***Обработка запроса*mode*")
				chat_data[chat_id].append({"role": "user", "content": f'You are a programmer, your colleagues ask this question, help: {message.text}(Translate your answer into Russian)'})
				ans = ask_anything(chat_data[chat_id])
				bot.send_message(message.chat.id, 'Ответ: ' + f'{ans}')
				chat_data[chat_id].append({"role": "assistent", "content": ans})
			else:
				bot.send_message(message.chat.id, "***Processing requests*mode*")
				chat_data[chat_id].append({"role": "user", "content": f'You are a programmer, your colleagues ask this question, help: {message.text}'})
				ans = ask_anything(chat_data[chat_id])
				bot.send_message(message.chat.id, 'Answer: ' + f'{ans}')
				chat_data[chat_id].append({"role": "assistent", "content": ans})
		else:
			if lang[chat_id]:
				bot.send_message(message.chat.id, "***Обработка запроса***")
				chat_data[chat_id].append({"role": "user", "content": f'{message.text}(Translate your answer into Russian)'})
				ans = ask_anything(chat_data[chat_id])
				bot.send_message(message.chat.id, 'Ответ: ' + f'{ans}')
				chat_data[chat_id].append({"role": "assistent", "content":ans})
			else:
				bot.send_message(message.chat.id, "***Processing requests***")
				chat_data[chat_id].append({"role": "user", "content": message.text})
				ans = ask_anything(chat_data[chat_id])
				bot.send_message(message.chat.id, 'Answer: ' + f'{ans}')
				chat_data[chat_id].append({"role": "assistent", "content":ans})


bot.infinity_polling()
