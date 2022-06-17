import telebot

TOKEN = 'Your token'

bot = telebot.TeleBot(TOKEN)

user_id_to_send: int = 'user id'


def send_message_w_bot(message: str):
    """
    Отправка сообщений специальному пользователю по ID
    :param message: str
    :return: None
    """
    bot.send_message(user_id_to_send, message)
