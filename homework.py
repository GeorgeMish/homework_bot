import logging
import requests
from telegram import Bot
from telegram.ext import CommandHandler, Updater
import os
from dotenv import load_dotenv
from time import time



load_dotenv()
PRACTICUM_TOKEN = os.getenv('PRACTICUM_TOKEN')
TELEGRAM_TOKEN = os.getenv('TELEGRAM_TOKEN')
TELEGRAM_CHAT_ID = os.getenv('TELEGRAM_CHAT_ID')

DAY_IN_SEC = 30 * 24 * 60 * 60
RETRY_PERIOD = 600
ENDPOINT = 'https://practicum.yandex.ru/api/user_api/homework_statuses/'
HEADERS = {'Authorization': f'OAuth {PRACTICUM_TOKEN}'}


HOMEWORK_VERDICTS = {
    'approved': 'Работа проверена: ревьюеру всё понравилось. Ура!',
    'reviewing': 'Работа взята на проверку ревьюером.',
    'rejected': 'Работа проверена: у ревьюера есть замечания.'
}


class NegativeValueException(Exception):
    """Класс исключений для проверки доступности переменных окружения."""

    pass


def check_tokens():
    """Функция проверяет доступность переменных окружения."""
    for token in os.getenv():
        if token is None:
            raise NegativeValueException('Отсутствуют обязательные'
                                         'переменные окружения')


def send_message(bot, message):
    """Функция отправляет сообщение в Telegram чат."""
    bot = Bot(token=TELEGRAM_TOKEN)
    chat_id = TELEGRAM_CHAT_ID
    message = 'Ваша работа проверена!'
    bot.send_message(chat_id, message)


def get_api_answer(timestamp):
    """Функция получает ответ от API Яндекс.Домашки."""
    payload = {'from_date': timestamp - DAY_IN_SEC}
    if response.status_code != 200:
        try:
            response = requests.get(
                url=ENDPOINT,
                headers=HEADERS,
                params=payload
            )
            return response.json()
        except Exception:
            logging.error(Exception, exc_info=True)


def check_response(response):
    """Проверяет ответ API на соответствие документации."""
    response = response.json()


def parse_status(homework):
    """Извлекает из информации о конкретной домашней работе статус работы."""
    return f'Изменился статус проверки работы "{homework_name}". {verdict}'


def main():
    """Основная логика работы бота."""
    ...

    bot = telegram.Bot(token=TELEGRAM_TOKEN)
    timestamp = int(time.time())

    ...

    while True:
        try:

            ...

        except Exception as error:
            message = f'Сбой в работе программы: {error}'
            ...
        ...


if __name__ == '__main__':
    main()
