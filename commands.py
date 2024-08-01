from telebot import TeleBot
from telebot.types import BotCommand
import os
from dotenv import load_dotenv
from telebot import TeleBot
from telebot.types import BotCommand, InlineKeyboardMarkup, InlineKeyboardButton, WebAppInfo

# Функция для регистрации команд бота
def register_commands(bot: TeleBot):
    commands = [
        BotCommand("start", "Запустить бота"),
        BotCommand("hello", "Поздороваться"),
    ]
    
    bot.set_my_commands(commands)

# Обработчик команды /start
def send_welcome(bot: TeleBot, message):
    welcome_text = ("Привет! Добро пожаловать в CATCHING THE CASH 😺\n"
                    "Отныне ты — директор криптобиржи.\n"
                    "Какой? Выбирай сам. Тапай по экрану, собирай монеты, "
                    "качай пассивный доход, разрабатывай собственную стратегию дохода.\n"
                    "Мы в свою очередь оценим это во время листинга токена, даты которого ты узнаешь совсем скоро.\n"
                    "Про друзей не забывай — зови их в игру и получайте вместе ещё больше монет!")

    # Создание кнопки для запуска Mini App
    markup = InlineKeyboardMarkup()
    button = InlineKeyboardButton(text="Играть в 1 клик 😺", web_app=WebAppInfo(url="https://graceful-pika-90363b.netlify.app/"))
    markup.add(button)

    # Отправка сообщения с кнопкой
    bot.send_message(message.chat.id, welcome_text, reply_markup=markup)

# Функция для регистрации обработчиков команд
def register_handlers(bot: TeleBot):
    bot.register_message_handler(lambda message: send_welcome(bot, message), commands=['start'])
