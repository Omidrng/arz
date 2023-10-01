import telebot
import requests
import json

botapi = "6504932578:AAFCZwWak66yffTTr6Rm_-huAlMoJ8Jv7rA"

support = "گذارش مشکل:\n@DevNasa"

welcome = "به بات قیمت لحظه ای ارز ها خوش آمدید.\nیکی از گزینه های زیر را انتخاب کنید:"

r = requests.get("https://www.tgju.org/?act=sanarateservice&client=tgju&noview&type=json")
f = r.text

y = json.loads(f)

for i in range(1):
    a = y['sana_buy_usd']['price']
    d = y['sana_sell_usd']['price']
    c = y['sana_buy_eur']['price']
    e = y['sana_sell_eur']['price']
    x = y['sana_buy_aed']['price']
    h = y['sana_sell_aed']['price']
buy = 'قیمت لحظه ای خرید '
sell = 'قیمت لحظه ای فروش '
base = ' ریال'
finish = ": "

usdt = "دلار"
eur = "یورو"
aed = "درهم"

usdtbuy = buy + usdt + finish + str(a) + base
usdtsell = sell + usdt + finish + str(d) + base

aedbuy = buy + aed + finish + str(x) + base
aedsell = sell + aed + finish + str(h) + base

eurbuy = buy + eur + finish + str(c) + base
eursell = sell + eur + finish + str(e) + base





windows_amoozesh = telebot.types.InlineKeyboardButton("چنل اسپانسر", url="https://t.me/omidnetworkk")
amoozesh_service = telebot.types.InlineKeyboardMarkup(row_width=1)
amoozesh_service.add(windows_amoozesh)






bot = telebot.TeleBot(botapi)

keyboard_buttons_start = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
keyboard_buttons_start.add("قیمت لحظه ای خرید دلار", "قیمت لحظه ای فروش دلار", "قیمت لحظه ای خرید یورو", "قیمت لحظه ای فروش یورو", "قیمت لحظه ای خرید درهم", "قیمت لحظه ای فروش درهم", "پشتیبانی")
@bot.message_handler(commands=['start'])

def welcome_message(message):
    bot.send_message(message.chat.id, welcome, reply_markup=keyboard_buttons_start)

@bot.message_handler()

def tarefe(message):
    if message.text == "قیمت لحظه ای خرید دلار":
        bot.reply_to(message, usdtbuy, reply_markup=amoozesh_service)
    elif message.text == "قیمت لحظه ای فروش دلار":
        bot.reply_to(message, usdtsell, reply_markup=amoozesh_service)
    elif message.text == "قیمت لحظه ای خرید یورو":
        bot.reply_to(message, eurbuy, reply_markup=amoozesh_service)
    elif message.text == "قیمت لحظه ای فروش یورو":
        bot.reply_to(message, eursell, reply_markup=amoozesh_service)
    elif message.text == "قیمت لحظه ای خرید درهم":
        bot.reply_to(message, aedbuy, reply_markup=amoozesh_service)
    elif message.text == "قیمت لحظه ای فروش درهم":
        bot.reply_to(message, aedsell, reply_markup=amoozesh_service)
    elif message.text == "پشتیبانی":
        bot.reply_to(message, support, reply_markup=amoozesh_service)


bot.infinity_polling()
