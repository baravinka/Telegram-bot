import random
import telebot
bot = telebot.TeleBot('1323964128:AAHAluGjcuNeAGGpiBEOdWOYvx-46l1Qqyc')
from telebot import types
first = ["Сегодня — идеальный день для новых начинаний.","Оптимальный день для того, чтобы решиться на смелый поступок!","Будьте осторожны, сегодня звёзды могут повлиять на ваше финансовое состояние.","Лучшее время для того, чтобы начать новые отношения или разобраться со старыми.","Плодотворный день для того, чтобы разобраться с накопившимися делами."]
second = ["Но помните, что даже в этом случае нужно не забывать про","Если поедете за город, заранее подумайте про","Те, кто сегодня нацелен выполнить множество дел, должны помнить про","Если у вас упадок сил, обратите внимание на","Помните, что мысли материальны, а значит вам в течение дня нужно постоянно думать про"]
second_add = ["отношения с друзьями и близкими.","работу и деловые вопросы, которые могут так некстати помешать планам.","себя и своё здоровье, иначе к вечеру возможен полный раздрай.","бытовые вопросы — особенно те, которые вы не доделали вчера.","отдых, чтобы не превратить себя в загнанную лошадь в конце месяца."]
third = ["Злые языки могут говорить вам обратное, но сегодня их слушать не нужно.","Знайте, что успех благоволит только настойчивым, поэтому посвятите этот день воспитанию духа.","Даже если вы не сможете уменьшить влияние ретроградного Меркурия, то хотя бы доведите дела до конца.",]
sixth = ["Хорошего дня."]
# Метод, который получает сообщения и обрабатывает их
@bot.message_handler(commands=['start', 'go'])
def start_message(message):
    bot.send_message(message.chat.id, 'Привет,хочешь узнать свой гороскоп напиши гороскоп,не знаешь свой знак зодиака напиши zn');
@bot.message_handler(content_types=['text'])
def send_text(message):
        if message.text == 'zn':
                keyboard = types.InlineKeyboardMarkup()
                key_oven = types.InlineKeyboardButton(text='21.03-20.04',  callback_data='Овен')
                keyboard.add(key_oven)
                key_telec = types.InlineKeyboardButton(text='21.04-21.05', callback_data='Телец')
                keyboard.add(key_telec)
                key_bliznecy = types.InlineKeyboardButton(text='22.05-21.06', callback_data='Близнецы')
                keyboard.add(key_bliznecy)
                key_rak = types.InlineKeyboardButton(text='22.06-22.07', callback_data='Рак')
                keyboard.add(key_rak)
                key_lev = types.InlineKeyboardButton(text='23.07-23.08', callback_data='Лев')
                keyboard.add(key_lev)
                key_deva = types.InlineKeyboardButton(text='24.08-23.09', callback_data='Дева')
                keyboard.add(key_deva)
                key_vesy = types.InlineKeyboardButton(text='24.09-23.10', callback_data='Весы')
                keyboard.add(key_vesy)
                key_scorpion = types.InlineKeyboardButton(text='24.10-22.11', callback_data='Скорпион')
                keyboard.add(key_scorpion)
                key_strelec = types.InlineKeyboardButton(text='23.11-22.12', callback_data='Стрелец')
                keyboard.add(key_strelec)
                key_kozerog = types.InlineKeyboardButton(text='23.12-20.01', callback_data='Козерог')
                keyboard.add(key_kozerog)
                key_vodoley = types.InlineKeyboardButton(text='21.01-19.02', callback_data='Водолей')
                keyboard.add(key_vodoley)
                key_ryby = types.InlineKeyboardButton(text='20.02-20.03', callback_data='Рыбы')
                keyboard.add(key_ryby)
                bot.send_message(message.from_user.id, text='Выбери свою дату рождения', reply_markup=keyboard)
        elif message.text == 'Гороскоп' or message.text == 'гороскоп'  :
                bot.send_message(message.from_user.id, "Сейчас я расскажу тебе гороскоп на сегодня.")
                keyboard = types.InlineKeyboardMarkup()
                key_oven = types.InlineKeyboardButton(text='Овен', callback_data='zodiac')
                keyboard.add(key_oven)
                key_telec = types.InlineKeyboardButton(text='Телец', callback_data='zodiac')
                keyboard.add(key_telec)
                key_bliznecy = types.InlineKeyboardButton(text='Близнецы', callback_data='zodiac')
                keyboard.add(key_bliznecy)
                key_rak = types.InlineKeyboardButton(text='Рак', callback_data='zodiac')
                keyboard.add(key_rak)
                key_lev = types.InlineKeyboardButton(text='Лев', callback_data='zodiac')
                keyboard.add(key_lev)
                key_deva = types.InlineKeyboardButton(text='Дева', callback_data='zodiac')
                keyboard.add(key_deva)
                key_vesy = types.InlineKeyboardButton(text='Весы', callback_data='zodiac')
                keyboard.add(key_vesy)
                key_scorpion = types.InlineKeyboardButton(text='Скорпион', callback_data='zodiac')
                keyboard.add(key_scorpion)
                key_strelec = types.InlineKeyboardButton(text='Стрелец', callback_data='zodiac')
                keyboard.add(key_strelec)
                key_kozerog = types.InlineKeyboardButton(text='Козерог', callback_data='zodiac')
                keyboard.add(key_kozerog)
                key_vodoley = types.InlineKeyboardButton(text='Водолей', callback_data='zodiac')
                keyboard.add(key_vodoley)
                key_ryby = types.InlineKeyboardButton(text='Рыбы', callback_data='zodiac')
                keyboard.add(key_ryby)
                bot.send_message(message.from_user.id, text='Выбери свой знак зодиака', reply_markup=keyboard)
