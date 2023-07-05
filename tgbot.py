
import telebot
from telebot import types
import random
import sqlite3

bot = telebot.TeleBot('')


@bot.message_handler(commands=['start'])
def start(message):
    connect = sqlite3.connect('users.db')
    cursor = connect.cursor()
    cursor.execute("""CREATE TABLE IF NOT EXISTS login_id(
            id INTEGER,
            wins INTEGER
        )""")
    connect.commit()
    users_data = [message.chat.id, 0]
    cursor.execute("INSERT INTO login_id (id, wins) VALUES (?, ?)", users_data)
    connect.commit()

    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    Contacts = types.KeyboardButton('Контакты')
    Donate = types.KeyboardButton('Донат')
    Random_New_Music = types.KeyboardButton('❌Крестики-Нолики⭕')
    markup.add(Contacts, Donate, Random_New_Music)
    msg = bot.send_message(message.chat.id,
                           f'<b><i>Меню открыто</i></b>',
                           parse_mode='html', reply_markup=markup)
    bot.register_next_step_handler(msg, text)


a1, a2, a3 = types.InlineKeyboardButton('⬜️', callback_data='1'), types.InlineKeyboardButton('⬜️',
                                                                                             callback_data='2'), types.InlineKeyboardButton(
    '⬜️', callback_data='3')
a4, a5, a6 = types.InlineKeyboardButton('⬜️', callback_data='4'), types.InlineKeyboardButton('⬜️',
                                                                                             callback_data='5'), types.InlineKeyboardButton(
    '⬜️', callback_data='6')
a7, a8, a9 = types.InlineKeyboardButton('⬜️', callback_data='7'), types.InlineKeyboardButton('⬜️',
                                                                                             callback_data='8'), types.InlineKeyboardButton(
    '⬜️', callback_data='9')
spisok_knopok = [a1, a2, a3, a4, a5, a6, a7, a8, a9]
lose = 0
moves_comp = []
moves_player = []
combination = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [1, 4, 7], [2, 5, 8], [3, 6, 9], [1, 5, 9], [3, 5, 7]]


def spisok():
    global spisok_knopok, a1, a2, a3, a4, a5, a6, a7, a8, a9, moves_player, moves_comp
    a1, a2, a3 = types.InlineKeyboardButton('⬜️', callback_data='1'), types.InlineKeyboardButton('⬜️',
                                                                                                 callback_data='2'), types.InlineKeyboardButton(
        '⬜️', callback_data='3')
    a4, a5, a6 = types.InlineKeyboardButton('⬜️', callback_data='4'), types.InlineKeyboardButton('⬜️',
                                                                                                 callback_data='5'), types.InlineKeyboardButton(
        '⬜️', callback_data='6')
    a7, a8, a9 = types.InlineKeyboardButton('⬜️', callback_data='7'), types.InlineKeyboardButton('⬜️',
                                                                                                 callback_data='8'), types.InlineKeyboardButton(
        '⬜️', callback_data='9')
    spisok_knopok = [a1, a2, a3, a4, a5, a6, a7, a8, a9]
    moves_comp = []
    moves_player = []
    return spisok_knopok


