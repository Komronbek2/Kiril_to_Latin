"""
14/01/2021
Dasturlash asoslari
КИРИЛЛ-LOTIN TELEGRAM BOT
Muallif: Anvar Narzullaev
Web sahifa: https://python.sariq.dev
"""
import telebot
from transliterate import to_cyrillic, to_latin

# <-- Tokeningizni shu yerga yozing
TOKEN = "1514556420:AAH14vOcMZAzyAOcdVDCqEwBkxLpO_UhMVk"
bot = telebot.TeleBot(token=TOKEN)

# \start komandasi uchun mas'ul funksiya


@bot.message_handler(commands=['start'])
def send_welcome(message):
    # Bu usul bilan foydalanuvchi nomini olishimiz mumkin
    username = message.from_user.username
    xabar = f'Assalom alaykum, {username}👋 \nKirill-Lotin-Kirill botiga xush kelibsiz!'
    xabar += '\n\nMatningizni yuboring😊.'
    bot.reply_to(message, xabar)

# #matnlar uchun mas'ul funksiya


@bot.message_handler(func=lambda msg: msg.text is not None)
def translit(message):
    msg = message.text
    def javob(msg): return to_cyrillic(msg) if msg.isascii() else to_latin(msg)
    bot.reply_to(message, javob(msg))


bot.polling()
