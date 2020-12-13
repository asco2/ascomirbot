import telebot
import config
import random

from telebot import types

bot = telebot.TeleBot(config.TOKEN)

@bot.message_handler(commands=['start'])
def welcome(message):
    sti = open('static/welcome.tgs', 'rb')
    bot.send_sticker(message.chat.id, sti)

    # keyboard
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton("😊Как дела?")
    item2 = types.KeyboardButton("🤗Поиск аниме")
    item3 = types.KeyboardButton("Чего хотят мои создатели👨🏻‍💻")

    markup.add(item1, item2, item3)

    bot.send_message(message.chat.id, "Добро пожаловать,{0.first_name}!\nЯ - <b>{1.first_name}</b>, бот созданный чтобы быть вашей слугой.".format(message.from_user, bot.get_me()), parse_mode='html', reply_markup=markup)

@bot.message_handler(content_types=['text'])
def lalala(message):
    if message.chat.type == 'private':
        if  message.text == '😊Как дела?':
            markup = types.InlineKeyboardMarkup(row_width=2)
            item1 = types.InlineKeyboardButton("Хорошо", callback_data='good')
            item2 = types.InlineKeyboardButton("Не очень", callback_data='bad')
 
            markup.add(item1, item2)
 
            bot.send_message(message.chat.id, 'Отлично,хозяин вы как?', reply_markup=markup)

        elif message.text == '🤗Поиск аниме':
            bot.send_message(message.chat.id, 'Хорошо сейчас найдем!')            
            markup = types.InlineKeyboardMarkup()
            item1 = btn_my_site = types.InlineKeyboardButton(text='Атака титанов', url='https://yummyanime.club/catalog/item/vtorzhenie-gigantov')
            markup.add(btn_my_site)
            item2 = btn_my_site = types.InlineKeyboardButton(text='Город, в котором меня нет', url='https://yummyanime.club/catalog/item/gorod-v-kotorom-menya-net')
            markup.add(btn_my_site)
            item3 = btn_my_site = types.InlineKeyboardButton(text='Тетрадь Смерти', url='https://yummyanime.club/catalog/item/tetrad-smerti')
            markup.add(btn_my_site)
            item4 = btn_my_site = types.InlineKeyboardButton(text='Вайолет Эвергарден', url='https://yummyanime.club/catalog/item/vajolet-evergarden')
            markup.add(btn_my_site)
            item5 = btn_my_site = types.InlineKeyboardButton(text='Клинок, рассекающий демонов', url='https://yummyanime.club/catalog/item/klinok-rassekayushij-demonov')
            markup.add(btn_my_site)
            item6 = btn_my_site = types.InlineKeyboardButton(text='Наруто: Ураганные хроники', url='https://yummyanime.club/catalog/item/naruto-uragannye-hroniki')
            markup.add(btn_my_site)
            item7 = btn_my_site = types.InlineKeyboardButton(text='Паразит - Учение о жизни', url='https://yummyanime.club/catalog/item/parazit-uchenie-o-zhizni')
            markup.add(btn_my_site)
            item8 = btn_my_site = types.InlineKeyboardButton(text='Волейбол!!', url='https://yummyanime.club/catalog/item/volejbol-tv-1')
            markup.add(btn_my_site)
            item9 = btn_my_site = types.InlineKeyboardButton(text='Резонанс Ужаса', url='https://yummyanime.club/catalog/item/rezonans-uzhasa')
            markup.add(btn_my_site)
            item10 = btn_my_site = types.InlineKeyboardButton(text='Владыка', url='https://yummyanime.club/catalog/item/vladyka')
            markup.add(btn_my_site)
            bot.send_message(message.chat.id, "Выберите аниме хозяин", reply_markup = markup)

        elif message.text == 'Чего хотят мои создатели👨🏻‍💻':
            bot.send_message(message.chat.id, 'Мои создатели хотят что бы вы поставили им хорошую оценку')
            sti = open('static/Anime.tgs', 'rb')
            bot.send_sticker(message.chat.id, sti)

        else:
            bot.send_message(message.chat.id,'Я не знаю что ответить хозяин 😢')
    
@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    try:
        if call.message:
            if call.data == 'good':
                bot.send_message(call.message.chat.id, 'Вот и отличненько 😊')
            elif call.data == 'bad':
                bot.send_message(call.message.chat.id, 'Бывает 😢')

              # remove inline buttons
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="😊 Как дела?",
                reply_markup=None)
 
            # show alert
            bot.answer_callback_query(callback_query_id=call.id, show_alert=False,
                text="Господин где вы!😰")
 
    except Exception as e:
        print(repr(e))
 
# RUN
bot.polling(none_stop=True)