@bot.message_handler(content_types=['text'])
def text(message):
    if message.text == 'Контакты':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        telegram = types.KeyboardButton('telegram')
        vk = types.KeyboardButton('vk')
        back = types.KeyboardButton('↩Назад')
        markup.add(telegram, vk, back)
        bot.send_message(message.chat.id, 'Выберите способ обратной связи', reply_markup=markup)
    elif message.text == 'telegram':
        bot.send_message(message.chat.id, 'https://t.me/blackcolday')
    elif message.text == 'vk':
        bot.send_message(message.chat.id, 'https://vk.com/blackcolday')
    elif message.text == 'Донат':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        Sber = types.KeyboardButton('Сбер')
        Tinkoff = types.KeyboardButton('Тинькофф')
        back = types.KeyboardButton('↩Назад')
        markup.add(Sber, Tinkoff, back)
        bot.send_message(message.chat.id, 'Выберите банк', reply_markup=markup)
    elif message.text == '↩Назад':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        Contacts = types.KeyboardButton('Контакты')
        Donate = types.KeyboardButton('Донат')
        Random_New_Music = types.KeyboardButton('❌Крестики-Нолики⭕')
        markup.add(Contacts, Donate, Random_New_Music)
        bot.send_message(message.chat.id, f'<b><i>Вы вернулись в Главное Меню</i></b>', reply_markup=markup,
                         parse_mode='html')
    elif message.text == '❌Крестики-Нолики⭕':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        Yes = types.KeyboardButton('Да!')
        No = types.KeyboardButton('Нет')
        markup.add(Yes, No)
        bot.send_message(message.chat.id, 'Вы уверены, что хотите начать?', reply_markup=markup)
    elif message.text == 'Нет':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        Contacts = types.KeyboardButton('Контакты')
        Donate = types.KeyboardButton('Донат')
        Random_New_Music = types.KeyboardButton('❌Крестики-Нолики⭕')
        markup.add(Contacts, Donate, Random_New_Music)
        bot.send_message(message.chat.id, f'<b><i>Вы вернулись в Главное Меню</i></b>', reply_markup=markup,
                         parse_mode='html')
    if message.text == 'Да!':
        spisok()
        backkk = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
        back_get = types.KeyboardButton('↩Назад')
        backkk.add(back_get)
        bot.send_message(message.chat.id, 'Начинаем!', reply_markup=backkk)
        markup = types.InlineKeyboardMarkup(row_width=3)
        a1, a2, a3 = types.InlineKeyboardButton('⬜️', callback_data='1'), types.InlineKeyboardButton('⬜️',
                                                                                                     callback_data='2'), types.InlineKeyboardButton(
            '⬜️', callback_data='3')
        a4, a5, a6 = types.InlineKeyboardButton('⬜️', callback_data='4'), types.InlineKeyboardButton('⬜️',
                                                                                                     callback_data='5'), types.InlineKeyboardButton(
            '⬜️', callback_data='6')
        a7, a8, a9 = types.InlineKeyboardButton('⬜️', callback_data='7'), types.InlineKeyboardButton('⬜️',
                                                                                                     callback_data='8'), types.InlineKeyboardButton(
            '⬜️', callback_data='9')
        markup.add(a1, a2, a3, a4, a5, a6, a7, a8, a9)
        bot.send_message(message.chat.id, 'Вы: ⭕', reply_markup=markup)


def comp(x):
    global a1, a2, a3, a4, a5, a6, a7, a8, a9, moves_comp
    if x == a1:
        moves_comp.append(1)
        a1 = types.InlineKeyboardButton('❌', callback_data='comp1')
    if x == a2:
        a2 = types.InlineKeyboardButton('❌', callback_data='comp2')
        moves_comp.append(2)
        return a2
    if x == a3:
        a3 = types.InlineKeyboardButton('❌', callback_data='comp3')
        moves_comp.append(3)
        return a3
    if x == a4:
        moves_comp.append(4)
        a4 = types.InlineKeyboardButton('❌', callback_data='comp4')
        return a4
    if x == a5:
        moves_comp.append(5)
        a5 = types.InlineKeyboardButton('❌', callback_data='comp5')
        return a5
    if x == a6:
        moves_comp.append(6)
        a6 = types.InlineKeyboardButton('❌', callback_data='comp6')
        return a6
    if x == a7:
        moves_comp.append(7)
        a7 = types.InlineKeyboardButton('❌', callback_data='comp7')
        return a7
    if x == a8:
        moves_comp.append(8)
        a8 = types.InlineKeyboardButton('❌', callback_data='comp8')
        return a8
    if x == a9:
        moves_comp.append(9)
        a9 = types.InlineKeyboardButton('❌', callback_data='comp9')
        return a9


