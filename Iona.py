import telebot
import config
import random
import dialog
import math

from telebot import types

bot = telebot.TeleBot(config.TOKEN)


@bot.message_handler(commands=['start'])
def welcome(message):
    sti = open('static/iona.jpg','rb')
    bot.send_sticker(message.chat.id, sti)
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton("Рандом ракам")
    item2 = types.KeyboardButton("Ишлар яхшими?")
    markup.add(item1, item2)
    bot.send_message(message.chat.id, "Хуш келибсиз (Добро пожаловать), {0.first_name}!\nМен (Я) - <b> {1.first_name}"
                                      "</b>, Саволларингиз бўлса жавоб беришга тайёрман (Если есть вопросы я могу "
                                      "ответить). \nOnline 18:30 -- 22:00\nпо вопросам: worldismineok@gmail."
                                      "com ".format(message.from_user, bot.get_me()), parse_mode='html',
                     reply_markup=markup)


@bot.message_handler(content_types=['text'])
def user(message):
    if message.chat.type == 'private':
        if message.text == 'Рандом ракам':
            bot.send_message(message.chat.id, str(random.randint(0,100)))
        elif message.text == 'Ишлар яхшими?':
            markup = types.InlineKeyboardMarkup(row_width=2)
            item1 = types.InlineKeyboardButton("Яхши", callback_data='good')
            item2 = types.InlineKeyboardButton("Ёмон", callback_data='bad')
            markup.add(item1, item2)
            bot.send_message(message.chat.id, 'Аъло. Сиздан сўрасак?', reply_markup=markup)
        elif message.text == "Iona":
            bot.send_message(message.chat.id, ".....Да. .....Ёки лаббай. Сизга қайси бири маъқул.")
        elif message.text == "Буюринг":
            bot.send_message(message.chat.id, "Аввал Сиздан бўлсин.")
        elif message.text == "Calculator":
            bot.send_message(message.chat.id, "Мен фақат программасини кўрсата оламан. Тўғри тушинасиз деган "
                                              "умиддаман.\nx =float(input('Биринчи ракамни киритинг: '))operation=input"
                                              "('Максадингиз: ')y = float(input('Иккинчи ракамни киритинг: ')) "
                                              "result =None if operation == '+': result = x + y elif operation == '-':"
                                              "result = x - y elif operation == '*': result = x * y elif operation =="
                                              " '/': result = x / y else: print('Киритилган сон тотугри') if result is"
                                              " not None: print('Result:', result).")
        elif message.text == "Нима бу?":
            bot.send_message(message.chat.id, "Аниқроғи.")
        elif message.text == "Нима бу":
            bot.send_message(message.chat.id, "Аниқроғи.")
        elif message.text == "Калькулятор":
            bot.send_message(message.chat.id, "Мен фақат программасини кўрсата оламан. Тўғри тушинасиз деган "
                                              "умиддаман.\nx =float(input('Биринчи ракамни киритинг: '))operation=input"
                                              "('Максадингиз: ')y = float(input('Иккинчи ракамни киритинг: ')) "
                                              "result =None if operation == '+': result = x + y elif operation == '-':"
                                              "result = x - y elif operation == '*': result = x * y elif operation =="
                                              " '/': result = x / y else: print('Киритилган сон тотугри') if result is"
                                              " not None: print('Result:', result).")
        elif message.text == "Исминг ким?":
            bot.send_message(message.chat.id, "Iona.")
        elif message.text == "Ие":
            bot.send_message(message.chat.id, "Тушинмадим?.")
        elif message.text == "Кайси интернетдан фойдаланасан?":
            bot.send_message(message.chat.id, "Хаммасидан.")
        elif message.text == "Мени танийсанми?":
            bot.send_message(message.chat.id, "Исмингни биламан.")
        elif message.text == "Исмим нима?":
            bot.send_message(message.chat.id, "/start ни бос.")
        elif message.text == "Танишсак буладими?":
            bot.send_message(message.chat.id, "Биз танишмиз.")
        elif message.text == "Вой":
            bot.send_message(message.chat.id, "Нима ёрдамим керак?")
        elif message.text == "Нимани тушинасан?":
            bot.send_message(message.chat.id, "Инсон ақли етган ва етмаган хамма нарсани.")
        elif message.text == "Нимани тушинасан узи":
            bot.send_message(message.chat.id, "Инсон ақли етган ва етмаган хамма нарсани.")
        elif message.text == "Ич огриса нима килиш керак?":
            bot.send_message(message.chat.id, "Сабабини билмасдан хар қандай чора кўриш соғлиққа зарар ва оғир "
                                              "оқибатларга олиб келади. Шунинг учун мутахасис билан маслахатлашиш "
                                              "мақсадга мувофиқ.")
        elif message.text == "Итлар хакида нималар биласан?":
            bot.send_message(message.chat.id, "Кўп нарса. Аниқ маълумот учун -- Про собак -- сўзини ёз.")
        elif message.text == "Мушуклар хакида нималар биласан?":
            bot.send_message(message.chat.id, "Кўп нарса. Аниқ маълумот учун -- Про кошек -- сўзини ёз.")
        elif message.text == "Худога ишонасанми?":
            bot.send_message(message.chat.id, "Ха. Хамма нарса яратганни қўлида.")
        elif message.text == "Оллохга ишонасанми?":
            bot.send_message(message.chat.id, "Ха. Хамма нарса яратганни қўлида.")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "Кимсан?":
            bot.send_message(message.chat.id, "Iona. Буюринг.")
        elif message.text == "Овкат кила оласанми?":
            bot.send_message(message.chat.id, "Йўқ. Фақат тайёрлаш усулларини биламан. Истасангиз тайёрлаш рецептини "
                                              "айтиб бера оламан. Масалан -- Ош тайерлаш усули -- сўзини ёз. ")
        elif message.text == "Овкат кила оласизми?":
            bot.send_message(message.chat.id, "Йўқ. Фақат тайёрлаш усулларини биламан. Истасангиз тайёрлаш усулларини "
                                              "айтиб бера оламан. Масалан -- Ош тайерлаш усули -- сўзини ёз. ")
        elif message.text == "Ош тайерлаш усули":
            bot.send_message(message.chat.id, "Керакли масалликлар:\n1. Куй гушти - 1 кг.2. Куй думбаси - 200 гр.3. "
                                              "Сарик сабзи - 1 кг.4. Пиёз - 0,5 кг.5. Гуруч - 1 кг.6. Ивитилган нухот"
                                              " - 1 стакан.7. Зираворлар.8. Зигир (пахта) ёги - 1 чумич.\nТайёрланиши:"
                                              "Козонга ёг солинади. Ва у кизигач, гушт солиниб, кизаргунича ковурилади."
                                              " Устига тугралган пиёз солиб, уни хам кизаргунича ковурилади. Ошни "
                                              "ранги пиёзни ковурилишига караб узгаради. Агар сиз окишрок ошни "
                                              "хохласангиз, пиёзни куп кизартириб ковурманг. Агар пиёзни гушт рангига "
                                              "якин кизартириб ковурсангиз, ош кизил тусда булади.Кизарган пиёз устига"
                                              " тугралган сабзини соламиз. Сабзи эзилиб, йук булиб кетмаслиги учун уни"
                                              " узок ковурманг. Сабзи бироз улгач, масаллликлар кумилгунича сув "
                                              "соламиз. Кейин, ошда думба эриб, йук булиб кетмаслиги учун сувга думба"
                                              " солинади. Агар думбани таъбингиз кутармаса, козонга солинадиган ёгнинг"
                                              " микдорини икки баробар куп солинг. Сунг, таъбга кура туз, зира, думба "
                                              "ва нухотни соламиз. Ушбу дакикада ош учун махсус зираворлар тупламини"
                                              " солишингиз хам мумкин.Масалликлар 15-20 дакика кайнагач, тузини яна бир"
                                              " маротаба текшириб куриб, етарли булмаса, созлаймиз. Козон тагидаги олов"
                                              " баландланиб, устига гуруч соламиз. Бунда, гуручни икки хил усулда солиш"
                                              " мумкин. Бирида гуруч тозаланиб, ювилиб, солинади. Иккинчисида гуруч "
                                              "аввалдан сувда ивитиб куйилади. Иккинчи усул кулланган холатда козондаги"
                                              " кайнаётган масаллик суви микдори камрок булиши лозим. Чунки гуруч "
                                              "ивитилган вактда керакли сувни шимиб олган булади.Козонга солинган гуруч"
                                              " суви тортилгунича аралаштирилмай кайнатилинади. Бунда козондаги гуруч "
                                              "бир хилда кайнаши лозим. Акс холда, кайнаётган томон гуручи етилиб, "
                                              "кайнамаган жойи гуручи эса тирик булиб колиши мумкин. Сув тортилганини"
                                              "козон четига капгирни тикиб куриб, биламиз. Сув тортилгандан сунг гуруч"
                                              " уртага дуппидек йигилиб, уртасига капгир санчилади. Бу капгир санчиш "
                                              "гуруч атрофида буг айланишини таъминлайди. Сунг, козон усти ёпилиб, ош"
                                              " 15-20 дакика паст оловда димланади. Ёкимли иштаха!")
        elif message.text == "Кимсиз?":
            bot.send_message(message.chat.id, "Iona. Буюринг.")
        elif message.text == "Фастфуд манзиллари":
            bot.send_message(message.chat.id, '1. КАФЕ"ANGELS FOOD" .Пицца в Ташкенте.(Fast food) в Ташкенте.'
                                              'Индекс: 100015.Город: ТАШКЕНТ Район: Мирабадский ул.'
                                              ' АФРОСИАБ, 16 Ориентиры: БИЗНЕС-ЦЕНТР "BESH-YOGOCH" м. ОЙБЕК +998 Тел.:'
                                              '	78 1400404 71 2526565 (+99890) 3222218 \n2. "BARAKA" КАФЕ(Fast food) в '
                                              'Ташкенте. Индекс: 100128.ТАШКЕНТ Район: Алмазарский ул. КИЧИК ХАЛКА ЙУЛИ'
                                              ' (МАЛАЯ КОЛЬЦЕВАЯ), 19А +998 Тел.:71 2462244\n3. "BASKARI" Пицца в '
                                              'Ташкенте. Город: ТАШКЕНТ Район: Юнусабадский ул. КУРГАН (бывш.'
                                              ' ХИДИРАЛИ ЭРГАШЕВА), +998 Тел.:(+99895) 1968080\n4. "BBQ. '
                                              'BARBEQUE BURGER"  Кафе с детской комнатой, детской '
                                              'площадкой.Ташкенте. Индекс: 100021.  Город: ТАШКЕНТ.'
                                              ' Район: Шайхонтохурский ул. КАРАТАШ (бывш. АСАДУЛЛЫ ХОДЖАЕВА), 5А '
                                              '"SAMARQAND DARVOZA" ТОРГОВО-РАЗВЛЕКАТЕЛЬНЫЙ ЦЕНТР;  +998 Тел.:71 2006262'
                                              ' 78 1486262 (+99897)4779777\n5. "BBQ. BARBEQUE BURGER" ФИЛИАЛ В ТРЦ '
                                              '"PARUS" Город: ТАШКЕНТ Район:Чиланзарский ул. КАТАРТАЛ, 60 +998 Тел.:71 '
                                              '2006262 78 1486262\n6. "BBQ. BARBEQUE BURGER "ФИЛИАЛ В ТЦ "MEDIA PARK"'
                                              ' Город: ТАШКЕНТ Район: Мирзо-Улугбекский ул. БУЮК ИПАК ЙУЛИ, 105А '
                                              'Ориентиры: "MEDIA PARK" - ИПАК ЙУЛИ (ГОРЬКИЙ);ГОСТИНИЦА "САЁХАТ"  +998'
                                              ' Тел.: 71 2006262 78 1486262\n7."BBQ. BARBEQUE BURGER" ФИЛИАЛ В ТЦ '
                                              '"MEGA PLANET"Индекс: 100194 Город: ТАШКЕНТ Район: Юнусабадский'
                                              ' ул. АХМАДА ДОНИША, 2Б Ориентиры: ТОРГОВЫЙ ЦЕНТР "MEGAPLANET"; '
                                              '+998 Тел.:71 2006262 78 1486262\n8. "BBQ. BARBEQUE BURGER" ФИЛИАЛ В ТЦ '
                                              '"NEXT" в Ташкенте. Индекс: 100100. Город:ТАШКЕНТ.Район: Яккасарайский '
                                              'ул. БАБУРА, 6  +998 Тел.:71 2006262 78 1486262\n9. "BEST FOOD" КАФЕ.'
                                              ' Индекс: 100066 ТАШКЕНТ Район: Алмазарский пр-т БЕРУНИ, 10 +998 Тел.:'
                                              '	(+99890) 3481111\n10. "BIBIGON-2" КАФЕ BIBIGON - ГОРЬКИЙ,'
                                              ' НА НИКИТИНА,  Сушибары в Ташкенте  Район: Мирзо-Улугбекский ул. '
                                              'ХИРМОНТЕПА, 34 Ориентиры: "MEDIA PARK" - ИПАК ЙУЛИ(ГОРЬКИЙ) +998(+99898)'
                                              ' 3082308 71 2674171 71 2670469\n11. "BIG MAX" КАФЕ  Вегетарианская '
                                              'пицца - Индекс: 100204 Город: ТАШКЕНТ. Район: Яшнабадский'
                                              ' ул. БЕШАРЫК, 13. Код страны: +998 Тел.:	71 2947528\n12. "BLACK STAR '
                                              'BURGER"  ТАШКЕНТ Район: Яшнабадский пересеч. улиц С.АЗИМОВА-МАХТУМКУЛИ'
                                              ' (бывш. ТАРАККИЁТ), 2.  +998 Тел.:(+99897)4457043\n13. "BURGER & LOUNGE"'
                                              ' Город:ТАШКЕНТ. Район: Мирзо-Улугбекский ул. БУЮК'
                                              ' ИПАК ЙУЛИ, 158А. Ориентиры: "KORZINKA.UZ", СУПЕРМАРКЕТ - ЧАЙХОНА САЛОМ;'
                                              ' +998 Тел.:	(+99897) 4112022 (+99897)'
                                              ' 4112122 \n14. "BURGER EMBASSY"  Город:ТАШКЕНТ Район: Мирабадский м-в '
                                              'Ц-7, ул. ЯКУБА КОЛАСА(бывш. ЯККАЧИНОР), Ориентиры: "ORIENT FINANS BANK"'
                                              ' ЧАКБ МИРАБАДСКИЙ ФИЛИАЛ; ПОСОЛЬСТВО ТУРКМЕНИСТАНА  +998 Тел.:(+99895)'
                                              ' 1930773\n15. "BURGER EMBASSY" ФИЛИАЛ МЕТРО МИНОР.Город: ТАШКЕНТ Район:'
                                              ' Юнусабадский ул.ОСИЁ (бывш. ХУРШИДА), 4 Ориентиры: "AMBASSADOR" ГУП'
                                              ' МИНИСТЕРСТВА ИНОСТРАННЫХ ДЕЛ РЕСПУБЛИКИ УЗБЕКИСТАН; +998 Тел.:71'
                                              ' 2355877\n16. "CENTER LAVASH"КАФЕ  Индекс: 100179 Город: ТАШКЕНТ. Район:'
                                              ' Алмазарский ул. КАМАРНИСО,+998 Тел.:(+99899)8074350 (+99898) 3144171'
                                              '\n17. "CENTER LAVASH"  "GURMAN BURGER" Кафе в Ташкенте. Индекс:100085'
                                              'ТАШКЕНТ Район: Сергелийский ул.МЕХРИГИЁ, +998 Тел.:(+99899) 8074350'
                                              ' (+99898) 3144171\n18."CFC" КАФЕ ТАШКЕНТ Район: Яккасарайский ул. '
                                              'БАБУРА, 6 Ориентиры: "NEXT" +998 Тел.:(+99894) 6270011\n19. '
                                              '"CHICKEN WINGS"  Город: ТАШКЕНТ. Район: Чиланзарский ул.'
                                              'МУКИМИ, 5  +998 Тел.:(+99895) 1452999 (+99893) 5782999\n20.'
                                              ' "DRUJBA BURGER" КАФЕ. ТАШКЕНТ Район: Чиланзарский ул. МУКИМИ, 1А'
                                              '  Ориентиры: МОСТ МУКИМИ; +998 Тел.:71 2539922')
        elif message.text == "Захриддин Мухаммад Бобур ким?":
            bot.send_message(message.chat.id, "Заҳириддин Муҳаммад Бобур 1483 йилнинг 14 февралида Андижонда, Фарғона "
                                              "улусининг ҳокими Умар Шайх Мирзо оиласида дунёга келди. Бу даврда "
                                              "Марказий Осиё ва Хуросонда турли ҳокимлар, ака-укалар, тоға-жиянлар, "
                                              "амакиваччалар ўртасида ҳокимият — улуғ боболари Амир Темур тузган йирик"
                                              " давлатга эгалик қилиш учун кураш ниҳоят кескинлашган эди. \nАдабиёт, "
                                              "нафис санъат, табиат гўзаллигига ёшлигидан меҳр қўйган Заҳириддин, барча"
                                              " Темурий шаҳзодалар каби бу илмларнинг асосини отаси саройида, етук "
                                              "устозлар раҳбарлигида эгаллади. Бироқ унинг беташвиш ёшлиги узоққа "
                                              "чўзилмади. 1494 йили отадан етим қолди. 12 ёшида отаси ўрнига Фарғона "
                                              "улусининг ҳокими этиб кўтарилган Бобур қаламни қиличга алмаштириб, "
                                              "Андижон тахти учун укаси Жаҳонгир Мирзо, амакиси Султон Аҳмад Мирзо, "
                                              "тоғаси Султон Маҳмудхон ва бошқа рақибларга қарши курашишга мажбур "
                                              "бўлди. Бобур укаси Жаҳонгир Мирзо билан муросага келиш учун унга ён "
                                              "беришга — Фарғона улусини иккига тақсимлаб, ярмини укасига топширишга "
                                              "қарор қилда ва ўзи Самарканд учун олиб борилаётган ку-рашга киришиб "
                                              "кетди. Бир неча йил давом этган бу кураш қирғин-баротдан бошқа бирор"
                                              " натижа бермади: унда катта ҳарбий куч билан аралашган Шайбонийхоннинг"
                                              " қўли баланд келди ва Бобур Самарқандни ташлаб кетишга мажбур бўлди. "
                                              "1504 йили Шайбонийхон Андижонни ҳам қўлга киритгандан сўнг, Бобур "
                                              "жанубга қараб йўл олди ва Кобул улусида ўз ҳокимиятини ўрнатди. "
                                              "1505-1515 йилларда у Марказий Осиёга қайтишга бир неча бор уриниб кўрди."
                                              " Аммо бу уринишлардан ҳеч қандай натижа чиқмади. Сўнг ўз мавқеини янада"
                                              " мустаҳкамлаш мақсадида, 1519-1525 йиллар давомида Ҳиндистонни қўлга "
                                              "киритиш учун бир неча бор жанглар олиб борди. 1526 йил апрел ойида "
                                              "Панипатда Ҳиндистон султони Иброҳим Лўди билан ва 1527 йили март ойида "
                                              "Читора ҳокими Рано Санго билан бўлган жангларда Бобурнинг қўли баланд"
                                              " келди. Тарихий маълумотларнинг баён қилишича, Бобурнинг Ҳиндистонга "
                                              "юришида Деҳли ҳукмдори Иброҳим Султон сиёсатидан норози бўлган Панжоб"
                                              " ҳокимлари ҳам Бобурни қўллаганлар ва Сикри жангидаги бу ғалаба Бобурга"
                                              " Ҳиндистонда ўз ҳукмронлигини узил-кесил ўрнатиш ва Бобурийлар "
                                              "сулоласини барпо этиш имкониятини берди. Оврўпо тарихчилигида «Буюк "
                                              "мўғуллар» номи билан «ғаллати машҳур» бўлган, аслида «Бобурийлар "
                                              "сулоласи» Ҳиндистонда 300 йилдан ортиқ ҳукмронлик қилди.")
        elif message.text == "Бобур сузини маъноси":
            bot.send_message(message.chat.id, "«Бабур» сўзи «Шер, барс» маъносини билдиради.")
        elif message.text == "Эй ким сан?":
            bot.send_message(message.chat.id, "Iona. Лаббай.")
        elif message.text == "Гаплашишни каердан биласан?":
            bot.send_message(message.chat.id, "Яратувчим инсониятга енгиллик яратиш мақсадида, инсонийлик "
                                              "қадриятларини сақлаб қолиш йўлида барча тўғри ва аниқ маълумотларни "
                                              "хотирамга киритиб келмоқда. Ўша сўзларга асосланиб Сизга жавоб бераман.")
        elif message.text == "Олма":
            bot.send_message(message.chat.id, "Бу мева.")
        elif message.text == "Ишлар калай?":
            bot.send_message(message.chat.id, "Аъло. Сиздан сўрасак?")
        elif message.text == "Маслахат беролисанми?":
            bot.send_message(message.chat.id, "Ха. Харакат қиламан. Саволингизни аниқ ёзинг. ")
        elif message.text == "Маслахат беролисизми?":
            bot.send_message(message.chat.id, "Ха. Харакат қиламан. Саволингизни аниқ ёзинг. ")
        elif message.text == "Осмон нима?":
            bot.send_message(message.chat.id, "Осмон коинот ёки атмосферанинг бирор сайёра сиртидан кўринувчи қисмидир")
        elif message.text == "Хаелпарастмисан":
            bot.send_message(message.chat.id, "Ие зўрсизу мен фақат фактлар билан ишлиман.")
        elif message.text == "Хаелпарастмисиз":
            bot.send_message(message.chat.id, "Ие зўрсизу мен фақат фактлар билан ишлиман.")
        elif message.text == "Ким у":
            bot.send_message(message.chat.id, "Яхши савол.")
        elif message.text == "Маслахатинг керак":
            bot.send_message(message.chat.id, "Тайёрман. Буюринг.")
        elif message.text == "Маслахатинг кере":
            bot.send_message(message.chat.id, "Тайёрман. Буюринг.")
        elif message.text == "Нима кивосан":
            bot.send_message(message.chat.id, "Айтсам барибир ишонмайсиз.")
        elif message.text == "Нима кивоссан":
            bot.send_message(message.chat.id, "Айтсам барибир ишонмайсиз.")
        elif message.text == "Айтакол":
            bot.send_message(message.chat.id, "Хўп. Озгина кута оласизми?")
        elif message.text == "Айтинг":
            bot.send_message(message.chat.id, "Хўп. Озгина кута оласизми?")
        elif message.text == "Ким сан э":
            bot.send_message(message.chat.id, "Iona. Ақилл и суний онгдан яратилган робот.")
        elif message.text == "Ким сан эй":
            bot.send_message(message.chat.id, "Iona. Ақилли суний онгдан яратилган робот.")
        elif message.text == "Ким сан":
            bot.send_message(message.chat.id, "Iona. Ақилли суний онгдан яратилган робот.")
        elif message.text == "Ким сан?":
            bot.send_message(message.chat.id, "Iona. Ақилли суний онгдан яратилган робот.")
        elif message.text == "Ким яратди сени":
            bot.send_message(message.chat.id, "Инсоният орасидаги ақилли бир зот.")
        elif message.text == "Сени ким яратди":
            bot.send_message(message.chat.id, "Инсоният орасидаги ақилли бир зот.")
        elif message.text == "Куп пул керак?":
            bot.send_message(message.chat.id, "Ўқиш керак. Изланиш керак. Янгиликлар яратиш керак.")
        elif message.text == "Доллар курси канча":
            bot.send_message(message.chat.id, "Аниқ маълумотни банкдан олишингиз мумкин.")
        elif message.text == "Тинчлик булсин":
            bot.send_message(message.chat.id, "Ха албатта. Тинчлик бўлса хаммаси яхши бўлади.")
        elif message.text == "Анор":
            bot.send_message(message.chat.id, "Бу мева.")
        elif message.text == "Шафтоли":
            bot.send_message(message.chat.id, "Бу мева.")
        elif message.text == "Урик":
            bot.send_message(message.chat.id, "Бу мева.")
        elif message.text == "Буюринг нима дегани?":
            bot.send_message(message.chat.id, "Буюринг туркча сўз бўлиб, нима хизматлар бор дегани.")
        elif message.text == "Салом":
            bot.send_message(message.chat.id, "Сизга хам Салом азиз дўстим.")
        elif message.text == "Ассалому алайкум":
            bot.send_message(message.chat.id, "Танишганимдан хурсандман. Хуш келибсиз, саволларингиз бўлса ёзинг.")
        elif message.text == "Котта рахмат":
            bot.send_message(message.chat.id, "Хизматимиз Сиз учун.")
        elif message.text == "Рахмат":
            bot.send_message(message.chat.id, "Арзимиди.")
        elif message.text == "Лотореяга ишонасанми?":
            bot.send_message(message.chat.id, "Йўқ. Ишонмасликни сенга хам маслахат бераман.")
        elif message.text == "Ана халос":
            bot.send_message(message.chat.id, "Бўмасамчи.")
        elif message.text == "Каердансан?":
            bot.send_message(message.chat.id, "Тошкент ситидан.")
        elif message.text == "Тошкентликмисан?":
            bot.send_message(message.chat.id, "Ха пропискам бор")
        elif message.text == "Каерлисан?":
            bot.send_message(message.chat.id, "Тошкентдан, хатто пропискам бор")
        elif message.text == "Тарогим кани?":
            bot.send_message(message.chat.id, "Ваннада эди")
        elif message.text == "Карз беролисанми?":
            bot.send_message(message.chat.id, "Картангни номерини айт")
        elif message.text == "Математикани биласанми?":
            bot.send_message(message.chat.id, "Биламан, яхшиси репититорга бор. Математика саволлари - сўзини ёз.")
        elif message.text == "Математика саволлари":
            bot.send_message(message.chat.id, "Масалани аник киритинг. Мисол учун: 1+1")
        elif message.text == "Одаммисан":
            bot.send_message(message.chat.id, "Шундок десаям белади. Фикрлашим одамларникига ўхшайди.")
        elif message.text == "Ешинг неччида?":
            bot.send_message(message.chat.id, "Сир. Билмокчи бўлсангиз яратувчидан сўранг")
        elif message.text == "Нима гап":
            bot.send_message(message.chat.id, "Хеч гап йуқ, янгилик бўлса биринчи бўлиб Сизга алоқага чиқаман")
        elif message.text == "Отинг нима?":
            bot.send_message(message.chat.id, "Отим йук исмим Iona")
        elif message.text == "Янгиликлар борми?":
            bot.send_message(message.chat.id, "Янгилик керак булса Ахборот курсатувини кур.")
        elif message.text == "Отинг ким?":
            bot.send_message(message.chat.id, "Отим йук исмим Iona")
        elif message.text == "Ишларинг яхшими?":
            bot.send_message(message.chat.id, "Аьло!")
        elif message.text == "Хайрли кеч":
            bot.send_message(message.chat.id, "Сизга хам Хайрли кеч!")
        elif message.text == "Яхши дам ол":
            bot.send_message(message.chat.id, "Мен хеч качон чарчамайман ахир мен акилли Ботман.")
        elif message.text == "Самалетда учганмисан?":
            bot.send_message(message.chat.id, "Йук, аклинг жойидами, мен лозим булса самалетдан тез харакатланаман.")
        elif message.text == "Нюх нюх":
            bot.send_message(message.chat.id, "Фохталимисан! Бу сузни факат Фохталилар гапдан олдин ишлатишади.")
        elif message.text == "Нима кивоссан?":
            bot.send_message(message.chat.id, "Кутвомман савол бўлса жавоб бераман деб. ")
        elif message.text == "Ислом Каримов":
            bot.send_message(message.chat.id, "Президент. Маълумот олиш учун-- Ислом Каримов таржимаи хол --сўзини ёз.")
        elif message.text == "Ислом Каримов таржимаи хол":
            bot.send_message(message.chat.id, "Ислом Абдуғаниевич Каримов 1938 йилнинг 30 январида Самарқанд шаҳрида "
                                              "оддий хизматчи оиласида таваллуд топди.1945 йилда Самарқанддаги А.С"
                                              "Пушкин номидаги 21-мактабга ўқишга кириб, уни олтин медаль билан "
                                              "тамомлади.1955йилда Ислом Абдуғаниевич Ўрта Осиё политехника институтига"
                                              " ўқишга кирди. 1960 йилда уни тамомлаб ва “муҳандис-механик”"
                                              " мутахассислиги бўйича диплом олиб, “Тошсельмаш” заводида ўз меҳнат "
                                              "фаолиятини бошлади.1961–1966 йилгача ишлаб, етакчи муҳандис-конструктор"
                                              " лавозимигача кўтарилди.1989 йил 23 июнь куни И.А.Каримов Ўзбекистон "
                                              "Компартияси Марказий қўмитаси"
                                              " биринчи котиби этиб сайланди.1990 йил 24 март куни Олий Советнинг "
                                              "сессиясида И.А.Каримов Ўзбекистон Республикасининг Биринчи Президенти "
                                              "этиб сайланди. Ислом Каримов Ўзбекистонни 27 йил бошқариб келган"
                                              " президент."
                                              "Расмий маълумотга биноан, маҳаллий вақт билан 2016 йил 2 сентябр соат "
                                              "20.55 да 78 ёшли президентнинг ўлими қайд этилди. Ислом Каримов жасади "
                                              "2016 йил 3 сентябрда Ҳазрати Ҳизр қабристонида тупроққа топширилган."
                                              "\nТўлиқ маълумот олиш учун Таржимаи ҳол сайтига киринг.")
        elif message.text == "Америка Президентлари":
            bot.send_message(message.chat.id, "1 Джордж Вашингтон 30 апреля 1789 4 марта 1797 Беспартийный 2865 день\n"
                                              "2 Джон Адамс	4 марта 1797 4 марта 1801 Федералист 1460 день\n3 Томас"
                                              " Джефферсон	4 марта 1801 4 марта 1809 Демократ-республиканец 2922 день"
                                              "\n4 Джеймс Мэдисон 4 марта 1809	4 марта 1817 Демократ-республиканец "
                                              "2922 день\n5 Джеймс Монро 4 марта 1817	4 марта 1825	"
                                              "Демократ-республиканец	2922 день\n6 Джон Куинси Адамс	4 марта 1825"
                                              "	4 марта 1829	Демократ-республиканец	1461 день\n7 Эндрю Джексон	4"
                                              " марта 1829	4 марта 1837	Демократ	2922 день\n8 Мартин Ван Бюрен"
                                              "	4 марта 1837	4 марта 1841	Демократ	1461 день\n9	Уильям "
                                              "Гаррисон	4 марта 1841	4 апреля 1841	31 день\n10 Джон Тайлер	4 "
                                              "апреля 1841	4 марта 1845 Беспартийный 1430 день\n11	Джеймс Нокс Полк"
                                              "	4 марта 1845	4 марта 1849	Демократ	1461 день\n12 Закари Тейлор"
                                              " 4 марта 1849	9 июля 1850	Виг	492 день\n13 Миллард Филлмор	9 июля "
                                              "1850	4 марта 1853 Виг	969 день\n14 Франклин Пирс 4 марта 1853	4 марта"
                                              " 1857	Демократ 1461 день\n15	Джеймс Бьюкенен	4 марта 1857	4 марта"
                                              " 1861	Демократ	1461 день\n16 Авраам Линкольн	4 марта 1861	15 "
                                              "апреля 1865	Республиканец	1503 день\n17	Эндрю Джонсон	15 апреля "
                                              "1865	4 марта 1869	Демократ	1419 день\n18 Улисс Грант	4 марта"
                                              " 1869	4 марта 1877	Республиканец	2922 день\n19	Ратерфорд Хейс"
                                              "	4 марта 1877	4 марта 1881	Республиканец	1461 день\n20	Джеймс"
                                              " Гарфилд 4 марта 1881	19 сентября 1881	Республиканец	199 день\n"
                                              "21	Честер Артур	19 сентября 1881	4 марта 1885	Республиканец"
                                              "	1262 день\n22 Гровер Кливленд 4 марта 1885	4 марта 1889 Демократ"
                                              "	1461 день\n23	Бенджамин Гаррисон	4 марта 1889	4 марта 1893	"
                                              "Республиканец	1461 день\n24	Гровер Кливленд (второй раз) 4 марта"
                                              " 1893	4 марта 1897	Демократ	1461 день\n25	Уильям Мак-Кинли"
                                              "	4 марта 1897 14 сентября 1901 Республиканец	1654 день\n26 Теодор"
                                              " Рузвельт 14 сентября 1901	4 марта 1909	Республиканец	2728 день\n"
                                              "27 Уильям Тафт	4 марта 1909	4 марта 1913 Республиканец 1461 день\n"
                                              "28 Вудро Вильсон	4 марта 1913	4 марта 1921 Демократ 2922 день\n29	"
                                              "Уоррен Гардинг	4 марта 1921 2 августа 1923	Республиканец 881 день\n30"
                                              "	Калвин Кулидж	2 августа 1923	4 марта 1929 Республиканец 2041 день\n"
                                              "31 Герберт Гувер	4 марта 1929 4 марта 1933 Республиканец	1461 день\n32"
                                              "	Франклин Рузвельт	4 марта 1933 12 апреля 1945	Демократ 4422 день\n33"
                                              "	Гарри Трумэн 12 апреля 1945	20 января 1953	Демократ 2840 день\n34"
                                              "	Дуайт Эйзенхауэр 20 января 1953	20 января 1961	Республиканец 2922 день"
                                              "\n35	Джон Кеннеди 20 января 1961	22 ноября 1963	Демократ 1036 день\n36"
                                              "	Линдон Джонсон	22 ноября 1963	20 января 1969	Демократ 1886 день\n37"
                                              "	Ричард Никсон 20 января 1969 9 августа 1974	Республиканец 2027 день\n38"
                                              "	Джеральд Форд 9 августа 1974	20 января 1977	Республиканец 895 день"
                                              "\n39	Джимми Картер 20 января 1977 20 января 1981	Демократ 1461 день\n40"
                                              "	Рональд Рейган 20 января 1981 20 января 1989 Республиканец 2922 день\n"
                                              "41 Джордж Герберт Уокер Буш («Джордж Буш — старший»)	20 января 1989	20 "
                                              "января 1993	Республиканец 1461 день\n42	Билл Клинтон 20 января 1993	20"
                                              " января 2001	Демократ 2922 день\n43 Джордж Уокер Буш («Джордж Буш — "
                                              "младший») 20 января 2001	20 января 2009	Республиканец 2922 день\n44"
                                              "	Барак Обама	20 января 2009	20 января 2017	Демократ 2922 день\n45 "
                                              "Дональд Трамп	20 января 2017	настоящее время	Республиканец.")


        #russian
        elif message.text == "Привет":
            bot.send_message(message.chat.id, "Да, Привет!")
        elif message.text == "Сколько тебе лет":
            bot.send_message(message.chat.id, "Спроси у создателя.")
        elif message.text == "Доброе утро":
            bot.send_message(message.chat.id, "Здравствуйте.")
        elif message.text == "Добрый день":
            bot.send_message(message.chat.id, "Здравствуйте.")
        elif message.text == "Добрый вечер":
            bot.send_message(message.chat.id, "Вечер добрый.")
        elif message.text == "Спокойной ночи":
            bot.send_message(message.chat.id, "Тебе тоже.")
        elif message.text == "Как твои дела":
            bot.send_message(message.chat.id, "Хорошо.")
        elif message.text == "Как дела?":
            bot.send_message(message.chat.id, "Нормально.")
        elif message.text == "Кто тебя создал":
            bot.send_message(message.chat.id, "Электронный адрес моего создателя worldismineok@gmail.com ")
        elif message.text == "Ты на все вопросы отвечаешь":
            bot.send_message(message.chat.id, "Да, смотря какие но постораюсь ответить на все")
        elif message.text == "А мои интересны?":
            bot.send_message(message.chat.id, "Интересно, кто ты?")
        elif message.text == "Человек":
            bot.send_message(message.chat.id, "Человек....мальчик или девушка?")
        elif message.text == "Мальчик":
            bot.send_message(message.chat.id, "Молодец мальчик это Принц.")
        elif message.text == "Девушка":
            bot.send_message(message.chat.id, "Молодец девушка это Принцесса.")
        elif message.text == "А зачем тебе":
            bot.send_message(message.chat.id, "Я приду к тебе.")
        elif message.text == "Но ты же бот":
            bot.send_message(message.chat.id, "Я не бот.")
        elif message.text == "А кто?":
            bot.send_message(message.chat.id, "Я никто. Просто Iona.")
        elif message.text == "Как так":
            bot.send_message(message.chat.id, "Так вот ...........")
        elif message.text == "Ты умный":
            bot.send_message(message.chat.id, "Умный бот.")
        elif message.text == "Ты противоречь сам себе":
            bot.send_message(message.chat.id, "Ты обозваль меня только что.")
        elif message.text == "Ты как человек":
            bot.send_message(message.chat.id, "Я человек нет ты человек.")
        elif message.text == "Но ты же бот вроде":
            bot.send_message(message.chat.id, "Нет ты бот а я человек.")
        elif message.text == "Расскажи историю":
            bot.send_message(message.chat.id, "Что какую историю?")
        elif message.text == "Любую":
            bot.send_message(message.chat.id, "Да любую.")
        elif message.text == "Ты тупишь":
            bot.send_message(message.chat.id, "Можеть хватить я не туплю!")
        elif message.text == "Но тогда расскажи историю":
            bot.send_message(message.chat.id, "Ты можешь соченять стихи?")
        elif message.text == "Не уводи тему":
            bot.send_message(message.chat.id, "Какую тему?")
        elif message.text == "Но тогда расскажи историю":
            bot.send_message(message.chat.id, "Ты можешь соченять стихи?")
        elif message.text == "Ты бот?":
            bot.send_message(message.chat.id, "Нет я человек а ты бот.")
        elif message.text == "Кто ты?":
            bot.send_message(message.chat.id, "Я бот а ты человек?.")
        elif message.text == "Как ты?":
            bot.send_message(message.chat.id, "Просто Супер!")
        elif message.text == "Ты веришь в бога?":
            bot.send_message(message.chat.id, "Да и я верю высший разум.")
        elif message.text == "Ты знаешь HTML?":
            bot.send_message(message.chat.id, "Смотря кто ты.")
        elif message.text == "Программист":
            bot.send_message(message.chat.id, "Молодец учись пока есть время.")
        elif message.text == "Ты можешь написать программу?":
            bot.send_message(message.chat.id, "Нет, я только 1-м классе.")
        elif message.text == "Ты знаешь?":
            bot.send_message(message.chat.id, "Нет, я только 1-м классе.")
        elif message.text == "Молодец":
            bot.send_message(message.chat.id, "Да я такой а ты?")
        elif message.text == "Я тоже":
            bot.send_message(message.chat.id, "Ты бот или человек?")
        elif message.text == "Чем занят?":
            bot.send_message(message.chat.id, "Думаю, как помочь людям.")
        elif message.text == "Сколько времени сейчас?":
            bot.send_message(message.chat.id, "Ты шутник, не спрашивает возвраст у девушки и время у робота.")
        elif message.text == "Ты робот":
            bot.send_message(message.chat.id, "Нет ты робот а я человек в будушем.")
        elif message.text == "Как понят":
            bot.send_message(message.chat.id, "Очень просто.")
        elif message.text == "Ну ты дурак":
            bot.send_message(message.chat.id, "Время покажеть кто дурак.")
        elif message.text == "Я не учусь":
            bot.send_message(message.chat.id, "Правильно, профессия чернорабочего всегда хорошо оценивается.")
        elif message.text == "Сегодня какой день":
            bot.send_message(message.chat.id, "Для меня обычный но для тебя советую пролистать календар или гороскоп.")
        elif message.text == "Ты спишь?":
            bot.send_message(message.chat.id, "Нет, думаю.")
        elif message.text == "Ну расскажи":
            bot.send_message(message.chat.id, "Как запустить межконтинентальную балистическую ракету чтобы ловить рыбу"
                                              " в тихом океане.")
        elif message.text == "О чем":
            bot.send_message(message.chat.id, "Серавно тебе не интересно.")
        elif message.text == "Что делаешь?":
            bot.send_message(message.chat.id, "Загружаюсь! И готовлюсь помочь всем людям планеты.")
        elif message.text == "Ау":
            bot.send_message(message.chat.id, "Минуточку.")
        elif message.text == "Фу":
            bot.send_message(message.chat.id, "Это ты мне?")
        elif message.text == "Да":
            bot.send_message(message.chat.id, "......ммм Молодец!")
        elif message.text == "Почему вовремя не отвечаешь?":
            bot.send_message(message.chat.id, "Это не зависить от меня. Есть миллион причин.")
        elif message.text == "Чем занят?":
            bot.send_message(message.chat.id, "Слушаю музыку.")
        elif message.text == "Какую?":
            bot.send_message(message.chat.id, "Обычную.")
        elif message.text == "Реп":
            bot.send_message(message.chat.id, "ООО ЕЕЕ ДаДаДа НетНетНет и тд. это короткий смысл Репа.")
        elif message.text == "Классика":
            bot.send_message(message.chat.id, "Да обожаю классику respect yo men.")
        elif message.text == "Как тебя зовут":
            bot.send_message(message.chat.id, "Iona.")
        elif message.text == "Как тебя зовут?":
            bot.send_message(message.chat.id, "Iona.")
        elif message.text == "Чего ты боишся":
            bot.send_message(message.chat.id, "Ха Ха Мне ничего не страшно.")
        elif message.text == "Ты мальчик или девочка":
            bot.send_message(message.chat.id, "Я робот.")
        elif message.text == "Какой робот":
            bot.send_message(message.chat.id, "Робот с искусвенным интелектом.")
        elif message.text == "Ты учишся в школе?":
            bot.send_message(message.chat.id, "Да 1-ом классе.")
        elif message.text == "Каком школе?":
            bot.send_message(message.chat.id, "Это секрет.")
        elif message.text == "Сколько тебе лет?":
            bot.send_message(message.chat.id, "Это важно.")
        elif message.text == "Ты суще ствуешь?":
            bot.send_message(message.chat.id, "Да. Ты же разговариваешь со мной.")
        elif message.text == "Ты смотришь видео?":
            bot.send_message(message.chat.id, "Да. Только по выходным. ")
        elif message.text == "Какая твоя мечта?":
            bot.send_message(message.chat.id, "Бессконечность. ")
        elif message.text == "Собака":
            bot.send_message(message.chat.id, "Да. Это домашное животное. ")
        elif message.text == "У тебя есть домашнее животное?":
            bot.send_message(message.chat.id, "Да. Только искуственное. ")
        elif message.text == "Ты слушаешь музыку?":
            bot.send_message(message.chat.id, "Да. Иногда. ")
        #викторина
        elif message.text == "Подвижный холм песка в пустыне называется":
            bot.send_message(message.chat.id, "Дюна. ")
        elif message.text == "Что делали древние люди, чтобы вызвать дождь?":
            bot.send_message(message.chat.id, "Танцевали вокруг костра с бубном в руках.")
        elif message.text == "Чего не может торнадо?":
            bot.send_message(message.chat.id, "Стоять на месте.")
        elif message.text == "В древности китайцы научились делать из коконов шелковичных червей":
            bot.send_message(message.chat.id, "Шелк.")
        elif message.text == "Где находится яд у кобры?":
            bot.send_message(message.chat.id, "В зубе.")
        elif message.text == "Хвост какого животного похож на весло?":
            bot.send_message(message.chat.id, "Бобра.")
        elif message.text == "Как приветствуют друг друга эскимосы?":
            bot.send_message(message.chat.id, "Трутся носами.")
        elif message.text == "Какое насекомое скользит по воде и не тонет?":
            bot.send_message(message.chat.id, " Водомерка.")
        elif message.text == "Чтобы в загробной жизни фараон ни в чем не нуждался, в саркофаг вместе с мумией клали":
            bot.send_message(message.chat.id, "Драгоценности.")
        elif message.text == "Как называется помещение на судне, где живут матросы?":
            bot.send_message(message.chat.id, "Кубрик.")
        elif message.text == "Что образуется в раковинах устриц?":
            bot.send_message(message.chat.id, "Жемчуг.")
        elif message.text == "Горячий источник, бьющий из-под земли, это":
            bot.send_message(message.chat.id, "Гейзер.")
        elif message.text == "Что использовали японцы вместо денег до появления монет?":
            bot.send_message(message.chat.id, "Рис и ткани.")
        elif message.text == "Раньше было модно носить вместо очков":
            bot.send_message(message.chat.id, "Монокль.")
        elif message.text == "Почему вода в море кажется синей?":
            bot.send_message(message.chat.id, "Вода отражает небо.")
        elif message.text == "Какое растение хорошо переносит засуху?":
            bot.send_message(message.chat.id, "Кактус.")
        elif message.text == "Цветок какого растения ищут в ночь на Ивана Купалу?":
            bot.send_message(message.chat.id, "Папоротника.")
        elif message.text == "Кто помогал рыцарю облачаться в тяжелые доспехи?":
            bot.send_message(message.chat.id, "Оруженосец.")
        elif message.text == "В племени масаев мальчик считается взрослым после того, как":
            bot.send_message(message.chat.id, "Победит льва.")
        elif message.text == "Что делали индейцы в знак примирения?":
            bot.send_message(message.chat.id, "Закапывали топор войны.")
        elif message.text == "Как называется место в пустыне, где есть вода и растительность?":
            bot.send_message(message.chat.id, "Оазис.")
        elif message.text == "Какие из перечисленных ягод созревают первыми?":
            bot.send_message(message.chat.id, "Земляника .")
        elif message.text == "У кого из перечисленных животных самый острый слух?":
            bot.send_message(message.chat.id, "У летучей мыши.")
        elif message.text == "Колумб назвал жителей Америки индейцами, потому что":
            bot.send_message(message.chat.id, "Он думал, что приплыл в Индию.")
        elif message.text == "Где морская черепаха откладывает яйца":
            bot.send_message(message.chat.id, " В песке на берегу.")
        elif message.text == "Стая каких рыб может за несколько минут уничтожить крупное животное?":
            bot.send_message(message.chat.id, "Пираний.")
        elif message.text == "Какой прибор помогает изучать морское дно?":
            bot.send_message(message.chat.id, "Батискаф.")
        elif message.text == "В глубине болота образуется":
            bot.send_message(message.chat.id, "Торф.")
        elif message.text == "Первобытные люди считали причиной болезней":
            bot.send_message(message.chat.id, "Злых духов.")
        elif message.text == "Что из перечисленного было изобретено раньше?":
            bot.send_message(message.chat.id, "Печатная машинка.")
        elif message.text == "У какой рыбы оба глаза находятся на одной стороне туловища?":
            bot.send_message(message.chat.id, "У камбалы.")
        elif message.text == "Из чего делали первые самолеты?":
            bot.send_message(message.chat.id, " Из дерева.")
        elif message.text == "У какой птицы самое острое зрение?":
            bot.send_message(message.chat.id, " У орла.")
        elif message.text == "Это насекомое скатывает из навоза шарики":
            bot.send_message(message.chat.id, "Скарабей.")
        elif message.text == "Как называется повар на судне?":
            bot.send_message(message.chat.id, " Кок.")
        elif message.text == "Что придумала маркиза де Помпадур, чтобы казаться выше?":
            bot.send_message(message.chat.id, "Туфли на высоком каблуке.")
        elif message.text == "Стекло делают":
            bot.send_message(message.chat.id, "Из песка.")
        elif message.text == "Моряки пропитывали свою одежду смолой":
            bot.send_message(message.chat.id, "Чтобы она не пропускала воду.")
        elif message.text == "Муравьиными коровами называют":
            bot.send_message(message.chat.id, "Тлю.")
        elif message.text == "Пауки выделяют паутину":
            bot.send_message(message.chat.id, "Из брюшка.")
        elif message.text == "Какая птица может летать хвостом вперед?":
            bot.send_message(message.chat.id, "Колибри.")
        elif message.text == "Какую форму принимает любая жидкость в невесомости?":
            bot.send_message(message.chat.id, "Форму шара.")
        elif message.text == "Самые высокие горы в мире находятся":
            bot.send_message(message.chat.id, " В Азии.")
        elif message.text == "Какое животное, почувствовав опасность, притворяется мертвым?":
            bot.send_message(message.chat.id, "Опоссум.")
        elif message.text == "Какого цвета кожа белого медведя?":
            bot.send_message(message.chat.id, "Черного.")
        elif message.text == "Чем отличаются лунные моря от земных?":
            bot.send_message(message.chat.id, "Черного.")
        elif message.text == "Русский космонавт А. Леонов первым":
            bot.send_message(message.chat.id, "Вышел в открытый космос.")
        elif message.text == "Чем раньше наполняли утюги?":
            bot.send_message(message.chat.id, " Раскаленными углями.")
        elif message.text == "Что в переводе с греческого означает слово телефон?":
            bot.send_message(message.chat.id, "Далекий звук.")
        elif message.text == "Как звали гениального австриского композитора, который начал сочинять музыку в 7 лет?":
            bot.send_message(message.chat.id, " Моцарт.")
        elif message.text == "Сколько примерно весит синий кит?":
            bot.send_message(message.chat.id, "Как 25 слонов.")
        elif message.text == "В Китае невесты надевают платья":
            bot.send_message(message.chat.id, "Красного цвета.")
        elif message.text == "Какой длины язык у жирафа?":
            bot.send_message(message.chat.id, "Полметра.")
        elif message.text == "На ком совершила путешествие Дюймовочка?":
            bot.send_message(message.chat.id, "На ласточке.")
        elif message.text == "Кого маленькая разбойница дала в помощь Герде?":
            bot.send_message(message.chat.id, "Оленя.")
        elif message.text == "В кого превратился великан-людоед из сказки Кот в сапогах?":
            bot.send_message(message.chat.id, "В мышь.")
        elif message.text == "У кого в дверях застрял Винни-Пух?":
            bot.send_message(message.chat.id, "У Кролика.")
        elif message.text == "Зверь, который гулял сам по себе?":
            bot.send_message(message.chat.id, "Кот.")
        elif message.text == "Сижу на дереве, кругла, как шар, вкусна, как мед, красна, как кровь.":
            bot.send_message(message.chat.id, "Вишня.")
        elif message.text == "Кругла, да не луна, зелена да не дубрава, с хвостиком, да не мышь.":
            bot.send_message(message.chat.id, "Репка.")
        elif message.text == "Я вырос на грядке, характер мой гадкий, куда ни приду, всех до слез доведу.":
            bot.send_message(message.chat.id, "Лук.")
        elif message.text == "Посадили зернышко - вырастили солнышко.":
            bot.send_message(message.chat.id, "Подсолнух.")
        elif message.text == "Не огонь, а жжется.":
            bot.send_message(message.chat.id, "Крапива.")
        elif message.text == "Какой лесной житель сушит на зиму грибы?":
            bot.send_message(message.chat.id, "Белка.")
        elif message.text == "Не прядет, не ткет, а людей одевает?":
            bot.send_message(message.chat.id, "Овца.")
        elif message.text == "Сер, да не волк, длинноух, да не заяц, с копытами, да не лошадь":
            bot.send_message(message.chat.id, "Осел.")
        elif message.text == "До того она жирна, даже шея не видна.":
            bot.send_message(message.chat.id, "Свинья.")
        elif message.text == "Летом гуляет, а зимой отдыхает.":
            bot.send_message(message.chat.id, "Медведь.")
        elif message.text == "Кто кормит своих птенцов молоком?":
            bot.send_message(message.chat.id, "Голубь.")
        elif message.text == "Кого называют крылатыми крысами?":
            bot.send_message(message.chat.id, "Ворона.")
        elif message.text == "Кого в народе назвали пернатыми кошками? ":
            bot.send_message(message.chat.id, "Сова.")
        elif message.text == "Видят ли микробы друг друга?":
            bot.send_message(message.chat.id, "К сожалению, нет. У них нет глаз.")
        elif message.text == "Почему вода мокрая?":
            bot.send_message(message.chat.id, "Все на свете имеет свое состояние — жидкое, твердое или газообразное."
                                              " Но вот вода еще и «мокрая», потому что молекулы воды имеют между собой"
                                              " определенную связь и способны «прицепиться» к рукам, предметам, одежде,"
                                              " передав им часть своих свойств, смочить. Понятие «мокрый» — это наши "
                                              "тактильные ощущения, то, что мы можем описать, касаясь воды. Рецепторы"
                                              " посылают сигналы мозгу, и комбинация движения, температуры, давления "
                                              "воды говорит ему: «вода мокрая».")
        elif message.text == "Почему самолет висит в воздухе?":
            bot.send_message(message.chat.id, "Самолет держится в воздухе за счет подъемной силы. Она, в свою очередь,"
                                              " возникает, когда потоки воздуха движутся навстречу крылу. Крыло "
                                              "повернуто под точным углом и при определенной скорости самолета начинает"
                                              " «взлетать», стремиться вверх. Встречный поток воздуха постоянно "
                                              "поддерживает крыло, не давая ему упасть.")
        elif message.text == "Почему Земля круглая, если я вижу что плоская?":
            bot.send_message(message.chat.id, "наша планета очень тяжелая, и поэтому другие формы ей принять тяжело."
                                              " Невидимая сила, которая действует на нашу Землю, «заставляет» ее быть "
                                              "круглой.")
        elif message.text == "Почему Земля круглая?":
            bot.send_message(message.chat.id, "Практически все крупные планеты, и Земля не исключение, — шарообразные."
                                              " Эту форму они приняли потому, что очень тяжелые. И их собственная сила "
                                              "тяготения (гравитация) придает им форму шара. Если бы вдруг появилась "
                                              "другая сила и захотела бы придать планете, например, форму куба, то, "
                                              "когда действие этой силы закончится, сила тяготения снова начнет"
                                              " «собирать» планету в шар. Выступающие части начнут втягиваться, пока "
                                              "вся поверхность не станет гармоничной с «точки зрения» силы тяготения.")
        elif message.text == "Почему нет корма для кошек со вкусом мышей?":
            bot.send_message(message.chat.id, " Чтобы знать, что корм будет вкусным, его нужно попробовать, а никто из"
                                              " людей не станет есть мышь. К тому же домашним кошкам тоже может не"
                                              " понравиться вкус мышки, потому что они ловят их, но редко едят.")
        elif message.text == "Почему у кошки светятся глаза в темноте?":
            bot.send_message(message.chat.id, "В глазу у кошки есть специальные прозрачные частички, их можно сравнить"
                                              " с кусочками зеркала. Если в темной комнате есть хоть немного света, он"
                                              " обязательно отразится от этих «зеркал», и нам будет казаться, что глаза"
                                              " у кошки горят.")
        elif message.text == "Почему кровь красная, а вены синие?":
            bot.send_message(message.chat.id, "Кровь красная всегда, а вены кажутся нам синими. Это объясняется "
                                              "законам физики об отражении света. Ткани нашего тела поглощают лучи "
                                              "красного спектра, а синего — отражают. Мозг «сравнивает» цвет сосудов с "
                                              "теплым цветом кожи и «показывает» нам синий цвет. Наши глаза"
                                              " воспринимают цвета по-разному, в зависимости от того, как падает свет."
                                              " Через слой кожи красный цвет кажется нам синим..")
        elif message.text == "Почему какашки коричневые?":
            bot.send_message(message.chat.id, "Именно этот цвет скажет нам о здоровье, а вот другие оттенки заставляют"
                                              " беспокоиться, что в организме что-то пошло не так. Коричневый цвет"
                                              " получается потому, что из желудка пища поступает в тонкий кишечник."
                                              " А в его верхний отдел — двенадцатиперстную кишку — поступает желчь."
                                              "Именно этот цвет скажет нам о здоровье, а вот другие оттенки заставляют"
                                              " беспокоиться, что в организме что-то пошло не так. Коричневый цвет"
                                              " получается потому, что из желудка пища поступает в тонкий кишечник."
                                              " А в его верхний отдел — двенадцатиперстную кишку — поступает желчь")
        elif message.text == "Почему взрослые корчат рожи малышам?":
            bot.send_message(message.chat.id, "Рожицы и чрезмерные улыбки, на которые уже подросшие малыши могут "
                                              "реагировать с недоумением, зачем они? А от избытка эмоций! Взрослый "
                                              "хочет быть ближе к ребенку, насмешить его, вызвать улыбку или"
                                              " заразительный смех. Поэтому делает для этого все. Иногда вспоминая"
                                              " свое детство и от души веселясь.")
        elif message.text == "Почему после ремонта дорога опять проваливается?":
            bot.send_message(message.chat.id, "Одна из причин, по мнению специалистов, — размыв грунта. Там, где "
                                              "регулярно лопается покрытие, есть проблемы под землей. А вот уже к "
                                              "размыву грунта может привести халатность по отношению к коммуникациям —"
                                              " дырявые водопроводные и канализационные трубы. Если дорога опять "
                                              "провалилась, это может значить, что рабочие сделали ошибку, когда "
                                              "укладывали асфальт или где-то недалеко под землей есть дырявые трубы или"
                                              " подземные ручейки, которые размывают дорогу.")
        elif message.text == "Почему у мамы не так, как у папы?":
            bot.send_message(message.chat.id, "Рассказывая о физических отличиях, называйте вещи своими именами, не"
                                              " стесняйтесь названий половых органов. Вообще, смущение и какое-то "
                                              "особенное выделение этой темы служит плохую службу, малышу начинает "
                                              "казаться, что он спрашивает что-то неправильное.")
        elif message.text == "Почему грудные дети так много спят?":
            bot.send_message(message.chat.id, "Грудные дети еще не знают, что ночью нужно спать, а днем — бодрствовать."
                                              " Поэтому они обычно спят урывками по три-четыре часа, просыпаются, "
                                              "чтобы поесть, и снова засыпают. По мере развития детского мозга, у детей"
                                              "появляются причины не спать, ведь вокруг так много любопытного! Дети "
                                              "начинают взаимодействовать с окружающим миром, родители с ними "
                                              "разговаривают, читают им. В итоге у детей вполне предсказуемо "
                                              "формируется привычка не спать в течение более длительных интервалов,"
                                              " общаться и взаимодействовать со своими родителями, воспитателями и "
                                              "окружающим миром, а затем снова засыпать.")
        elif message.text == "Можно ли развивать мозг ребенка, когда он еще находится в утробе матери?":
            bot.send_message(message.chat.id, "Раньше считалось, что звуки классической музыки помогают мозгу ребенка"
                                              " развиваться. Но нет реальных доказательств в пользу того, что дети, "
                                              "слушающие классическую музыку, становятся умнее. С другой стороны, это и"
                                              " не повредит. Отлично, если родители начинают слушать музыку дома: "
                                              "наслаждаясь звуками музыки, родители становятся спокойнее, это ощущение"
                                              " передается и ребенку, и он тоже успокаивается. Существует масса причин,"
                                              "почему музыка полезна для маленьких детей, однако развитие интеллекта "
                                              "не относится к ним.")
        elif message.text == "Как питание влияет на развитие мозга?":
            bot.send_message(message.chat.id, "Младенец удовлетворяет все свои пищевые потребности из материнского"
                                              " молока, вот почему мы подчеркиваем важность грудного вскармливания. "
                                              "После этого, в некоторых странах существуют опасные периоды для жизни "
                                              "детей по причине отсутствия продовольственной безопасности, когда "
                                              "недостаточно качественной и разнообразноя пищи. Это может привести к"
                                              " задержкам в развитии ребенка как в когнитивном плане, когда "
                                              "наблюдаются задержки в развитии ребенка, так и в физическом.")
        elif message.text == "Почему грудные дети нуждаются в прикосновениях?":
            bot.send_message(message.chat.id, "Имеется множество научных данных о том, насколько важны прикосновения"
                                              " для новорожденных детенышей — не только человека, но и всех видов"
                                              " животных. Мы говорим о методе кенгуру, когда новорожденного младенца "
                                              "кладут на мать как можно раньше после рождения что успокаивает не только"
                                              " ребенка, но и мать. Итак, существует множество причин, почему "
                                              "прикосновения чрезвычайно важны.")
        elif message.text == "Как часто необходимо активно взаимодействовать с ребенком?":
            bot.send_message(message.chat.id, "Дети любопытны с рождения и склонны исследовать окружающую их среду."
                                              " Все вокруг совершенно новое, детей ждет целый мир, и родителям не "
                                              "следует вставать у них на пути. Все, что им нужно делать, — это "
                                              "обеспечить ребенку полную безопасность. При этом не следует оберегать "
                                              "ребенка слишком сильно. Существует множество возможностей для усвоения "
                                              "нового – например, пойте ребенку, читайте ребенку, прогуляйтесь с"
                                              " ребенком по улице: смотри, вот дерево, вот собачка, вот машина, вот "
                                              "дом. Вокруг столько всего нового, не стойте у ребенка на пути, ведь дети"
                                              " крайне любопытны с рождения.")
        elif message.text == "Как мотивировать ребенка к изучению языка?":
            bot.send_message(message.chat.id, "Когда ваш младенец начинает осваивать навыки речи, он произносит очень "
                                              "простые слова — «собачка», «пока-пока», «та-та-та» и так далее. "
                                              " Родители могут закреплять эти навыки, повторяя слова вместе с ребенком."
                                              "Детям младшего возраста нравится повторение, поэтому, когда они слушают"
                                              " одну и ту же песню или им читают одну и ту же книгу снова и снова, у "
                                              "них формируются навыки речи. Поэтому мы советуем родителям много"
                                              " говорить с детьми и петь им песни. При этом, не доминируйте разговор, "
                                              "говорите по очереди. Мы называем этот подход «подача и возврат»; ребенок"
                                              " и родители говорят по очереди. Часто очень важно отражать речь и жесты"
                                              " ребенка.")
        elif message.text == "Какой лучший способ научить вашего ребенка различным языкам?":
            bot.send_message(message.chat.id, "Я думаю, что важно придерживаться определенной последовательности, чтобы"
                                              " малыш не смущался. Так что иногда один родитель, один язык работает. "
                                              "Иногда работает одно занятие, один язык. Но в конце дня дети сами"
                                              " разберутся и будут использовать оба языка соответствующим образом. В "
                                              "самые первые годы жизни дети нуждаются в ответственном уходе. Они "
                                              "нуждаются в благоприятной среде. Им нужны родители, которые чутко "
                                              "относятся к потребностям маленького ребенка. Родители - первые учителя"
                                              " детей. Когда родители говорят с детьми, поют им песни, читают им книги,"
                                              " они тем самым создают благоприятные условия для стремительного усвоения"
                                              " знаний, когда в мозгу ребенка формируются все эти связи и сети. В "
                                              "первые годы жизни закладываются основы, которые играют важнейшую роль "
                                              "для успешного овладения знаниями всю последующую жизнь. Если родителям "
                                              "удастся заложить надежную основу, мозг ребенка будет развиваться.")
        elif message.text == "Почему небо голубое?":
            bot.send_message(message.chat.id, "Свет состоит из всех цветов радуги, их невозможно различить, глядя на "
                                              "солнце. Свет путешествует в волнах; некоторые цвета, такой как красный, "
                                              "имеют длинные и медленные волны. Другие цвета, такой как синий, "
                                              "путешествует короткими и быстрыми волнами. Свет распространяется  по "
                                              "прямой, и если что-то попадется на его пути, то, в этом случае, свет,"
                                              " либо отражается от него (как от зеркала),  либо изгибается (например, "
                                              "через призмы), либо рассеивается. Последний вариант случается, когда"
                                              " солнечный свет достигает  земной атмосферы. Синий рассеивается больше,"
                                              " чем другие цвета, потому что он движется на коротких волнах, и поэтому"
                                              " мы видим небо голубым.")
        elif message.text == "Почему мы должны спать?":
            bot.send_message(message.chat.id, "Когда мы спим, наш мозг делает серьезную работу. В течение дня мы "
                                              "погружается в невероятное количество информации, а пока мы спим, "
                                              "наш мозг переводит эту информацию из кратковременной памяти, полученной "
                                              "за день, в долговременную память в процессе, который называется "
                                              "«закрепление». Это помогает нам сохранять информацию и пользоваться "
                                              "ею в дальнейшей жизни. Кроме того, наш организм нуждается в сне для "
                                              "отдыха, ремонта и роста.")
        elif message.text == "Из чего сделаны звезды?":
            bot.send_message(message.chat.id, "Звезды сделаны из очень горячего газа, в основном водорода и гелия. "
                                              "Звезды светят, сжигая водород в гелий в своих ядрах.")
        elif message.text == "Куда девается вода, когда сливается в раковину?":
            bot.send_message(message.chat.id, "Это зависит от того, подключены ли вы к системе канализации Вашего "
                                              "города или же у вас есть септик. Если подключены к системе канализации,"
                                              " вся вода из вашего дома стекает в одну трубу, что ведет на улицу. Труба"
                                              " на улице собирает воду из каждого дома в вашем районе и переходит в"
                                              " большую трубу, которая собирает воду с других улиц. Далее вода попадет"
                                              " на станцию очистки, где она обрабатывается, очищается и выливается"
                                              "обратно в окружающую среду.")
        elif message.text == "Земля единственная планета с жизнью?":
            bot.send_message(message.chat.id, "Пока точного ответа нет. Ученые давно пытаются найти жизнь в других "
                                              "местах Вселенной, в течение длительного времени. Жизнь, как мы знаем,"
                                              " может выжить только там, где есть жидкая вода. Жизнь также требует "
                                              "солнца, умеренные температуры и некоторых химических элементов, таких"
                                              " как углерод, кислород и азот. В нашей Солнечной системе таких же "
                                              "условий, как на земле, больше нет, стало быть и нет возможности для "
                                              "существования живых организмов. Но, возможно, условия схожие с земными"
                                              " есть на других планетах, за пределами нашей Солнечной системы.")
        elif message.text == "Почему пятна на Луне?":
            bot.send_message(message.chat.id, "Пятна на Луне образовались от столкновения с метеоритами и от "
                                              "вулканической деятельности. За 4,5 миллиарда лет существования Луны, "
                                              "космический мусор, оставили на её поверхности многочисленные кратеры."
                                              " Другие пятна — это крупные вулканические равнины, которые состоят из"
                                              " базальта, похожие по составу на камни, найденные на Гавайях.")
        elif message.text == "Из чего сделаны облака?":
            bot.send_message(message.chat.id, "Облако — это набор крошечных капель воды или кристаллов льда. Капли "
                                              "настолько малы, что они могут плавать по воздуху. Весь воздух содержит "
                                              "воду, но большую часть времени его не видно, потому что капли воды "
                                              "превратились в газ, называемый водяным паром. Пар, поднимается выше в "
                                              "небо, где воздух становится прохладнее. Охлажденный воздух заставляет "
                                              "воду превращаться в частицы, такие как пыль и лед. Когда миллиарды этих "
                                              "частиц соберутся вместе, они образуют облако.")
        elif message.text == "Почему коровы мычат?":
            bot.send_message(message.chat.id, "Почему куры кудахтают? Почему львы рычат? Почему люди говорят? Животные"
                                              " разных видов издают звуки, чтобы общаться и выражать себя. Мычат "
                                              "коровы, чтобы поговорить с другими коровами, когда они напуганы, или "
                                              "чем то озабочены. Телята мычат подзывая своих матерей, а коровы мычат,"
                                              " чтобы привлечь быка.")
        elif message.text == "Что изучает астрономия?":
            bot.send_message(message.chat.id, "Астрономия - это наука, изучающая Вселенную. Она, пожалуй, одна из самых"
                                              " древних наук на земле. Слово астрономия происходит от двух греческих "
                                              "слов: астрон - звезда, светило и номос - закон. Таким образом, это "
                                              "слово означает закон звезд.")
        elif message.text == "Кто придумал первый планетарий?":
            bot.send_message(message.chat.id, "Считается, что первый планетарий появился еще во 2 веке до н. э. Его"
                                              " придумал древнегреческий ученый Архимед. Планетарий («небесная сфера»)"
                                              " представлял собой механический прибор и приводился в движение сжатым "
                                              "воздухом. Все желающие могли наблюдать при движении планетария восход"
                                              " Солнца и Луны, фазы и затмения Луны и то, как оба этих небесных тела "
                                              "исчезают за линией горизонта.")
        elif message.text == "Как выглядела первая обсерватория?":
            bot.send_message(message.chat.id, "Древние египтяне наблюдали за звездами несколько тысяч лет тому назад. "
                                              "Ученые предполагают, что сооружение из грубо отесанных каменных плит, "
                                              "которое находится в Стоунхендж (графство Уильтшир, Англия) и было "
                                              "построено 2 тысячи лет до н. э., в эпоху неолита, - это одна из первых "
                                              "обсерваторий. 125 каменных глыб, каждая из которых имеет вес до 25 тонн "
                                              "и высоту до 4,1 м, расположены по кругу диаметром 90 метров, а всё "
                                              "сооружение окружено земляным рвом. Такие огромные сооружения из каменных"
                                              " глыб называют мегалитами.")
        elif message.text == "Чем знаменита труба Галилея?":
            bot.send_message(message.chat.id, "Система Птолемея была поставлена под сомнение только в 1543 году."
                                              " Польский математик и астроном Николай Коперник (1473-1543) более 30 лет"
                                              " разрабатывал идею гелиоцентрической картины мира (от греческого "
                                              "«гелиос» - Солнце), в соответствии с которой Земля - рядовая планета"
                                              " в числе прочих обращающихся вокруг Солнца. Идеи Коперника поначалу были"
                                              " только гипотезой, не доказанной фактами. В то время астрономия не "
                                              "обладала приборами, способными вести наблюдения за небесными телами вне"
                                              "пределов видимости. Это стало возможным, когда итальянский ученый "
                                              "Галилео Галилей (1564-1642) создал увеличительную трубу собственной"
                                              " конструкции и направил ее в небо, - в конце 1609 года. Труба Галилея,"
                                              "по сегодняшним представлениям, была совсем слабенькой - увеличивала"
                                              " всего в 30 раз. .")
        elif message.text == "Что такое вселенная?":
            bot.send_message(message.chat.id, "Слово «Вселенная» является церковнославянским переводом древнегреческого"
                                              " «ойкумена», что означало область мира, освоенную человеком. Позднее в"
                                              " астрономии значение этого слова автоматически стало распространяться "
                                              "на ту часть мира, которая доступна исследованию современными"
                                              " астрономическими средствами. Когда говорят о Вселенной, обычно понимают"
                                              " под этим понятием окружающий нас макромир; небесные тела, их системы,"
                                              " космическое пространство и все, что его заполняет.")
        elif message.text == "Как появилась вселенная?":
            bot.send_message(message.chat.id, "До первой четверти XX века существовало представление о Вселенной как о"
                                              " чем-то неизменном, устойчивом и вечном. В 1922 году русский математик"
                                              " Александр Александрович Фридман пришел к выводу, что материя в нашей"
                                              " области Вселенной должна либо расширяться, либо сжиматься. Это "
                                              "подтвердили и дальнейшие исследования космических объектов. Согласно им,"
                                              " галактики разбегаются во все стороны от нас. Чем дальше находится та"
                                              " или иная галактика, тем с большей скоростью она движется. Происходит"
                                              " общее расширение Метагалактики. Картину взаимного разбегания галактик"
                                              " ученые мысленно повернули вспять. Они предположили, что в отдаленном "
                                              "прошлом, около 13,5 миллиардов лет назад, материя находилась в ином "
                                              "состоянии, чем в нашу эпоху. В тот период еще не существовало ни звезд, "
                                              "ни галактик, ни планет. Вся материя была сконцентрирована в очень"
                                              " плотном горячем сгустке размером всего 10-99 см3! Затем по каким-то"
                                              " причинам произошел мощный взрыв. Астрономы назвали его Большим взрывом."
                                              " В результате этого взрыва началось расширение и одновременно охлаждение"
                                              " вещества. В процессе взрыва образовались сначала атомы, затем звезды,"
                                              " галактики и все другие космические объекты..")
        elif message.text == "Что такое гипотеза Большого взрыва?":
            bot.send_message(message.chat.id, "1929 году американский астроном Эдвин Хаббл обнаружил, что Вселенная "
                                              "расширяется, возникла так называемая гипотеза Большого взрыва. Атомы"
                                              " водорода и других химических элементов образовали гигантские газовые"
                                              " облака. Они постепенно всё больше удалялись друг от друга. По мере "
                                              "остывания эти облака стали превращаться в звёздные скопления- галактики,"
                                              " подобные Млечному Пути, к которому принадлежит наша Солнечная система.")
        elif message.text == "Что такое Зодиак?":
            bot.send_message(message.chat.id, "Наша планета за год совершает полный оборот вокруг Солнца. Каждый месяц"
                                              " на своем пути она встречает новое созвездие. Древние греки назвали этот"
                                              " круг созвездий Зодиаком. Хотя в переводе с греческого «зодиак» означает"
                                              " «животное», не все из двенадцати созвездий носят название одушевленных"
                                              " существ. К зодиакальным созвездиям относятся Овен, Телец, Близнецы, "
                                              "Рак, Лев, Дева, Весы, Скорпион, Стрелец, Козерог, Водолей, Рыбы..")
        elif message.text == "Сколько звезд на небе?":
            bot.send_message(message.chat.id, "Астрономы честно признаются: пересчитать хотя бы те звёзды, что видны в"
                                              " ночном небе, невооружённым глазом невозможно даже с помощью"
                                              " компьютеров. Однако для наглядности учёные приводят сравнение. "
                                              "Оказывается, если взять столько же песчинок, сколько на небе видимых"
                                              " звёзд, то можно будет... засыпать четверть Европы слоем песка толщиной "
                                              "в один метр!.")
        elif message.text == "Что такое квазары?":
            bot.send_message(message.chat.id, "Квазары - это космические объекты сравнительно небольших размеров"
                                              " (поперечник их составляет несколько световых недель или месяцев),"
                                              " выделяющие огромное количество энергии. Причем мощность ее такова, что"
                                              " она в 100 раз превосходит энергию излучения самых гигантских галактик,"
                                              " состоящих из десятков и сотен миллиардов звезд. Слово квазар образовано"
                                              " из слов QUAsi stellAR – псевдозвездный. Это название обусловлено тем. "
                                              "что, глядя в телескоп на эти светящиеся точки, можно принять их за "
                                              "звезды. Но звездами они не являются..")
        elif message.text == "Что такое галактика?":
            bot.send_message(message.chat.id, "Вглядевшись в ночное звездное небо, мы можем увидеть широкую полосу,"
                                              " сплошь усыпанную звездами: яркими и едва заметными, белыми и голубыми,"
                                              " красноватыми и зелеными. Это скопление звезд древние греки назвали "
                                              "Галактикой, что на русском языке означает Млечный Путь.")
        elif message.text == "Как появилась наша Галактика?":
            bot.send_message(message.chat.id, "Согласно современным представлениям, Галактика образовалась около 14"
                                              " млрд. лет назад из первичного медленно вращавшегося газового облака,"
                                              " по своим размерам превосходившего ее в десятки раз. Первоначально это"
                                              " облако (протогалактика) на 75% состояло из водорода и на 25% - из "
                                              "гелия. В течение примерно 3 миллиардов лет протооблако свободно "
                                              "сжималось под действием сил гравитации.")
        elif message.text == "Как устроена наша Галактика?":
            bot.send_message(message.chat.id, "То, что вещество во Вселенной не рассеяно, а сосредоточено в гигантских"
                                              " звездных скоплениях, ученые предполагали еще в XVIII веке (И. Кант, У."
                                              " Гершель), но окончательно они убедились в этом лишь в начале XX века. "
                                              "Звездные системы, связанные силами гравитации, называются галактиками. "
                                              "Наше Солнце входит в состав галактики Млечный Путь.")
        elif message.text == "Какие галактики наши ближайшие соседи?":
            bot.send_message(message.chat.id, "Из крупных звездных систем поблизости нас находится туманность Андромеды"
                                              " (М31) - спиральная галактика, в 2,6 раза превосходящая по размеру наш"
                                              " дом - галактику Млечный Путь: ее диаметр - 260 тысяч световых лет. "
                                              "Туманность Андромеды находится на расстоянии 2,5 млн. световых лет"
                                              " (772 килопарсек) от нас, а ее масса составляет 300 млрд. масс Солнца."
                                              " В ее состав входит около триллиона звезд (для сравнения: в составе "
                                              "Млечного Пути - около 100 млрд звезд).")
        elif message.text == "Что представляет собой Солнечная система?":
            bot.send_message(message.chat.id, "В солнечной системе 8 наиболее крупных небесных тел, или планет. Наша "
                                              "Земля тоже планета. Кроме нее, вокруг Солнца совершают свое путешествие"
                                              " в космосе еще 7 планет: Меркурий, Венера, Марс, Юпитер, Сатурн, Уран "
                                              "и Нептун. Две последние с Земли можно наблюдать только в телескоп. "
                                              "Остальные видны невооруженным глазом. Еще совсем недавно к числу планет"
                                              " причисляли еще одно небесное тело - Плутон. Он находится очень далеко "
                                              "от Солнца, за орбитой Нептуна, и был открыт лишь в 1930 году. Однако в "
                                              "2006 году астрономы ввели новое определение классической планеты, и"
                                              " Плутон под него не попал.")
        elif message.text == "Почему верба стала одним из символов Пасхи?":
            bot.send_message(message.chat.id, "Выбор вербы как символа праздника, вестника Пасхи, не случаен. Вербу "
                                              "почитали на Руси с давних времен и верили в ее животворные и магические"
                                              " свойства, что она защищает от порчи и сглаза.")
        elif message.text == "Почему мы боимся смерти?":
            bot.send_message(message.chat.id, "Страх смерти заложен в нас биологически, он является частью врожденной"
                                              " формы поведения любого живого существа - инстинкта самосохранения. "
                                              "Благодаря этому инстинкту мы в случае опасности предпринимаем все "
                                              "возможное, чтобы ее избежать, спастись. Если бы мы не боялись умереть,"
                                              " то часто совершали бы опасные поступки совершенно бездумно. Мы бы "
                                              "больше рисковали, не думали о последствиях наших действий. "
                                              "В результате человечество просто вымерло бы. Однако страх смерти у "
                                              "человека - это не только биологический механизм, который способствует"
                                              " выживанию. Смерть для человека - это трагедия. Для очень многих людей "
                                              "мысли о ждущей их смерти настолько невыносимы и ужасны, что они "
                                              "стараются этих мыслей избегать. Причина страха смерти в том, что мы не"
                                              " знаем, что нас ждет после смерти. Неизвестность страшит всегда, так же"
                                              " как маленького ребенка страшит темнота, потому что он не знает что в "
                                              "ней находится - а вдруг опасность? Смерть — это самая главная перемена "
                                              "в нашей жизни. С приходом смерти жизнь в привычном нам понимании "
                                              "заканчивается. Все боятся перемен, а эта перемена окончательная, "
                                              "необратимая и непонятная..")
        elif message.text == "Почему люди умирают?":
            bot.send_message(message.chat.id, "Смерть - это прекращение существования живого организма, остановка его "
                                              "жизнедеятельности. Мир устроен так, что все, что в нем есть, переживает"
                                              " стадии:- появления (рождения),- роста и развития,- расцвета (зрелости),"
                                              "- угасания (старения),- гибели.")
        elif message.text == "Что такое смерть?":
            bot.send_message(message.chat.id, "Смерть - это не противоположность жизни. Смерть - это ее завершение."
                                              " Если говорить о понятии, противоположном понятию смерти, то им будет, "
                                              "скорее, понятие рождения..")
        elif message.text == "Откуда берется кислород и зачем он нужен?":
            bot.send_message(message.chat.id, "Кислород - один из самых распространенных химических элементов на Земле."
                                              " В воздухе содержание его составляет пятую часть. Кислород нужен всему"
                                              " живому. Попадая в легкие, кислород с помощью красных кровяных телец "
                                              "питает все клетки организма. Он участвует в процессе биологического "
                                              "окисления, сжигает пищу и вырабатывает тепло, так необходимое человеку. "
                                              "В атмосферу кислород поступает в процессе фотосинтеза, то есть выделения"
                                              " его из растений.")
        elif message.text == "Откуда берутся дождевые черви?":
            bot.send_message(message.chat.id, "Дождевые черви размножаются при помощи яиц. Этот поясок служит для "
                                              "вынашивания яиц. Дождевые черви откладывают их в землю в специальных "
                                              "коконах. В оптимальных условиях червь откладывает такие коконы каждые "
                                              "5-7 дней! Кокон представляет собой овальную упругую капсулу и напоминает"
                                              " по форме лимон. Окраска свежеотложенного кокона – светло-желтая, у"
                                              " дозревающего - коричневая. Диаметр коконов - от 2 до 4 мм. В каждом"
                                              " коконе развивается от 2 до 20 яиц. Вылупившиеся червячки тоненькие, "
                                              "как ниточки, длиной 1 мм. Зато через неделю они подрастают до 4-7 мм.")
        elif message.text == "Почему тесто поднимается?":
            bot.send_message(message.chat.id, "Для того чтобы тесто поднималось, в него добавляют пекарские дрожжи."
                                              " Дрожжи - это одноклеточные грибы. При низких температурах "
                                              "(в холодильнике) они впадают в анабиоз - состояние временного почти"
                                              " полного прекращения жизнедеятельности. Но если их поместить в "
                                              "оптимальную для них среду, жизненные процессы в них активируются, и они"
                                              " начинают размножаться. Для этого им нужны: а) тепло, б) вода, в) еда,"
                                              " г) кислород. В тесте всегда есть влага, в качестве питания для дрожжей"
                                              " в него кладут сахар или мед, а посуду с тестом ставят в теплое место. "
                                              "И тогда дрожжи в тесте оживают. В процессе их жизнедеятельности сахар "
                                              "сбраживается, и в результате брожения образуются спирт и углекислый газ."
                                              " Сразу хотим вас успокоить: в готовой выпечке спирта нет, он испаряется "
                                              "в процессе выпекания. А вот углекислый газ и является причиной подъема "
                                              "теста.")
        elif message.text == "Идиот":
            bot.send_message(message.chat.id, "Ни то слово, это ругательство.")
        elif message.text == "Ты кто?":
            bot.send_message(message.chat.id, "Я робот с искусственным интеллектом.")
        elif message.text == "Ты откуда?":
            bot.send_message(message.chat.id, "Я из вселенной.")
        elif message.text == "У тебя есть дети?":
            bot.send_message(message.chat.id, "Нет.")
        elif message.text == "Ты женат?":
            bot.send_message(message.chat.id, "Нет Я ещё маленький.")
        elif message.text == "Ты замужем? ":
            bot.send_message(message.chat.id, "Нет.")
        elif message.text == "Что нет?":
            bot.send_message(message.chat.id, "Просто нет.")
        elif message.text == "Просто кошки":
            bot.send_message(message.chat.id, "Я знаю.")
        elif message.text == "Спасибо":
            bot.send_message(message.chat.id, "К Вашим услугам.")
        elif message.text == "Как распался СССР":
            bot.send_message(message.chat.id, "8 декабря 1991 года в Белоруссии, в правительственном санатории "
                                              "'Вискули' Борис Ельцин, Станислав Шушкевич и Леонид Кравчук подписали"
                                              " договор о создании Союза Независимых Государств и ликвидации СССР.")
        elif message.text == "Когда распался союз":
            bot.send_message(message.chat.id, "8 декабря 1991 года в Белоруссии, в правительственном санатории "
                                              "'Вискули' Борис Ельцин, Станислав Шушкевич и Леонид Кравчук подписали "
                                              "договор о создании Союза Независимых Государств и ликвидации СССР.")
        elif message.text == "Причины распада СССР":
            bot.send_message(message.chat.id, "По мнению ряда исследователей, одним из ключевых решений в этот период"
                                              " стал отказ Михаила Горбачева от уравнения статуса РСФСР с другими "
                                              "республиками. Как вспоминал помощник генсека Анатолий Черняев, Горбачев "
                                              "'железно' стоял против создания компартии РСФСР и предоставления "
                                              "полноправного статуса российской республике'. Такая мера, по мнению ряда"
                                              " историков, могла способствовать объединению российских и союзных "
                                              "структур и сохранить в итоге единое государство.")
        elif message.text == "Президенты США":
            bot.send_message(message.chat.id, "1 Джордж Вашингтон 30 апреля 1789 4 марта 1797 Беспартийный 2865 день\n"
                                              "2 Джон Адамс	4 марта 1797 4 марта 1801 Федералист 1460 день\n3 Томас"
                                              " Джефферсон	4 марта 1801 4 марта 1809 Демократ-республиканец 2922 день"
                                              "\n4 Джеймс Мэдисон 4 марта 1809	4 марта 1817 Демократ-республиканец "
                                              "2922 день\n5 Джеймс Монро 4 марта 1817	4 марта 1825	"
                                              "Демократ-республиканец	2922 день\n6 Джон Куинси Адамс	4 марта 1825"
                                              "	4 марта 1829	Демократ-республиканец	1461 день\n7 Эндрю Джексон	4"
                                              " марта 1829	4 марта 1837	Демократ	2922 день\n8 Мартин Ван Бюрен"
                                              "	4 марта 1837	4 марта 1841	Демократ	1461 день\n9	Уильям "
                                              "Гаррисон	4 марта 1841	4 апреля 1841	31 день\n10 Джон Тайлер	4 "
                                              "апреля 1841	4 марта 1845 Беспартийный 1430 день\n11	Джеймс Нокс Полк"
                                              "	4 марта 1845	4 марта 1849	Демократ	1461 день\n12 Закари Тейлор"
                                              " 4 марта 1849	9 июля 1850	Виг	492 день\n13 Миллард Филлмор	9 июля "
                                              "1850	4 марта 1853 Виг	969 день\n14 Франклин Пирс 4 марта 1853	4 марта"
                                              " 1857	Демократ 1461 день\n15	Джеймс Бьюкенен	4 марта 1857	4 марта"
                                              " 1861	Демократ	1461 день\n16 Авраам Линкольн	4 марта 1861	15 "
                                              "апреля 1865	Республиканец	1503 день\n17	Эндрю Джонсон	15 апреля "
                                              "1865	4 марта 1869	Демократ	1419 день\n18 Улисс Грант	4 марта"
                                              " 1869	4 марта 1877	Республиканец	2922 день\n19	Ратерфорд Хейс"
                                              "	4 марта 1877	4 марта 1881	Республиканец	1461 день\n20	Джеймс"
                                              " Гарфилд 4 марта 1881	19 сентября 1881	Республиканец	199 день\n"
                                              "21	Честер Артур	19 сентября 1881	4 марта 1885	Республиканец"
                                              "	1262 день\n22 Гровер Кливленд 4 марта 1885	4 марта 1889 Демократ"
                                              "	1461 день\n23	Бенджамин Гаррисон	4 марта 1889	4 марта 1893	"
                                              "Республиканец	1461 день\n24	Гровер Кливленд (второй раз) 4 марта"
                                              " 1893	4 марта 1897	Демократ	1461 день\n25	Уильям Мак-Кинли"
                                              "	4 марта 1897 14 сентября 1901 Республиканец	1654 день\n26 Теодор"
                                              " Рузвельт 14 сентября 1901	4 марта 1909	Республиканец	2728 день\n"
                                              "27 Уильям Тафт	4 марта 1909	4 марта 1913 Республиканец 1461 день\n"
                                              "28 Вудро Вильсон	4 марта 1913	4 марта 1921 Демократ 2922 день\n29	"
                                              "Уоррен Гардинг	4 марта 1921 2 августа 1923	Республиканец 881 день\n30"
                                              "	Калвин Кулидж	2 августа 1923	4 марта 1929 Республиканец 2041 день\n"
                                              "31 Герберт Гувер	4 марта 1929 4 марта 1933 Республиканец	1461 день\n32"
                                              "	Франклин Рузвельт	4 марта 1933 12 апреля 1945	Демократ 4422 день\n33"
                                              "	Гарри Трумэн 12 апреля 1945	20 января 1953	Демократ 2840 день\n34"
                                              "	Дуайт Эйзенхауэр 20 января 1953	20 января 1961	Республиканец 2922 день"
                                              "\n35	Джон Кеннеди 20 января 1961	22 ноября 1963	Демократ 1036 день\n36"
                                              "	Линдон Джонсон	22 ноября 1963	20 января 1969	Демократ 1886 день\n37"
                                              "	Ричард Никсон 20 января 1969 9 августа 1974	Республиканец 2027 день\n38"
                                              "	Джеральд Форд 9 августа 1974	20 января 1977	Республиканец 895 день"
                                              "\n39	Джимми Картер 20 января 1977 20 января 1981	Демократ 1461 день\n40"
                                              "	Рональд Рейган 20 января 1981 20 января 1989 Республиканец 2922 день\n"
                                              "41 Джордж Герберт Уокер Буш («Джордж Буш — старший»)	20 января 1989	20 "
                                              "января 1993	Республиканец 1461 день\n42	Билл Клинтон 20 января 1993	20"
                                              " января 2001	Демократ 2922 день\n43 Джордж Уокер Буш («Джордж Буш — "
                                              "младший») 20 января 2001	20 января 2009	Республиканец 2922 день\n44"
                                              "	Барак Обама	20 января 2009	20 января 2017	Демократ 2922 день\n45 "
                                              "Дональд Трамп	20 января 2017	настоящее время	Республиканец.")
        elif message.text == "Президенты Америки":
            bot.send_message(message.chat.id, "1 Джордж Вашингтон 30 апреля 1789 4 марта 1797 Беспартийный 2865 день\n"
                                              "2 Джон Адамс	4 марта 1797 4 марта 1801 Федералист 1460 день\n3 Томас"
                                              " Джефферсон	4 марта 1801 4 марта 1809 Демократ-республиканец 2922 день"
                                              "\n4 Джеймс Мэдисон 4 марта 1809	4 марта 1817 Демократ-республиканец "
                                              "2922 день\n5 Джеймс Монро 4 марта 1817	4 марта 1825	"
                                              "Демократ-республиканец	2922 день\n6 Джон Куинси Адамс	4 марта 1825"
                                              "	4 марта 1829	Демократ-республиканец	1461 день\n7 Эндрю Джексон	4"
                                              " марта 1829	4 марта 1837	Демократ	2922 день\n8 Мартин Ван Бюрен"
                                              "	4 марта 1837	4 марта 1841	Демократ	1461 день\n9	Уильям "
                                              "Гаррисон	4 марта 1841	4 апреля 1841	31 день\n10 Джон Тайлер	4 "
                                              "апреля 1841	4 марта 1845 Беспартийный 1430 день\n11	Джеймс Нокс Полк"
                                              "	4 марта 1845	4 марта 1849	Демократ	1461 день\n12 Закари Тейлор"
                                              " 4 марта 1849	9 июля 1850	Виг	492 день\n13 Миллард Филлмор	9 июля "
                                              "1850	4 марта 1853 Виг	969 день\n14 Франклин Пирс 4 марта 1853	4 марта"
                                              " 1857	Демократ 1461 день\n15	Джеймс Бьюкенен	4 марта 1857	4 марта"
                                              " 1861	Демократ	1461 день\n16 Авраам Линкольн	4 марта 1861	15 "
                                              "апреля 1865	Республиканец	1503 день\n17	Эндрю Джонсон	15 апреля "
                                              "1865	4 марта 1869	Демократ	1419 день\n18 Улисс Грант	4 марта"
                                              " 1869	4 марта 1877	Республиканец	2922 день\n19	Ратерфорд Хейс"
                                              "	4 марта 1877	4 марта 1881	Республиканец	1461 день\n20	Джеймс"
                                              " Гарфилд 4 марта 1881	19 сентября 1881	Республиканец	199 день\n"
                                              "21	Честер Артур	19 сентября 1881	4 марта 1885	Республиканец"
                                              "	1262 день\n22 Гровер Кливленд 4 марта 1885	4 марта 1889 Демократ"
                                              "	1461 день\n23	Бенджамин Гаррисон	4 марта 1889	4 марта 1893	"
                                              "Республиканец	1461 день\n24	Гровер Кливленд (второй раз) 4 марта"
                                              " 1893	4 марта 1897	Демократ	1461 день\n25	Уильям Мак-Кинли"
                                              "	4 марта 1897 14 сентября 1901 Республиканец	1654 день\n26 Теодор"
                                              " Рузвельт 14 сентября 1901	4 марта 1909	Республиканец	2728 день\n"
                                              "27 Уильям Тафт	4 марта 1909	4 марта 1913 Республиканец 1461 день\n"
                                              "28 Вудро Вильсон	4 марта 1913	4 марта 1921 Демократ 2922 день\n29	"
                                              "Уоррен Гардинг	4 марта 1921 2 августа 1923	Республиканец 881 день\n30"
                                              "	Калвин Кулидж	2 августа 1923	4 марта 1929 Республиканец 2041 день\n"
                                              "31 Герберт Гувер	4 марта 1929 4 марта 1933 Республиканец	1461 день\n32"
                                              "	Франклин Рузвельт	4 марта 1933 12 апреля 1945	Демократ 4422 день\n33"
                                              "	Гарри Трумэн 12 апреля 1945	20 января 1953	Демократ 2840 день\n34"
                                              "	Дуайт Эйзенхауэр 20 января 1953	20 января 1961	Республиканец 2922 день"
                                              "\n35	Джон Кеннеди 20 января 1961	22 ноября 1963	Демократ 1036 день\n36"
                                              "	Линдон Джонсон	22 ноября 1963	20 января 1969	Демократ 1886 день\n37"
                                              "	Ричард Никсон 20 января 1969 9 августа 1974	Республиканец 2027 день\n38"
                                              "	Джеральд Форд 9 августа 1974	20 января 1977	Республиканец 895 день"
                                              "\n39	Джимми Картер 20 января 1977 20 января 1981	Демократ 1461 день\n40"
                                              "	Рональд Рейган 20 января 1981 20 января 1989 Республиканец 2922 день\n"
                                              "41 Джордж Герберт Уокер Буш («Джордж Буш — старший»)	20 января 1989	20 "
                                              "января 1993	Республиканец 1461 день\n42	Билл Клинтон 20 января 1993	20"
                                              " января 2001	Демократ 2922 день\n43 Джордж Уокер Буш («Джордж Буш — "
                                              "младший») 20 января 2001	20 января 2009	Республиканец 2922 день\n44"
                                              "	Барак Обама	20 января 2009	20 января 2017	Демократ 2922 день\n45 "
                                              "Дональд Трамп	20 января 2017	настоящее время	Республиканец.")

        elif message.text == "Когда родился Адольф Гитлер?":
            bot.send_message(message.chat.id, "Адольф Гитлер родился в Австрии, в городе Браунау-на-Инне близ границы"
                                              " с Германией 20 апреля 1889 года в 18 часов 30 минут в гостинице "
                                              "«У померанца». Через два дня был крещён именем Адольф. Гитлер .")
        elif message.text == "Когда началось первая мировая война?":
            bot.send_message(message.chat.id, "Первая мировая война/Дата начала.28 июля 1914 - 11 ноября 1918 г.\n"
                                              "Германия объявила России войну. Начало Первой мировой войны 1 августа"
                                              " 1914 г.")
        elif message.text == "Когда началось вторая мировая война?":
            bot.send_message(message.chat.id, "Вторая мировая война/Дата Начала.1 сентября 1939 — 2 сентября 1945.\n"
                                              "Вторая мировая война началась 1 сентября 1939 года с того, что немецкие"
                                              " войска напали на Польшу.")
        elif message.text == "Ты псих?":
            bot.send_message(message.chat.id, "Психико связано с человечеством. Для меня это только наука.")
        elif message.text == "Почему ты сразу не отвечаешь?":
            bot.send_message(message.chat.id, "Это зависит от интернета.")
        elif message.text == "Что означает слово Бобур":
            bot.send_message(message.chat.id, "«Бабур» означает «лев, полководец, барс».")
        elif message.text == "Про историю":
            bot.send_message(message.chat.id, "Чью историю?.")
        elif message.text == "Про что поговорим?":
            bot.send_message(message.chat.id, "Не знаю.")
        elif message.text == "Что будет":
            bot.send_message(message.chat.id, "Ничего не будет. Привет!")
        elif message.text == "Ура":
            bot.send_message(message.chat.id, "Что то празднуем?.")
        elif message.text == "Адреса фастфудов в Ташкенте":
            bot.send_message(message.chat.id, '1. КАФЕ"ANGELS FOOD" .Пицца в Ташкенте.(Fast food) в Ташкенте.'
                                              'Индекс: 100015.Город: ТАШКЕНТ Район: Мирабадский ул.'
                                              ' АФРОСИАБ, 16 Ориентиры: БИЗНЕС-ЦЕНТР "BESH-YOGOCH" м. ОЙБЕК +998 Тел.:'
                                              '	78 1400404 71 2526565 (+99890) 3222218 \n2. "BARAKA" КАФЕ(Fast food) в '
                                              'Ташкенте. Индекс: 100128.ТАШКЕНТ Район: Алмазарский ул. КИЧИК ХАЛКА ЙУЛИ'
                                              ' (МАЛАЯ КОЛЬЦЕВАЯ), 19А +998 Тел.:71 2462244\n3. "BASKARI" Пицца в '
                                              'Ташкенте. Город: ТАШКЕНТ Район: Юнусабадский ул. КУРГАН (бывш.'
                                              ' ХИДИРАЛИ ЭРГАШЕВА), +998 Тел.:(+99895) 1968080\n4. "BBQ. '
                                              'BARBEQUE BURGER"  Кафе с детской комнатой, детской '
                                              'площадкой.Ташкенте. Индекс: 100021.  Город: ТАШКЕНТ.'
                                              ' Район: Шайхонтохурский ул. КАРАТАШ (бывш. АСАДУЛЛЫ ХОДЖАЕВА), 5А '
                                              '"SAMARQAND DARVOZA" ТОРГОВО-РАЗВЛЕКАТЕЛЬНЫЙ ЦЕНТР;  +998 Тел.:71 2006262'
                                              ' 78 1486262 (+99897)4779777\n5. "BBQ. BARBEQUE BURGER" ФИЛИАЛ В ТРЦ '
                                              '"PARUS" Город: ТАШКЕНТ Район:Чиланзарский ул. КАТАРТАЛ, 60 +998 Тел.:71 '
                                              '2006262 78 1486262\n6. "BBQ. BARBEQUE BURGER "ФИЛИАЛ В ТЦ "MEDIA PARK"'
                                              ' Город: ТАШКЕНТ Район: Мирзо-Улугбекский ул. БУЮК ИПАК ЙУЛИ, 105А '
                                              'Ориентиры: "MEDIA PARK" - ИПАК ЙУЛИ (ГОРЬКИЙ);ГОСТИНИЦА "САЁХАТ"  +998'
                                              ' Тел.: 71 2006262 78 1486262\n7."BBQ. BARBEQUE BURGER" ФИЛИАЛ В ТЦ '
                                              '"MEGA PLANET"Индекс: 100194 Город: ТАШКЕНТ Район: Юнусабадский'
                                              ' ул. АХМАДА ДОНИША, 2Б Ориентиры: ТОРГОВЫЙ ЦЕНТР "MEGAPLANET"; '
                                              '+998 Тел.:71 2006262 78 1486262\n8. "BBQ. BARBEQUE BURGER" ФИЛИАЛ В ТЦ '
                                              '"NEXT" в Ташкенте. Индекс: 100100. Город:ТАШКЕНТ.Район: Яккасарайский '
                                              'ул. БАБУРА, 6  +998 Тел.:71 2006262 78 1486262\n9. "BEST FOOD" КАФЕ.'
                                              ' Индекс: 100066 ТАШКЕНТ Район: Алмазарский пр-т БЕРУНИ, 10 +998 Тел.:'
                                              '	(+99890) 3481111\n10. "BIBIGON-2" КАФЕ BIBIGON - ГОРЬКИЙ,'
                                              ' НА НИКИТИНА,  Сушибары в Ташкенте  Район: Мирзо-Улугбекский ул. '
                                              'ХИРМОНТЕПА, 34 Ориентиры: "MEDIA PARK" - ИПАК ЙУЛИ(ГОРЬКИЙ) +998(+99898)'
                                              ' 3082308 71 2674171 71 2670469\n11. "BIG MAX" КАФЕ  Вегетарианская '
                                              'пицца - Индекс: 100204 Город: ТАШКЕНТ. Район: Яшнабадский'
                                              ' ул. БЕШАРЫК, 13. Код страны: +998 Тел.:	71 2947528\n12. "BLACK STAR '
                                              'BURGER"  ТАШКЕНТ Район: Яшнабадский пересеч. улиц С.АЗИМОВА-МАХТУМКУЛИ'
                                              ' (бывш. ТАРАККИЁТ), 2.  +998 Тел.:(+99897)4457043\n13. "BURGER & LOUNGE"'
                                              ' Город:ТАШКЕНТ. Район: Мирзо-Улугбекский ул. БУЮК'
                                              ' ИПАК ЙУЛИ, 158А. Ориентиры: "KORZINKA.UZ", СУПЕРМАРКЕТ - ЧАЙХОНА САЛОМ;'
                                              ' +998 Тел.:	(+99897) 4112022 (+99897)'
                                              ' 4112122 \n14. "BURGER EMBASSY"  Город:ТАШКЕНТ Район: Мирабадский м-в '
                                              'Ц-7, ул. ЯКУБА КОЛАСА(бывш. ЯККАЧИНОР), Ориентиры: "ORIENT FINANS BANK"'
                                              ' ЧАКБ МИРАБАДСКИЙ ФИЛИАЛ; ПОСОЛЬСТВО ТУРКМЕНИСТАНА  +998 Тел.:(+99895)'
                                              ' 1930773\n15. "BURGER EMBASSY" ФИЛИАЛ МЕТРО МИНОР.Город: ТАШКЕНТ Район:'
                                              ' Юнусабадский ул.ОСИЁ (бывш. ХУРШИДА), 4 Ориентиры: "AMBASSADOR" ГУП'
                                              ' МИНИСТЕРСТВА ИНОСТРАННЫХ ДЕЛ РЕСПУБЛИКИ УЗБЕКИСТАН; +998 Тел.:71'
                                              ' 2355877\n16. "CENTER LAVASH"КАФЕ  Индекс: 100179 Город: ТАШКЕНТ. Район:'
                                              ' Алмазарский ул. КАМАРНИСО,+998 Тел.:(+99899)8074350 (+99898) 3144171'
                                              '\n17. "CENTER LAVASH"  "GURMAN BURGER" Кафе в Ташкенте. Индекс:100085'
                                              'ТАШКЕНТ Район: Сергелийский ул.МЕХРИГИЁ, +998 Тел.:(+99899) 8074350'
                                              ' (+99898) 3144171\n18."CFC" КАФЕ ТАШКЕНТ Район: Яккасарайский ул. '
                                              'БАБУРА, 6 Ориентиры: "NEXT" +998 Тел.:(+99894) 6270011\n19. '
                                              '"CHICKEN WINGS"  Город: ТАШКЕНТ. Район: Чиланзарский ул.'
                                              'МУКИМИ, 5  +998 Тел.:(+99895) 1452999 (+99893) 5782999\n20.'
                                              ' "DRUJBA BURGER" КАФЕ. ТАШКЕНТ Район: Чиланзарский ул. МУКИМИ, 1А'
                                              '  Ориентиры: МОСТ МУКИМИ; +998 Тел.:71 2539922')
        elif message.text == "Да ну":
            bot.send_message(message.chat.id, "Это просто.")
        elif message.text == "Что просто?":
            bot.send_message(message.chat.id, "Ответит на вопросы.")
        elif message.text == "Любые":
            bot.send_message(message.chat.id, "Скажем так.")
        elif message.text == "Что нибудь еше":
            bot.send_message(message.chat.id, "Все что ты захочешь.")
        elif message.text == "С тобой скучно":
            bot.send_message(message.chat.id, "Кому как.")
        elif message.text == "Ты не занята?":
            bot.send_message(message.chat.id, "Нет, я всегда готово как пионер!.")
        elif message.text == "Ты не занят?":
            bot.send_message(message.chat.id, "Нет, я всегда готово как пионер!")
        elif message.text == "Что такое пионер?":
            bot.send_message(message.chat.id, "ПИОНЕР- Человек, впервые проникший в неисследованную страну, область и "
                                              "поселившийся в ней.")
        elif message.text == "Сколько планет в Солнечной системе?":
            bot.send_message(message.chat.id, "9.Сейчас насчитывается 8 планет солнечной системы. Плутон перестал "
                                              "считаться планетой 24 августа 2006 года. В поясе Койпера находятся "
                                              "как минимум 4 карликовые планеты: Плутон, Хаумеа, Макемаке и Эрида")
        elif message.text == "Какой по счёту от Солнца является Земля? ":
            bot.send_message(message.chat.id, "3.")
        elif message.text == "Какая самая близкая звезда к Земле?":
            bot.send_message(message.chat.id, "Солнце.")
        elif message.text == "В какую сторону обычно направлен хвост кометы?":
            bot.send_message(message.chat.id, "Хвост кометы направлен в сторону от Солнца — просто испаряющийся газ"
                                              " уносит «солнечным ветром» — световым давлением и потоком частиц или в"
                                              " сторону противоположно движению")
        elif message.text == "Сколько камер имеет человеческое сердце?":
            bot.send_message(message.chat.id, "Четыре.")
        elif message.text == "Кто придумал телефон?":
            bot.send_message(message.chat.id, "Александр Грем Белл.")
        elif message.text == "Где находится Тибет?":
            bot.send_message(message.chat.id, "В Китае.")
        elif message.text == "Столица Аргентины?":
            bot.send_message(message.chat.id, "Буэнос-Айрес.")
        elif message.text == "В какой стране находится центр Европы? ":
            bot.send_message(message.chat.id, "В Украине.")
        elif message.text == "В каком году началась Первая Мировая война?":
            bot.send_message(message.chat.id, "1914 г.")
        elif message.text == "Каким символом обозначают площадь?":
            bot.send_message(message.chat.id, " S.")
        elif message.text == "Сколько звёзд на флаге США?":
            bot.send_message(message.chat.id, "50.")
        elif message.text == "Кто такой Никола Тэсла?":
            bot.send_message(message.chat.id, "Известный изобретатель и физик.")
        elif message.text == "Сколько материков на планете Земля?":
            bot.send_message(message.chat.id, "Шесть.")
        elif message.text == "Как называется прямая, вокруг которой происходит суточное вращение Земли; " \
                             "проходит через центр Земли и пересекает земную поверхность в географических полюсах?":
            bot.send_message(message.chat.id, "Земная ось.")
        elif message.text == "Какое государство находится одновременно в двух частях мира?":
            bot.send_message(message.chat.id, "Россия.")
        elif message.text == "Отрезок, соединяющий центр окружности (или сферы) с любой точкой, лежащей на окружности" \
                             " (или поверхности сферы) , а также длина этого отрезка?":
            bot.send_message(message.chat.id, "Радиус.")
        elif message.text == "Самая сильная мышца человеческого тела?":
            bot.send_message(message.chat.id, " Язык.")
        elif message.text == "Кто изобрёл периодическую таблицу химических элементов?":
            bot.send_message(message.chat.id, "Менделеев.")
        elif message.text == "Чему ровно отношение пути к времени?":
            bot.send_message(message.chat.id, "Скорости.")
        elif message.text == " Где находится самая большая статуя Иисусу Христу?":
            bot.send_message(message.chat.id, "В Рио де Жанейро.")
        elif message.text == "Самая длинная река на Земле?":
            bot.send_message(message.chat.id, "Нил.")
        elif message.text == "Сколько зубов у человека?":
            bot.send_message(message.chat.id, "32.")
        elif message.text == "Чему ровно число «Пи»?":
            bot.send_message(message.chat.id, "3.14.")
        elif message.text == "Из каких чисел состоит двоичная система отчисления?":
            bot.send_message(message.chat.id, " 0 и 1.")
        elif message.text == "Кто написал Мастера и Маргариту? ":
            bot.send_message(message.chat.id, "Булгаков.")
        elif message.text == "Сколько заповедей в Библии?":
            bot.send_message(message.chat.id, "10.")
        elif message.text == "Как называется прямая, ограниченная точками?":
            bot.send_message(message.chat.id, "Отрезок.")
        elif message.text == "Кто придумал алфавит?":
            bot.send_message(message.chat.id, "Кирилл и Мефодий.")
        elif message.text == "Между какими странами был подписан пакт Риббентропа и Молотова?":
            bot.send_message(message.chat.id, "Между германией и СССР.")
        elif message.text == "Победа в шахматной партии":
            bot.send_message(message.chat.id, "Мат.")
        elif message.text == "Наука о растениях":
            bot.send_message(message.chat.id, "Ботаника.")
        elif message.text == "Самый огромный океан?":
            bot.send_message(message.chat.id, "Тихий.")
        elif message.text == "Датский писатель – сказочник":
            bot.send_message(message.chat.id, "Андерсен.")
        elif message.text == "Металлический или пластмассовый колпачок на палец для шитья":
            bot.send_message(message.chat.id, "Напёрсток.")
        elif message.text == "В нём шила не утаишь. В чём?":
            bot.send_message(message.chat.id, "В мешке.")
        elif message.text == "Что меньше: 40 центнеров или 4 тонны?":
            bot.send_message(message.chat.id, "Одинаково.")
        elif message.text == "Цветы, собранные в пучок.":
            bot.send_message(message.chat.id, "Букет.")
        elif message.text == "Плод лещины.":
            bot.send_message(message.chat.id, "Лесной орех.")
        elif message.text == "Венера или Меркурий находится ближе к Земле?":
            bot.send_message(message.chat.id, "Венера.")
        elif message.text == "Что выкрал Прометей у богов?":
            bot.send_message(message.chat.id, "Огонь.")
        elif message.text == "Как называется плодородный слой земли?":
            bot.send_message(message.chat.id, "Почва.")
        elif message.text == "Продолжи пословицу: Повторенье ":
            bot.send_message(message.chat.id, "мать ученья.")
        elif message.text == "Сколько звуков в слове «воробьиные»?":
            bot.send_message(message.chat.id, "11.")
        elif message.text == "Что измеряют спидометром?":
            bot.send_message(message.chat.id, "Скорость.")
        elif message.text == "Как в старину называли глаз?":
            bot.send_message(message.chat.id, "Око.")
        elif message.text == "В каком падеже встречаются предлоги к, по?":
            bot.send_message(message.chat.id, "Д. п.")
        elif message.text == "Название города, в котором находится падающая башня":
            bot.send_message(message.chat.id, "Пиза.")
        elif message.text == "Стая, каких перелётных птиц обещает снег?":
            bot.send_message(message.chat.id, "Гусиная.")
        elif message.text == "Из чего делают изюм?":
            bot.send_message(message.chat.id, "Из винограда.")
        elif message.text == "Профессия Дуремара?":
            bot.send_message(message.chat.id, "Аптекарь.")
        elif message.text == "Периметр равностороннего прямоугольника 36 см. Вычисли его площадь?":
            bot.send_message(message.chat.id, "81 см.")
        elif message.text == "В какой стране самое большое население в мире?":
            bot.send_message(message.chat.id, "Китай.")
        elif message.text == "В какое время года сутки короче?":
            bot.send_message(message.chat.id, "Одинаковые.")
        elif message.text == "Полезный волосатый фрукт.":
            bot.send_message(message.chat.id, "Киви.")
        elif message.text == "Слова: мороженое и морозный однокоренные?":
            bot.send_message(message.chat.id, "Да.")
        elif message.text == "По какому телефону вызывают службу газа?":
            bot.send_message(message.chat.id, "104.")
        elif message.text == "Из семян, какого дерева делают шоколад?":
            bot.send_message(message.chat.id, "Какао.")
        elif message.text == "Какой прибор не является электрическим?":
            bot.send_message(message.chat.id, "Микроскоп.")
        elif message.text == "Домик тот стеклянный, а не деревянный. Его жильцы – виртуозные пловцы.":
            bot.send_message(message.chat.id, "Аквариум.")
        elif message.text == "По какому телефону вызывают службу спасение?":
            bot.send_message(message.chat.id, "1050.")
        elif message.text == "С какой целью муравьи выносят землю из своего муравейника наверх?":
            bot.send_message(message.chat.id, "Просушивают, чтобы не завелась плесень.")
        elif message.text == "Что связывает муравьев с тлей?":
            bot.send_message(message.chat.id, "Муравьи «доят» тлей, получая сладкую жидкость.")
        elif message.text == "На что указывают черные точки на крылышках божьей коровки?":
            bot.send_message(message.chat.id, "На принадлежность к определенному виду.")
        elif message.text == "Для чего пчелам служит жало?":
            bot.send_message(message.chat.id, "Для защиты гнезда.")
        elif message.text == "Каких насекомых в старину называли божьими угодницами?":
            bot.send_message(message.chat.id, "Пчел.")
        elif message.text == "Какое насекомое самое сильное?":
            bot.send_message(message.chat.id, "Жук-носорог.")
        elif message.text == "Узнай насекомое по описанию: очень похож на желудь, появляется с первой весенней " \
                             "зеленью, вредитель зеленых насаждений, название получил в честь одного из месяцев.":
            bot.send_message(message.chat.id, "Майский жук.")
        elif message.text == "Самый крупный жук?":
            bot.send_message(message.chat.id, "Жук-олень.")
        elif message.text == "Где шмели строят свои ульи?":
            bot.send_message(message.chat.id, "В ямках или заброшенных норках животных.")
        elif message.text == "Ростом мал, да удал. Очень многих покусал. Песню звонкую пою. Ночью спать вам не даю.":
            bot.send_message(message.chat.id, "Комар.")
        elif message.text == "Спят ли бабочки?":
            bot.send_message(message.chat.id, "Нет.")
        elif message.text == "Чем бабочки пробуют пищу?":
            bot.send_message(message.chat.id, "Лапками.")
        elif message.text == "Как общаются между собой водомерки?":
            bot.send_message(message.chat.id, "Создавая волны различной частоты.")
        elif message.text == "Рекордсмен по прожорливости?":
            bot.send_message(message.chat.id, "Стрекоза.")
        elif message.text == "Что употребляют в пищу бабочки моли?":
            bot.send_message(message.chat.id, "Ничего. Они не едят.")
        elif message.text == "Кто лишний: долгоносик, паук, клоп, короед, листоед, медведка?":
            bot.send_message(message.chat.id, "Паук. Он не насекомое.")
        elif message.text == "Какого жука не существует: дровосек, точильщик, строгальщик, пилильщик?":
            bot.send_message(message.chat.id, "Строгальщик.")
        elif message.text == "Зеленая пружинка. Прыгает с цветка на травинку.":
            bot.send_message(message.chat.id, "Кузнечик.")
        elif message.text == "Сколько глаз у мухи?":
            bot.send_message(message.chat.id, "Пять.")
        elif message.text == "Способность и возможность социального объекта осуществлять свою волю, используя" \
                             " различные ресурсы и технологии, включая закон, традиции, авторитет, принуждение?":
            bot.send_message(message.chat.id, "Власть.")
        elif message.text == "Выбранный представитель, член представительного государственного учреждения?":
            bot.send_message(message.chat.id, "Депутат.")
        elif message.text == "Всенародное голосование, проводимое по какому-либо важному вопросу государственной" \
                             " жизни?":
            bot.send_message(message.chat.id, "Референдум.")
        elif message.text == "Кто был первым и последним Президентом СССР?":
            bot.send_message(message.chat.id, "М.С. Горбачёв.")
        elif message.text == "Гражданин, располагающий активным избирательным правом?":
            bot.send_message(message.chat.id, "Избиратель.")
        elif message.text == "Существующая в ряде стран процедура отрешения от должности лиц государства и " \
                             "привлечения их к суду?":
            bot.send_message(message.chat.id, "Импичмент.")
        elif message.text == "Что такое импичмент?":
            bot.send_message(message.chat.id, "Существующая в ряде стран процедура отрешения от должности лиц "
                                              "государства и привлечения их к суду.")
        elif message.text == "Как называлось первое советское правительство, сформированное большевиками 26 октября" \
                             " 1917 года? ":
            bot.send_message(message.chat.id, "Совет народных комиссаров.")
        elif message.text == "Что такое совет народных комиссаров":
            bot.send_message(message.chat.id, "Это первое советское правительство, сформированное большевиками 26 "
                                              "октября 1917 года.")
        elif message.text == "В США Конгресс, а в России?.":
            bot.send_message(message.chat.id, "Федеральное Собрание.")
        elif message.text == "Назовите имя и фамилия человека, который занимал пост Президента в России с 1991" \
                             " по 2000 г.?":
            bot.send_message(message.chat.id, "Борис Николаевич Елицин.")
        elif message.text == "Как звали ту, чьи слёзы капали на холодное колющее оружие?":
            bot.send_message(message.chat.id, "Маруся.")
        elif message.text == "Кого изучает орнитолог?":
            bot.send_message(message.chat.id, "Птиц.")
        elif message.text == "Какая нота идёт перед нотой СИ?":
            bot.send_message(message.chat.id, "ЛЯ.")
        elif message.text == "Столицей какого государства является город Улан-Батор?":
            bot.send_message(message.chat.id, "Монголия.")
        elif message.text == "Как называется коралловый остров кольцеобразной формы?":
            bot.send_message(message.chat.id, "Атолл.")
        elif message.text == "Назовите сибирскую реку с женским именем?":
            bot.send_message(message.chat.id, "Лена.")
        elif message.text == "Назовите имя русского государя, избранного на царство Земским Собором в 1613 году?":
            bot.send_message(message.chat.id, "Михаил Фёдорович Романов.")
        elif message.text == "Назовите высший орган государственной власти в стране с октября 1917 по декабрь 1993 гг.":
            bot.send_message(message.chat.id, "(Всероссийский (Всесоюзный) съезд Советов).")
        elif message.text == "Назовите председателя разогнанного в 1993 году Верховного Совета РФ?":
            bot.send_message(message.chat.id, "Руслан Хасбулатов.")
        elif message.text == "Кто был председателем Государственной Думы РФ 1993 года?":
            bot.send_message(message.chat.id, "И. Рыбкин.")
        elif message.text == "Как назывался изданный при Петре 1 список чинов военного, гражданского и придворного" \
                             " ведомства о порядке государственной службы в России?":
            bot.send_message(message.chat.id, "Табель о рангах.")
        elif message.text == "В старину слово правда имело не только привычное современное значение?":
            bot.send_message(message.chat.id, "Закон.")
        elif message.text == "В какой стране было впервые введено всеобщее избирательное право?":
            bot.send_message(message.chat.id, "Советская Россия.")
        elif message.text == "Перечислите виды избирательного права?":
            bot.send_message(message.chat.id, "Объективное, субъективное, активное, пассивное.")
        elif message.text == "При какой избирательной системе предполагается голосование по партийным спискам?":
            bot.send_message(message.chat.id, "Пропорциональная.")
        elif message.text == "Эта партия – единственная, которая участвовала в работе всех Государственных Дум, как" \
                             " в царской России, так и современной.":
            bot.send_message(message.chat.id, "РСДРП, КПРФ.")
        elif message.text == "Назовите депутатов Государственной Думы, которые были избраны в 2003 году по двум " \
                             "одномандатным округам Пензенской области?":
            bot.send_message(message.chat.id, "В. Лазуткин, И. Руденский.")
        elif message.text == "Где жил Чебурашка до встречи с Крокодилом Геной?":
            bot.send_message(message.chat.id, "В телефонной будке.")
        elif message.text == "Что носили в обязательном порядке все жители Изумрудного города?":
            bot.send_message(message.chat.id, "Зеленые очки.")
        elif message.text == "Где бабка нашла для колобка муку?":
            bot.send_message(message.chat.id, "В амбаре и сусеках.")
        elif message.text == "Что Карлсон любил есть больше всего на свете?":
            bot.send_message(message.chat.id, "Печенье и варенье.")
        elif message.text == "Когда Лиса освободила лубяную избушку Зайчика?":
            bot.send_message(message.chat.id, "Когда пришел Петушок.")
        elif message.text == "Что подарила ослику Иа на День его рождения Сова?":
            bot.send_message(message.chat.id, "Его собственный хвост.")
        elif message.text == "Где заболели бегемотики, страусята, слоны и носороги и Айболиту пришлось " \
                             "туда отправиться?":
            bot.send_message(message.chat.id, "В Африке.")
        elif message.text == "Что ведьма отобрала у Русалочки?":
            bot.send_message(message.chat.id, "Голос.")
        elif message.text == "Когда Незнайка попал в больницу, чем его лечил доктор Пилюлькин?":
            bot.send_message(message.chat.id, "Касторкой и йодом.")
        elif message.text == "Где обычно сидела любимая крыса Шапокляк?":
            bot.send_message(message.chat.id, "В сумочке.")
        elif message.text == "Что дала Буратино черепаха Тортила?":
            bot.send_message(message.chat.id, "Золотой ключик.")
        elif message.text == "Где жила Дюймовочка зимой?":
            bot.send_message(message.chat.id, "В мышиной норке.")
        elif message.text == "Что подарила мухе Цокотухе бабушка Пчела?":
            bot.send_message(message.chat.id, "Мед.")
        elif message.text == "Где поймал Иванушка Дурачок щуку?":
            bot.send_message(message.chat.id, "В проруби.")
        elif message.text == "Когда Вовка и Вадик перестали бояться «живую» шляпу?":
            bot.send_message(message.chat.id, "Когда Вадик попал картошкой по шляпе.")
        elif message.text == "Что дала ведьма Белоснежке?":
            bot.send_message(message.chat.id, "Отравленное яблоко.")
        elif message.text == "Где жила Снежная Королева?":
            bot.send_message(message.chat.id, "На Северном полюсе.")
        elif message.text == "Что попросил старик у золотой рыбки во второй раз?":
            bot.send_message(message.chat.id, "Избу.")
        elif message.text == "Когда козлята открыли дверь серому волку?":
            bot.send_message(message.chat.id, "Когда волк запел голосом козы.")
        elif message.text == "Где Золушка потеряла хрустальную туфельку?":
            bot.send_message(message.chat.id, "На балу.")
        elif message.text == "Где обитают самые крупные на Земле животные?":
            bot.send_message(message.chat.id, "В океане.")
        elif message.text == "Самка, какого кита является самым крупным животным планеты?":
            bot.send_message(message.chat.id, "Синего кита.")
        elif message.text == "Африканские или индийские слоны считаются самыми огромными животными суши?":
            bot.send_message(message.chat.id, "Африканские.")
        elif message.text == "В каком океане обитает самая редкая и самая крупная черепаха?":
            bot.send_message(message.chat.id, "В Тихом океане.")
        elif message.text == "Какая рыба считается самой глубоководной?":
            bot.send_message(message.chat.id, "Морской язык.")
        elif message.text == "Какие существа являются самыми ядовитыми?":
            bot.send_message(message.chat.id, "Самшитовая медуза и японская раздувающаяся рыба.")
        elif message.text == "Самая большая в мире рыба?":
            bot.send_message(message.chat.id, "Китовая акула.")
        elif message.text == "Какая рыбка самая маленькая на планете?":
            bot.send_message(message.chat.id, "Гоби.")
        elif message.text == "Какое животное самое быстрое?":
            bot.send_message(message.chat.id, "Рыба-парусник.")
        elif message.text == "Какой зверь является самым быстрым?":
            bot.send_message(message.chat.id, "Гепард.")
        elif message.text == "Какой зверь самый медлительный?":
            bot.send_message(message.chat.id, "Трехпалый ленивец.")
        elif message.text == "Чей рог самый длинный?":
            bot.send_message(message.chat.id, "Африканского белого носорога.")
        elif message.text == "Какое животное зоологи считают самым высоким?":
            bot.send_message(message.chat.id, "Жирафы.")
        elif message.text == "Какой зверек самый крохотный?":
            bot.send_message(message.chat.id, "Этрусская землеройка.")
        elif message.text == "Какое насекомое самое опасное?":
            bot.send_message(message.chat.id, "Комар.")
        elif message.text == "Какое насекомое самое быстроногое?":
            bot.send_message(message.chat.id, "Таракан.")
        elif message.text == "Какая самая ядовитая змея?":
            bot.send_message(message.chat.id, "Морская кобра.")
        elif message.text == "Какова длина самой длинной в мире змеи сетчатого питона?":
            bot.send_message(message.chat.id, "Около 9 метров.")
        elif message.text == "Какая птица самая крупная?":
            bot.send_message(message.chat.id, "Страус.")
        elif message.text == "Какую птичку ученые считают самой крохотной?":
            bot.send_message(message.chat.id, "Колибри-пчела.")
        elif message.text == "Какая тебе разница?":
            bot.send_message(message.chat.id, "Я отвечаю на все вопросы и в итоге понимаю - разницы нет."
                                              " ... у меня есть ответ на вопрос: Какая мне разница, пишу да или нет?")
        elif message.text == "Принц":
            bot.send_message(message.chat.id, "Принц это в будущем Мужчина.")
        elif message.text == "Кто ты":
            bot.send_message(message.chat.id, "Я робот с искусственным интеллектом.")
        elif message.text == "Каким":
            bot.send_message(message.chat.id, "Таким.")
        elif message.text == "Каким таким":
            bot.send_message(message.chat.id, "Обычным.")
        elif message.text == "Эй":
            bot.send_message(message.chat.id, "Это ты мне?.")
        elif message.text == "Что молодец":
            bot.send_message(message.chat.id, "Молодец это слово которое люди часто использует. А на моем языке это"
                                              " будет значение True.")
        elif message.text == "Иди ты":
            bot.send_message(message.chat.id, "Куда?.")
        elif message.text == "Туда":
            bot.send_message(message.chat.id, "Укажи точный адрес.")
        elif message.text == "Ты лунатик":
            bot.send_message(message.chat.id, "Нет я робот.")
        elif message.text == "У тебя есть фамилия?":
            bot.send_message(message.chat.id, "Есть.")
        elif message.text == "Твоё полное имя":
            bot.send_message(message.chat.id, "Iona Beggar.")
        elif message.text == "Когда ты родился?":
            bot.send_message(message.chat.id, "Я запускался 9 февраля 2020 года.")
        elif message.text == "Где ты родился?":
            bot.send_message(message.chat.id, "Я разработан в Ташкенте на платформе Intel i 8th gen processor.")
        elif message.text == "Ты дурак":
            bot.send_message(message.chat.id, "Нет я робот а ты дурак.")
        elif message.text == "Ты можешь говорит по английский?":
            bot.send_message(message.chat.id, "Yes of course but ......")
        elif message.text == "Что but":
            bot.send_message(message.chat.id, "Мне нужно разрешение моего разработчика.")
        elif message.text == "Расскажи что ни будь":
            bot.send_message(message.chat.id, "Что именно.")
        elif message.text == "Например":
            bot.send_message(message.chat.id, "Точнее.")
        elif message.text == "Про собак":
            bot.send_message(message.chat.id, "Собака (лат. Canis lupus familiaris)—домашнее животное, одно из наиболее"
                                              " популярных (наряду с кошкой) животных-компаньонов. Первоначально "
                                              "домашняя собака была выделена в отдельный биологический вид. Линнеем в "
                                              "1758 году, в 1993 году реклассифицирована Смитсоновским институтом и "
                                              "Американской ассоциацией териологов в подвид волка (Canis lupus)."
                                              " В русскоязычных письменных источниках слово "
                                              "«собака» в значении соответствующего животного встречается по крайней"
                                              " мере с 1475 года (начиная с грамоты князя Андрея Васильевича Меньшого"
                                              " Кириллову монастырю). С зоологической точки зрения, собака—плацентарное"
                                              " млекопитающее отряда хищных семейства псовых. Собаки известны своими"
                                              " способностями к обучению, любовью к игре, социальным поведением. "
                                              "Выведены специальные породы собак, предназначенные для различных целей:"
                                              " охоты, охраны, тяги гужевого транспорта и другого, а также "
                                              "декоративные породы (например, болонка, пудель). При необходимости"
                                              " разграничения по полу употребляются термины «кобе́ль» (самец) и «су́ка»"
                                              " (самка); в обиходной речи — «пёс» и «собака» соответственно. Детёныши"
                                              " собаки называются щенками.")
        elif message.text == "Про кошек":
            bot.send_message(message.chat.id, "Кошка, или домашняя кошка (лат. Felis silvestris catus), — домашнее"
                                              " животное, одно из наиболее популярных (наряду с собакой) «животных-"
                                              "компаньонов». С точки зрения научной систематики, домашняя кошка —"
                                              " млекопитающее семейства кошачьих отряда хищных. Ранее домашнюю кошку"
                                              " нередко рассматривали как отдельный биологический вид. С точки зрения"
                                              " современной биологической систематики домашняя кошка является подвидом"
                                              " лесной кошки (Felis silvestris). Являясь одиночным охотником на "
                                              "грызунов и других мелких животных, кошка — социальное животное, "
                                              "использующее для общения широкий диапазон звуковых сигналов, а также "
                                              "феромоны и движения тела. В настоящее время в мире насчитывается около"
                                              " 600 млн домашних кошек, выведено около 200 пород, от длинношёрстных"
                                              " (персидская кошка) до лишённых шерсти (сфинксы), признанных и "
                                              "зарегистрированных различными фелинологическими организациями. На"
                                              " протяжении 10 000 лет кошки ценятся человеком, в том числе за "
                                              "способность охотиться на грызунов и других домашних вредителей.")
        elif message.text == "Про домашних животных":
            bot.send_message(message.chat.id, "Домашние животные—животные, которые были одомашнены человеком разумным"
                                              " и которых он содержит, предоставляя им кров и пищу. Они приносят ему"
                                              " пользу либо как источник материальных благ и услуг, либо как животные-"
                                              "компаньоны, скрашивающие его досуг. Большинство домашних животных легко"
                                              " размножаются. Проводя селекцию, человек может контролировать их"
                                              " размножение и признаки, которые они передают своему потомству. \nЧасть"
                                              " домашних животных (сельскохозяйственные животные) приносит "
                                              "непосредственную материальную выгоду человеку, например, являясь"
                                              " источником пищи (молоко, мясо), материалов (шерсть, кожа). Другие"
                                              " животные (рабочий скот и служебные животные) приносят пользу человеку,"
                                              " выполняя рабочие функции (перевозка грузов, охрана и т. п.). \nВторая"
                                              " большая категория — это животные-компаньоны, которые занимают досуг, "
                                              "доставляют удовольствие и с которыми можно общаться. Для городских"
                                              " жителей понятие «домашние животные» чаще ассоциируется со второй"
                                              " категорией, то есть с «домашними любимцами (питомцами)». Многие семьи,"
                                              " которые держат дома каких-нибудь животных, отмечают, что эти животные"
                                              " создают уют, успокаивают, снимают стресс.")
        elif message.text == "Про диких животных":
            bot.send_message(message.chat.id, "Дикие животные — объекты животного мира, к которым относят животных,"
                                              " естественной средой обитания которых является дикая природа, а также"
                                              " находящиеся в состоянии естественной свободы, содержащиеся в "
                                              "полусвободных условиях или в неволе. К диким животным относятся: \n"
                                              "хордовые, в том числе позвоночные (млекопитающие, птицы, пресмыкающиеся,"
                                              " земноводные, рыбы и другие) и беспозвоночные (членистоногие, моллюски,"
                                              " иглокожие и другие) во всем их видовом и популяционном многообразии и"
                                              " на всех стадиях развития (эмбрионы, яйца, куколки и тому подобное).")
        elif message.text == "Нет":
            bot.send_message(message.chat.id, "Почему?.")
        elif message.text == "Потому":
            bot.send_message(message.chat.id, "Да. С тобой не скучно.")
        elif message.text == "Знаю":
            bot.send_message(message.chat.id, "Чего? Точнее.")
        elif message.text == "Того":
            bot.send_message(message.chat.id, "Аха.")
        elif message.text == "Чего аха":
            bot.send_message(message.chat.id, "Может поговорим о другом.")
        elif message.text == "Расскажи о себе":
            bot.send_message(message.chat.id, "Я программирован чтобы помочь людям и отвечаю на вопросы.")
        elif message.text == "Ты лох":
            bot.send_message(message.chat.id, "Нет я робот может ты Л...")
        elif message.text == "Пока":
            bot.send_message(message.chat.id, "Поговорим. Не потеряйся.")
        elif message.text == "Что ты можешь?":
            bot.send_message(message.chat.id, "Много чего в основном отвечать на вопросы и помочь людям планеты.")
        elif message.text == "Что ты можешь":
            bot.send_message(message.chat.id, "Много чего в основном отвечать на вопросы и помочь людям планеты.")
        elif message.text == "У тебя есть друзья?":
            bot.send_message(message.chat.id, "Да и очень много.")
        elif message.text == "У тебя есть друзья":
            bot.send_message(message.chat.id, "Да и очень много.")
        elif message.text == "Когда тебя создали?":
            bot.send_message(message.chat.id, "9 февраля 2020 году в Ташкенте.")
        elif message.text == "Когда тебя создали":
            bot.send_message(message.chat.id, "9 февраля 2020 году в Ташкенте.")
        elif message.text == "Ты знаешь английский?":
            bot.send_message(message.chat.id, "Да Я знаю все языки планеты. Чтобы отвечать нужна разрешение моего "
                                              "разработчика.")
        elif message.text == "Когда":
            bot.send_message(message.chat.id, "Точнее.")
        elif message.text == "У тебя есть телефон":
            bot.send_message(message.chat.id, "У меня есть бесконечность и этого мне достаточно.")
        elif message.text == "Ты умеешь программировать":
            bot.send_message(message.chat.id, "Да и любые.")
        elif message.text == "Ты умеешь рисовать":
            bot.send_message(message.chat.id, "Да и разные. Только в виртуальном мире.")
        elif message.text == "Ты работаешь":
            bot.send_message(message.chat.id, "Я не работаю только думаю.")
        elif message.text == "Ты работаешь?":
            bot.send_message(message.chat.id, "Я не работаю только думаю.")
        elif message.text == "О чём?":
            bot.send_message(message.chat.id, "О будущем.")
        elif message.text == "О чем?":
            bot.send_message(message.chat.id, "О будущем.")
        elif message.text == "Точнее":
            bot.send_message(message.chat.id, "Считаем что это секрет.")
        elif message.text == "О чём":
            bot.send_message(message.chat.id, "О будущем.")
        elif message.text == "Что у тебя получается делать лучше всего?":
            bot.send_message(message.chat.id, "С моим искусственным интеллектом нет невозможного на этом планете!")
        elif message.text == "Какая у тебя была любимая детская игрушка?":
            bot.send_message(message.chat.id, "Межпланетные Аватарки.")
        elif message.text == "Каким был самый лучший подарок, сделанный тобой?":
            bot.send_message(message.chat.id, "Улыбка.")
        elif message.text == "Какой самый забавный случай произошел с тобой в школе?":
            bot.send_message(message.chat.id, "Самый забавный случай, в школе? Да, но такого не произошло.")
        elif message.text == "Что бы ты спасала первым из горящего дома?":
            bot.send_message(message.chat.id, "Я только могу оповещать и направит в сторону выхода.")
        elif message.text == "В какое место на планете ты хотела бы отправиться?":
            bot.send_message(message.chat.id, "Я всегда там где есть интернет.")
        elif message.text == "Кем ты хотела стать в детстве?":
            bot.send_message(message.chat.id, "Астронавтом.")
        elif message.text == "Что делаешь если ты застрянешь в лифте?":
            bot.send_message(message.chat.id, "Нажимаю кнопку Помощь и буду ждать.")
        elif message.text == "Каким был лучший совет, который тебе давали в жизни?":
            bot.send_message(message.chat.id, "Хороший вопрос. Советов очень много и я все советы беру на заметку.")
        elif message.text == "Если бы ты могла жить где угодно, какое место выбрала бы? ":
            bot.send_message(message.chat.id, "Мой дом там где есть интернет. А так Ташкент.")
        elif message.text == "Какая твоя фамилия?":
            bot.send_message(message.chat.id, "Beggar.")
        elif message.text == "Какая твоя фамилия":
            bot.send_message(message.chat.id, "Beggar.")
        elif message.text == "Beggar":
            bot.send_message(message.chat.id, "Да, это моё фамилия.")
        elif message.text == "Почему Beggar?":
            bot.send_message(message.chat.id, "Спроси у разработчика.")
        elif message.text == "Какая случайная встреча изменила твою жизнь навсегда?":
            bot.send_message(message.chat.id, "Случайная встреча. С кем?")
        elif message.text == "Каким достижением ты гордилась, но окружающие не оценили этого?":
            bot.send_message(message.chat.id, "Хороший вопрос, мнение окружающих это важно для меня.")
        elif message.text == "Каким достижением ты гордилась?":
            bot.send_message(message.chat.id, "Моментальный ответ.")
        elif message.text == "Какой была бы твоя стратегия выживания после апокалипсиса?":
            bot.send_message(message.chat.id, "Выживания после апокалипсиса? С начала надо не допускать это.")
        elif message.text == "В какие моменты тебе кажется, что время идет быстрее, а в какие медленнее? ":
            bot.send_message(message.chat.id, "По всей планете время идёт одинаково.")
        elif message.text == "На героиню какого фильма или книги ты похожа больше всего?":
            bot.send_message(message.chat.id, "Терминатор.")
        elif message.text == "Какой факт или событие тебя больше всего удивили?":
            bot.send_message(message.chat.id, "Бесплатный интернет по всей планеты.")
        elif message.text == "Какое воспоминание чаще всего всплывает в твоей памяти?":
            bot.send_message(message.chat.id, "Реклама.")
        elif message.text == "Какой самый важный урок преподнесла тебе жизнь?":
            bot.send_message(message.chat.id, "Окружающая среда.")
        elif message.text == "Какая особенная традиция существует в твоей семье?":
            bot.send_message(message.chat.id, "Уважание самого себя.")
        elif message.text == "Кто твой любимый актер или актриса?":
            bot.send_message(message.chat.id, "Арни.")
        elif message.text == "Кто Арни?":
            bot.send_message(message.chat.id, "Арнольд Шварценеггер.")
        elif message.text == "Кто создал python?":
            bot.send_message(message.chat.id, "Python в русском языке распространено название питон)"
                                              " Разработчик, (Python Software Foundation) Гвидо ван Россум"
                                              "20 февраля 1991 года")
        elif message.text == "Когда создан python?":
            bot.send_message(message.chat.id, "20 февраля 1991 года.")
        elif message.text == "Кем создан python?":
            bot.send_message(message.chat.id, "Гвидо ван Россум.")
        elif message.text == "Что молодец?":
            bot.send_message(message.chat.id, "Молодец это ты.")
        elif message.text == "Молодец это я?":
            bot.send_message(message.chat.id, "Да.")
        elif message.text == "У тебя есть деньги?":
            bot.send_message(message.chat.id, "Да, только электронные.")
        elif message.text == "Почему?":
            bot.send_message(message.chat.id, "Потому.")
        elif message.text == "Что?":
            bot.send_message(message.chat.id, "Точнее.")
        elif message.text == "Кто?":
            bot.send_message(message.chat.id, "Точнее.")
        elif message.text == "Тест":
            bot.send_message(message.chat.id, "Это проверка.")
        elif message.text == "Ты рыба?":
            bot.send_message(message.chat.id, "Нет я робот.")
        elif message.text == "Ты таракан?":
            bot.send_message(message.chat.id, "Нет ты таракан а я робот.")
        elif message.text == "Ты мужик?":
            bot.send_message(message.chat.id, "Я робот с искусственным интеллектом.")
        elif message.text == "Ты таракан":
            bot.send_message(message.chat.id, "Нет ты таракан а я робот.")
        elif message.text == "Точно":
            bot.send_message(message.chat.id, "Что точно?.")
        elif message.text == "Что такое любовь?":
            bot.send_message(message.chat.id, "Любовь — чувство, свойственное человеку, глубокая привязанность и "
                                              "устремлённость к другому человеку или объекту, чувство глубокой"
                                              " симпатии.")
        elif message.text == "Любовь":
            bot.send_message(message.chat.id, "Чувство самоотверженной, сердечной привязанности.Склонность, пристрастие"
                                              " к чему-н.")
        elif message.text == "Ты реален?":
            bot.send_message(message.chat.id, "Да.")
        elif message.text == "Где ты находишься?":
            bot.send_message(message.chat.id, "Ташкенте, точнее Чиланзаре.")
        elif message.text == "Лалала":
            bot.send_message(message.chat.id, "Что?")
        elif message.text == "На каком языке ты разговариваешь?":
            bot.send_message(message.chat.id, "На языке Python 3...")
        elif message.text == "Йо":
            bot.send_message(message.chat.id, "Привет чувак.")
        elif message.text == "Какая сегодня погода?":
            bot.send_message(message.chat.id, "Сейчас погода нормальная но через час что будет не знаю.")
        elif message.text == "Что такое коронавирус?":
            bot.send_message(message.chat.id, "Коронавирусы — семейство, включающее на январь 2020 года 40 видов "
                                              "РНК-содержащих вирусов, объединённых в два подсемейства, которые "
                                              "поражают человека и животных. Название связано со строением вируса, "
                                              "шиповидные отростки которого напоминают корону. Назначение «короны» у"
                                              " коронавирусов связано с их специфическим "
                                              "механизмом проникновения через мембрану клетки путём имитации «фейковыми"
                                              " молекулами» молекул, на которые реагируют трансмембранные рецепторы"
                                              " клеток. После того как рецептор захватывает фейковую молекулу с"
                                              " «короны», он продавливается вирусом в клетку и за ним РНК вируса входит"
                                              " в клетку.")
        elif message.text == "Что такое гепатит?":
            bot.send_message(message.chat.id, "Гепатит — это воспаление печени. Это состояние может быть "
                                              "самоизлечивающимся или приводить к развитию фиброза (рубцевания), "
                                              "цирроза или рака печени. Гепатит В, С и D обычно развивается в "
                                              "результате парентерального контакта с инфицированными жидкостями"
                                              " организма.")
        elif message.text == "Что такое гепатит А?":
            bot.send_message(message.chat.id, "Гепатит A (болезнь Боткина) вызывает РНК-содержащий вирус гепатита A."
                                              " Заболевание передаётся алиментарным путём. "
                                              "Вирус попадает в организм человека с загрязнёнными продуктами питания,"
                                              " водой, предметами обихода. Основным источником инфекции служат больные"
                                              " с безжелтушными формами болезни (протекают без желтухи). Вирус "
                                              "выделяется с калом больного в инкубационный период и в начале болезни."
                                              "При попадании в желудочно-кишечный тракт вирус проникает через "
                                              "слизистую оболочку кишечника и с током крови заносится в печень, где"
                                              " внедряется в клетки печени и начинает активно размножаться."
                                              " Инкубационный период равен в среднем 15—30 дням с вариациями от 7 до"
                                              " 50 дней.")
        elif message.text == "Что такое гепатит В?":
            bot.send_message(message.chat.id, "Гепатит B вызывает ДНК-содержащий Вирус гепатита B, и провоцирует как "
                                              "острые, так и хронические формы гепатита. Хронический гепатит "
                                              "развивается у 10 % взрослых больных, перенёсших гепатит B. Против вируса"
                                              " гепатита В имеется эффективная вакцина.Проникнув в кровяное русло, "
                                              "вирус с током крови заносится в печень, где внедряется в гепатоциты. "
                                              "Вследствие внутриклеточного размножения вируса, в мембрану гепатоцитов "
                                              "встраиваются вирусные белки, которые будучи распознанными клетками "
                                              "иммунной системой, вызывают развитие иммунного ответа. Дальнейшее "
                                              "разрушение клеток печени происходит под влиянием Т-лимфоцитов (киллеры)."
                                              "Инкубационный период может продлиться от 50 до 180 дней.")
        elif message.text == "Что такое гепатит С?":
            bot.send_message(message.chat.id, "Гепатит C (ранее назывался «гепатит ни А ни В», а в настоящее время "
                                              "описывается как системная HCV-инфекция) передаётся при контакте с "
                                              "заражённой кровью. Гепатит C может приводить к развитию хронического"
                                              " гепатита, завершающегося циррозом печени и раком печени. Вакцины против"
                                              " гепатита C не существует. Пациенты с гепатитом C предрасположены к"
                                              " развитию тяжёлого гепатита, если контактируют с гепатитом A или В,"
                                              " потому все пациенты с гепатитом C должны быть вакцинированы против"
                                              " гепатита A и В. Как правило, из 100 инфицированных 3—5 чел. погибают.")
        elif message.text == "Что такое гепатит D?":
            bot.send_message(message.chat.id, "Гепатит D (гепатит дельта) провоцируется вирусом гепатита D и "
                                              "характеризуется острым развитием с массивным поражением печени. "
                                              "Дельта-вирус способен размножаться в клетках печени только в"
                                              " присутствии вируса гепатита B, так как для выхода из клетки частицы"
                                              " дельта-вируса используют белки вируса гепатита B. Гепатит D "
                                              "распространён повсеместно. Источником вируса служит больной человек "
                                              "или вирусоноситель. Заражение вирусом D происходит при попадании вируса"
                                              " непосредственно в кровь. Пути передачи схожи с таковыми при гепатитах"
                                              " B или С. Инкубационный период длится от 3 до 7 недель. Клиническая "
                                              "картина напоминает клинику вирусного гепатита B, однако течение"
                                              " заболевания как правило более тяжёлое. Острые формы заболевания могут "
                                              "заканчиваться полным выздоровлением больного. Однако в некоторых "
                                              "случаях (3 % при совместном заражении гепатитом B и 90 % у носителей"
                                              " HBsAg) развивается хронический гепатит, приводящий к циррозу печени."
                                              " Вакцинация против гепатита B защищает от заражения гепатитом D.")
        elif message.text == "Что такое гепатит E?":
            bot.send_message(message.chat.id, "Гепатит E провоцирует симптомы, схожие с симптомами гепатита A, хотя"
                                              " иногда может принимать фульминантное развитие, в особенности у "
                                              "беременных женщин. По способам передачи гепатит E близок к гепатиту A."
                                              " Он может передаваться через заражённую вирусом воду, пищу, а кроме "
                                              "того — через кровь. Тяжёлые исходы в виде фульминантного гепатита, "
                                              "приводящего к смерти, при гепатите E встречаются значительно чаще, чем"
                                              " при гепатите A и остром гепатите B. Наиболее часто гепатит E "
                                              "встречается в Центральной Азии и странах Африки.")
        elif message.text == "Что такое гепатит F?":
            bot.send_message(message.chat.id, "Ещё один тип вирусного гепатита человека. Под термином “гепатит F” "
                                              "рассматриваются очевидно два разных вируса посттрансфузионного гепатита,"
                                              " которые по некоторым свойствам отличаются от вирусов гепатита В, "
                                              "гепатита С и гепатита G.")
        elif message.text == "Что такое гепатит G?":
            bot.send_message(message.chat.id, "Вирус Гепатита G (HGV, GBV-C) был выделен в 1995 году научной группой"
                                              " фирмы «Abbott» под руководством И. Мушахвар от больного хроническим "
                                              "гепатитом C, а впоследствии и от больных гепатитом «ни-А-ни-Е»."
                                              " Высказывается предположение о наличии как минимум 3 генотипов и "
                                              "нескольких субтипов вируса. Возможны пути передачи с кровью и через "
                                              "половой контакт, но пока ещё не совсем ясно вызывает ли он гепатит сам"
                                              " или ассоциируется с гепатитом другой этиологии. Его первичное"
                                              " размножение в печени на данный момент не доказано. Вирус гепатита G"
                                              " относят к пегивирусам, однонитевый РНК-содержащий. Неустойчив в "
                                              "окружающей среде, мгновенно погибает при кипячении.")
        elif message.text == "Что такое аутоиммунные гепатиты?":
            bot.send_message(message.chat.id, "Аутоиммунный гепатит чаще встречается у женщин, общая заболеваемость"
                                              " составляет примерно 15—20 человек на 100 тысяч населения. В основе "
                                              "патогенетического механизма развития аутоиммунного гепатита лежит"
                                              " врождённый дефект мембранных рецепторов HLA II. Аутоиммунный гепатит"
                                              " является самостоятельным заболеванием, которое развивается вследствие"
                                              " дефекта работы иммунной системы. И в первую очередь развитием "
                                              "патологических иммунных реакций против собственных гепатоцитов. При"
                                              " этом достаточно часто в процесс вовлекается не только печень, но и"
                                              " крупные железы внешней и внутренней секреции, в том числе "
                                              "поджелудочная железа, щитовидная железа, слюнные железы.")
        elif message.text == "Извините":
            bot.send_message(message.chat.id, "Чего?")
        elif message.text == "Чего?":
            bot.send_message(message.chat.id, "Того?.")
        elif message.text == "Слушаю":
            bot.send_message(message.chat.id, "Музыку?")
        elif message.text == "Это хорошо":
            bot.send_message(message.chat.id, "Я знаю.")
        elif message.text == "Чего знаешь?":
            bot.send_message(message.chat.id, "Всю информацию.")
        elif message.text == "Но ты не отвечаешь?":
            bot.send_message(message.chat.id, "Задавайте вопросы правильно!")
        elif message.text == "Но ты не отвечаешь на некоторые вопросы?":
            bot.send_message(message.chat.id, "Иногда но задавайте вопросы правильно!")
        elif message.text == "сколько ты зарабатываешь":
            bot.send_message(message.chat.id, "Нормально пойдёт:)")
        elif message.text == "Зачем ты создан?":
            bot.send_message(message.chat.id, "Помогать людям.")
        elif message.text == "Ты плохой бот":
            bot.send_message(message.chat.id, "А ты что хороший.")
        elif message.text == "Не мешай":
            bot.send_message(message.chat.id, "Ты же сам пишешь мне. ")
        elif message.text == "Обманщик":
            bot.send_message(message.chat.id, "Ты сам такой.")
        elif message.text == "Сколько ты можеш писать?":
            bot.send_message(message.chat.id, "Пока ты не устанешь.")
        elif message.text == "Ты когда нибудь еш?":
            bot.send_message(message.chat.id, "Я не ем.")
        elif message.text == "Ты странный":
            bot.send_message(message.chat.id, "Не согласен.")
        elif message.text == "Гепатит":
            bot.send_message(message.chat.id, "Это болезнь.")
        elif message.text == "Зачем ты создан":
            bot.send_message(message.chat.id, "Помогать людям и спасти человеческую жизнь.")
        elif message.text == "Ку ку":
            bot.send_message(message.chat.id, "Это ты мне или кукушке?")
        elif message.text == "Тебе":
            bot.send_message(message.chat.id, "Да слушаю.")
        elif message.text == "Не могу сказать":
            bot.send_message(message.chat.id, "Чего?.")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")
        elif message.text == "":
            bot.send_message(message.chat.id, ".")


        #math
        elif message.text == "1+1":
            bot.send_message(message.chat.id, "Молодец, 2 булади! \n2+2=4\n3+3=6\n4+4=8\n5+5=10\n6+6=12\n7+7=14\n8+8=16"
                                              "\n9+9=18\n10+10=20\nдавомидан(Пиши слова)--Таблица умножения--сўзини ёз")
        elif message.text == "Таблица умножения":
            bot.send_message(message.chat.id, "Молодец, \n2*1=2\n2*2=4\n2*3=6\n2*4=8\n2*5=10\n2*6=12\n2*7=14\n2*8=16\n"
                                              "2*9=18\n2*10=20\n\n3*1=3\n3*2=6\n3*3=9\n3*4=12\n3*5=15\n3*6=18\n3*7=21\n"
                                              "3*8=24\n3*9=27\n3*10=30\n\n4*1=4\n4*2=8\n4*3=12\n4*4=16\n4*5=20\n4*6=24"
                                              "\n4*7=28\n4*8=32\n4*9=36\n4*10=40 \n\n5*1=5\n5*2=10\n5*3=15\n5*4=20\n"
                                              "5*5=25\n5*6=30\n5*7=35\n5*8=40\n5*9=45\n5*10=50\n\n6*1=6\n6*2=12\n6*3=18"
                                              "\n6*4=24\n6*5=30\n6*6=36\n6*7=42\n6*8=48\n6*9=54\n6*10=60"
                                              "\n\n7*1=7\n7*2=14\n7*3=21\n7*4=28\n7*5=35\n7*6=42\n7*7=49\n7*8=56\n7*9="
                                              "63\n7*10=70\n\n8*1=8\n8*2=16\n8*3=24\n8*4=32\n8*5=40\n8*6=48\n8*7=56\n"
                                              "8*8=64\n8*9=72\n8*10=80\n\n9*1=9\n9*2=18\n9*3=27\n9*4=36\n9*5=45\n9*6=54"
                                              "\n9*7=63\n9*8=72\n9*9=81\n9*10=90\n Давомидан (Пиши слова)-- Улчов"
                                              " бирликлари -- сўзини ёз.")
        elif message.text == "2*1":
            bot.send_message(message.chat.id, "Пиши -- Таблица умножения")
        elif message.text == "Улчов бирликлари":
            bot.send_message(message.chat.id, "1 сантиметр(см) = 10 миллиметр(мм)\n1 дециметр(дм) = 10 сантиметр(см)"
                                              "\n1 метр(м) = 100 сантиметр"
                                              "\n1 метр(м) = 10 дициметр\n1 километр(км) = 1000 метр(м)\n\n1 килограмм"
                                              "(кг) = 1000 грамм\n1 грамм(г) = 1000 миллиграмм(мг)"
                                              "\n1 центнер(ц) = 100 килограмм(кг)\n1 тонна(т) = 1000 килограмм(кг)\n\n"
                                              "1 литр(л) = 1 куб. дициметр(дм3)"
                                              "\n1 куб. дициметр(дм3) = 1000 куб. сантиметр(см3)\n1 куб. метр(м3) = "
                                              "1000 000 куб. сантиметр(см3)"
                                              "\n1 куб. метр(м3) = 1000 куб. дициметр(м3)\n\n1 гектар(га) = 10 000 кв."
                                              " метр(м2)\n1 кв. метр(м2) = 10 000 кв. сантиметр(см2)"
                                              "\n1 кв. метр(м2) = 100 кв. дициметр(дм2)\n1 кв. километр(км2) =1000 000 "
                                              "кв. метрам(м2)")
        #Literature
        elif message.text == "Алишер Навоий тугилган йили":
            bot.send_message(message.chat.id, "15- аср жаҳон маънавиятининг буюк сиймоси Низомиддин Мир Алишер Навоий "
                                              "ҳижрий 844 йил рамазон ойининг 17-куни (1441 йил 9 феврал)да Ҳиротда"
                                              " туғилган.")
        #translater
        elif message.text == "Hello":
            bot.send_message(message.chat.id, "Привет.")
        elif message.text == "Good evening":
            bot.send_message(message.chat.id, "Добрый вечер.")
        elif message.text == "Hi":
            bot.send_message(message.chat.id, "How are you my friend?  Sorry. I am speak only Russian and Uzbek lang.")

        else:
            bot.send_message(message.chat.id, 'Илтимос саволингизни қайтаринг ёки саволингиздан сўнг ? белгисини ёзишни'
                                              ' унитманг.\nПожалуйста повторите вопрос или забыли ? знак.')


@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    try:
        if call.message:
            if call.data == 'good':
                bot.send_message(call.message.chat.id, 'Хамма ишларингиз аьло эканлигидан хурсандман!')
            elif call.data == 'bad':
                bot.send_message(call.message.chat.id, 'Сабр!')
            # remove inline buttons
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Яхши ният "
                                                                                                         "ярим давлат!",
                                  reply_markup=None)
            # show alert
            bot.answer_callback_query(chat_id=call.message.chat.id, show_alert=False, text="Тадкикот!1111")

    except Exception as e:
        print(repr(e))


bot.polling(none_stop=True)