@bot.callback_query_handler(func=lambda call: True)
def callback_worker(call):
                        if call.data == "zodiac":
                                # Формируем гороскоп
                               msg = random.choice(first) + ' ' + random.choice(second) + ' ' + random.choice(second_add) + ' ' + random.choice(third)+  ' ' + random.choice(sixth)
                                # Отправляем текст в Телеграм
                               bot.send_message(call.message.chat.id, msg)
                        elif call.data == "Овен":
                                msg = "Вы овен"
                                bot.send_message(call.message.chat.id, msg)
                        elif call.data == "Телец":
                                msg = "Вы телец"
                                bot.send_message(call.message.chat.id, msg)
                        elif call.data == "Близнецы":
                                msg = "Вы близнецы"
                        elif call.data == "Рак":
                                msg = "Вы рак"
                                bot.send_message(call.message.chat.id, msg)
                        elif call.data == "Лев":
                                msg = "Вы лев"
                                bot.send_message(call.message.chat.id, msg)
                        elif call.data == "Дева":
                                msg = "Вы дева"
                                bot.send_message(call.message.chat.id, msg)
                        elif call.data == "Весы":
                                msg = "Вы весы"
                                bot.send_message(call.message.chat.id, msg)
                        elif call.data == "Скорипон":
                                msg = "Вы скорпион"
                                bot.send_message(call.message.chat.id, msg)
                        elif call.data == "Стрелец":
                                msg = "Вы стрелец"
                                bot.send_message(call.message.chat.id, msg)
                        elif call.data == "Козерог":
                                msg = "Вы козерог"
                                bot.send_message(call.message.chat.id, msg)
                        elif call.data == "Водолей":
                                msg = "Вы водолей"
                                bot.send_message(call.message.chat.id, msg)
                        elif call.data == "Рыбы":
                                msg = "Вы рыбы"
                                bot.send_message(call.message.chat.id, msg)
                        else: bot.send_message(call.message.chat.id, 'ошибка')

bot.polling(none_stop=True, interval=0)