@bot.callback_query_handler(func=lambda call: True)
def callback(call):
    def win(x):
        global a1, a2, a3, a4, a5, a6, a7, a8, a9, spisok_knopok, lose, moves_player, moves_comp
        if len(moves_player) >= 3:
            for i in combination:
                if set(moves_player) & set(i) == set(i):
                    wins = 1
                    a1, a2, a3 = types.InlineKeyboardButton('⬜️', callback_data='1'), types.InlineKeyboardButton('⬜️',
                                                                                                         callback_data='2'), types.InlineKeyboardButton(
                    '⬜️', callback_data='3')
                    a4, a5, a6 = types.InlineKeyboardButton('⬜️', callback_data='4'), types.InlineKeyboardButton('⬜️',
                                                                                                         callback_data='5'), types.InlineKeyboardButton(
                    '⬜️', callback_data='6')
                    a7, a8, a9 = types.InlineKeyboardButton('⬜️', callback_data='7'), types.InlineKeyboardButton('⬜️',
                                                                                                         callback_data='8'), types.InlineKeyboardButton(
                    '⬜️', callback_data='9')
                    spisok_knopok = [a1, a2, a3, a4, a5, a6, a7, a8, a9]
                    connect = sqlite3.connect('users.db')
                    cursor = connect.cursor()
                    cursor.execute("UPDATE login_id SET wins = wins + ? WHERE id = ?", (wins, call.message.chat.id,))
                    connect.commit()
                    cursor.execute('SELECT * FROM login_id')
                    connect.commit()
                    wins_bd = cursor.fetchall()
                    for x in wins_bd:
                        if x[0] == call.message.chat.id:
                            return bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                         text=f'<b>Вы победили!🥳</b>\nПобед: {x[1]}', parse_mode='html')

                if set(moves_comp) & set(i) == set(i):
                    a1, a2, a3 = types.InlineKeyboardButton('⬜️', callback_data='1'), types.InlineKeyboardButton('⬜️',
                                                                                                                 callback_data='2'), types.InlineKeyboardButton(
                        '⬜️', callback_data='3')
                    a4, a5, a6 = types.InlineKeyboardButton('⬜️', callback_data='4'), types.InlineKeyboardButton('⬜️',
                                                                                                                 callback_data='5'), types.InlineKeyboardButton(
                        '⬜️', callback_data='6')
                    a7, a8, a9 = types.InlineKeyboardButton('⬜️', callback_data='7'), types.InlineKeyboardButton('⬜️',
                                                                                                                 callback_data='8'), types.InlineKeyboardButton(
                        '⬜️', callback_data='9')
                    spisok_knopok = [a1, a2, a3, a4, a5, a6, a7, a8, a9]
                    return bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                                 text=f'<b>Вы проиграли!☹️</b>', parse_mode='html')

            else:
                return None

        else:
            return None
    if call.message:
        global markup, a1, a2, a3, a4, a5, a6, a7, a8, a9, spisok_knopok, wins, lose, moves_player, moves_comp
        if call.data == '1':
            a1 = types.InlineKeyboardButton('⭕', callback_data='-1')
            moves_player.append(1)
            markup = types.InlineKeyboardMarkup(row_width=3)
            for i in range(len(spisok_knopok)):
                if spisok_knopok[i].callback_data == '1':
                    del spisok_knopok[i]
                    break
            if spisok_knopok == [] and win(spisok_knopok) == None:
                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text='Ничья!',)
            elif win(spisok_knopok) == None:
                computer_move = random.randint(0, len(spisok_knopok) - 1)
                for i in range(len(spisok_knopok)):
                    if i == computer_move:
                        comp(spisok_knopok[i])
                        del spisok_knopok[i]
                        break
                if win(spisok_knopok) == None:
                    markup.add(a1, a2, a3, a4, a5, a6, a7, a8, a9)
                    bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text='Вы: ⭕',
                                      reply_markup=markup)


        if call.data == '2':
            a2 = types.InlineKeyboardButton('⭕', callback_data='-2')
            moves_player.append(2)
            markup = types.InlineKeyboardMarkup(row_width=3)
            for i in range(len(spisok_knopok)):
                if spisok_knopok[i].callback_data == '2':
                    del spisok_knopok[i]
                    break
            if spisok_knopok == [] and win(spisok_knopok) == None:
                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text='Ничья!', )
            elif win(spisok_knopok) == None:
                computer_move = random.randint(0, len(spisok_knopok) - 1)
                for i in range(len(spisok_knopok)):
                    if i == computer_move:
                        comp(spisok_knopok[i])
                        del spisok_knopok[i]
                        break
                if win(spisok_knopok) == None:
                    markup.add(a1, a2, a3, a4, a5, a6, a7, a8, a9)
                    bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                          text='Вы: ⭕',
                                          reply_markup=markup)
        if call.data == '3':
            moves_player.append(3)
            a3 = types.InlineKeyboardButton('⭕', callback_data='-3')
            markup = types.InlineKeyboardMarkup(row_width=3)
            for i in range(len(spisok_knopok)):
                if spisok_knopok[i].callback_data == '3':
                    del spisok_knopok[i]
                    break
            if spisok_knopok == [] and win(spisok_knopok) == None:
                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text='Ничья!', )
            elif win(spisok_knopok) == None:
                computer_move = random.randint(0, len(spisok_knopok) - 1)
                for i in range(len(spisok_knopok)):
                    if i == computer_move:
                        comp(spisok_knopok[i])
                        del spisok_knopok[i]
                        break
                if win(spisok_knopok) == None:
                    markup.add(a1, a2, a3, a4, a5, a6, a7, a8, a9)
                    bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                          text='Вы: ⭕',
                                          reply_markup=markup)

        if call.data == '4':
            moves_player.append(4)
            a4 = types.InlineKeyboardButton('⭕', callback_data='-4')
            markup = types.InlineKeyboardMarkup(row_width=3)
            for i in range(len(spisok_knopok)):
                if spisok_knopok[i].callback_data == '4':
                    del spisok_knopok[i]
                    break
            if spisok_knopok == [] and win(spisok_knopok) == None:
                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text='Ничья!', )
            elif win(spisok_knopok) == None:
                computer_move = random.randint(0, len(spisok_knopok) - 1)
                for i in range(len(spisok_knopok)):
                    if i == computer_move:
                        comp(spisok_knopok[i])
                        del spisok_knopok[i]
                        break
                if win(spisok_knopok) == None:
                    markup.add(a1, a2, a3, a4, a5, a6, a7, a8, a9)
                    bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                          text='Вы: ⭕',
                                          reply_markup=markup)

        if call.data == '5':
            moves_player.append(5)
            a5 = types.InlineKeyboardButton('⭕', callback_data='-5')
            markup = types.InlineKeyboardMarkup(row_width=3)
            for i in range(len(spisok_knopok)):
                if spisok_knopok[i].callback_data == '5':
                    del spisok_knopok[i]
                    break
            if spisok_knopok == [] and win(spisok_knopok) == None:
                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text='Ничья!', )
            elif win(spisok_knopok) == None:
                computer_move = random.randint(0, len(spisok_knopok) - 1)
                for i in range(len(spisok_knopok)):
                    if i == computer_move:
                        comp(spisok_knopok[i])
                        del spisok_knopok[i]
                        break
                if win(spisok_knopok) == None:
                    markup.add(a1, a2, a3, a4, a5, a6, a7, a8, a9)
                    bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                          text='Вы: ⭕',
                                          reply_markup=markup)
        if call.data == '6':
            moves_player.append(6)
            a6 = types.InlineKeyboardButton('⭕', callback_data='-6')
            markup = types.InlineKeyboardMarkup(row_width=3)
            for i in range(len(spisok_knopok)):
                if spisok_knopok[i].callback_data == '6':
                    del spisok_knopok[i]
                    break
            if spisok_knopok == [] and win(spisok_knopok) == None:
                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text='Ничья!', )
            elif win(spisok_knopok) == None:
                computer_move = random.randint(0, len(spisok_knopok) - 1)
                for i in range(len(spisok_knopok)):
                    if i == computer_move:
                        comp(spisok_knopok[i])
                        del spisok_knopok[i]
                        break
                if win(spisok_knopok) == None:
                    markup.add(a1, a2, a3, a4, a5, a6, a7, a8, a9)
                    bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                          text='Вы: ⭕',
                                          reply_markup=markup)

        if call.data == '7':
            moves_player.append(7)
            a7 = types.InlineKeyboardButton('⭕', callback_data='-7')
            markup = types.InlineKeyboardMarkup(row_width=3)
            for i in range(len(spisok_knopok)):
                if spisok_knopok[i].callback_data == '7':
                    del spisok_knopok[i]
                    break
            if spisok_knopok == [] and win(spisok_knopok) == None:
                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text='Ничья!', )
            elif win(spisok_knopok) == None:
                computer_move = random.randint(0, len(spisok_knopok) - 1)
                for i in range(len(spisok_knopok)):
                    if i == computer_move:
                        comp(spisok_knopok[i])
                        del spisok_knopok[i]
                        break
                if win(spisok_knopok) == None:
                    markup.add(a1, a2, a3, a4, a5, a6, a7, a8, a9)
                    bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                          text='Вы: ⭕',
                                          reply_markup=markup)

        if call.data == '8':
            moves_player.append(8)
            a8 = types.InlineKeyboardButton('⭕', callback_data='-8')
            markup = types.InlineKeyboardMarkup(row_width=3)
            for i in range(len(spisok_knopok)):
                if spisok_knopok[i].callback_data == '8':
                    del spisok_knopok[i]
                    break
            if spisok_knopok == [] and win(spisok_knopok) == None:
                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text='Ничья!', )
            elif win(spisok_knopok) == None:
                computer_move = random.randint(0, len(spisok_knopok) - 1)
                for i in range(len(spisok_knopok)):
                    if i == computer_move:
                        comp(spisok_knopok[i])
                        del spisok_knopok[i]
                        break
                if win(spisok_knopok) == None:
                    markup.add(a1, a2, a3, a4, a5, a6, a7, a8, a9)
                    bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                          text='Вы: ⭕',
                                          reply_markup=markup)

        if call.data == '9':
            moves_player.append(9)
            a9 = types.InlineKeyboardButton('⭕', callback_data='-9')
            markup = types.InlineKeyboardMarkup(row_width=3)
            for i in range(len(spisok_knopok)):
                if spisok_knopok[i].callback_data == '9':
                    del spisok_knopok[i]
                    break
            if spisok_knopok == [] and win(spisok_knopok) == None:
                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text='Ничья!', )
            elif win(spisok_knopok) == None:
                computer_move = random.randint(0, len(spisok_knopok) - 1)
                for i in range(len(spisok_knopok)):
                    if i == computer_move:
                        comp(spisok_knopok[i])
                        del spisok_knopok[i]
                        break
                if win(spisok_knopok) == None:
                    markup.add(a1, a2, a3, a4, a5, a6, a7, a8, a9)
                    bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                          text='Вы: ⭕',
                                          reply_markup=markup)



bot.polling(none_stop=True)
