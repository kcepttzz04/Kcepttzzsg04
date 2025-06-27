import telebot
import os

# Lấy token từ biến môi trường (Environment Variable)
# Đây là cách an toàn để quản lý token, không nên hardcode trực tiếp vào code
BOT_TOKEN = os.environ.get('8099339703:AAHINPHp70N9r0VOXCIa1fQshcYWRZONWf8')

if not BOT_TOKEN:
    print("Error: BOT_TOKEN environment variable not set.")
    exit()

bot = telebot.TeleBot(BOT_TOKEN)

@bot.message_handler(commands=['start', 'hello'])
def send_welcome(message):
    bot.reply_to(message, "Chào mừng bạn! Tôi là bot của bạn.")

@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.reply_to(message, message.text)

print("Bot đang chạy...")
bot.polling()