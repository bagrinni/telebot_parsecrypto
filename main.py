import time
import telebot
from bs4 import BeautifulSoup
import requests
from telebot import types

TOKEN = '6326153479:AAHn6xDqblMhUY8CihcpxvapD9Ohm6t6dGo'

bot = telebot.TeleBot(TOKEN)

url = 'https://www.coingecko.com/ru'

is_running = False

keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
button_one = types.KeyboardButton('Bitcoin')
button_two = types.KeyboardButton('Ethereum')
button_three = types.KeyboardButton('Techer')
button_stop = types.KeyboardButton('Stop')
keyboard.add(button_one, button_two, button_three,button_stop)


@bot.message_handler(commands=['start'])
def handle_start(message):
    global is_running
    is_running = False
    bot.send_message(message.chat.id, "Бот запущен.", reply_markup=keyboard)


@bot.message_handler(func=lambda message: message.text == 'Bitcoin')
def handle_bitcoin(message):
    global is_running
    is_running = True
    while is_running:
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')
        crypto_symbol = soup.find('div', class_='tw-text-xs tw-leading-4 tw-text-gray-500 dark:tw-text-moon-200 tw-font-medium tw-block 2lg:tw-inline').get_text(strip=True)
        current_price = soup.find('span', {'data-coin-id': '1', 'data-price-target': 'price'}).get_text(strip=True)
        hourly_change = soup.find('span', class_='gecko-up').get_text(strip=True)
        weekly_change = soup.find('span', class_='gecko-down').get_text(strip=True)

        msg = f'Криптовалюта: {crypto_symbol}\nТекущая цена: {current_price}\nИзменение за час: {hourly_change}\nИзменение за неделю: {weekly_change}'
        bot.send_message(message.chat.id, msg)
        time.sleep(30)


@bot.message_handler(func=lambda message: message.text == 'Ethereum')
def handle_ethereum(message):
    global is_running
    is_running = True
    while is_running:
        response = requests.get('https://www.coingecko.com/ru/%D0%9A%D1%80%D0%B8%D0%BF%D1%82%D0%BE%D0%B2%D0%B0%D0%BB%D1%8E%D1%82%D1%8B/%D1%8D%D1%84%D0%B8%D1%80%D0%B8%D1%83%D0%BC')
        soup = BeautifulSoup(response.text, 'html.parser')
        crypto_symbol = soup.find('div', class_='tw-font-bold tw-text-gray-900 dark:tw-text-moon-50 tw-text-lg tw-leading-7 !tw-text-base 2lg:!tw-text-lg').get_text(strip=True)
        current_price = soup.find('span', {'data-coin-id': '279', 'data-price-target': 'price'}).get_text(strip=True)
        hourly_change = soup.find('span', class_='gecko-up').get_text(strip=True)
        weekly_change = soup.find('span', class_='gecko-down').get_text(strip=True)

        msg = f'Криптовалюта: {crypto_symbol}\nТекущая цена: {current_price}\nИзменение за час: {hourly_change}\nИзменение за неделю: {weekly_change}'
        bot.send_message(message.chat.id, msg)
        time.sleep(30)


@bot.message_handler(func=lambda message: message.text == 'Techer')
def handle_techer(message):
    global is_running
    is_running = True
    while is_running:
        response = requests.get('https://www.coingecko.com/ru/%D0%9A%D1%80%D0%B8%D0%BF%D1%82%D0%BE%D0%B2%D0%B0%D0%BB%D1%8E%D1%82%D1%8B/tether')
        soup = BeautifulSoup(response.text, 'html.parser')
        crypto_symbol = soup.find('div', class_='tw-font-bold tw-text-gray-900 dark:tw-text-moon-50 tw-text-lg tw-leading-7 !tw-text-base 2lg:!tw-text-lg').get_text(strip=True)
        current_price = soup.find('span', {'data-coin-id': '325', 'data-price-target': 'price'}).get_text(strip=True)
        hourly_change = soup.find('span', class_='gecko-up').get_text(strip=True)
        weekly_change = soup.find('span', class_='gecko-down').get_text(strip=True)

        msg = f'Криптовалюта: {crypto_symbol}\nТекущая цена: {current_price}\nИзменение за час: {hourly_change}\nИзменение за неделю: {weekly_change}'
        bot.send_message(message.chat.id, msg)
        time.sleep(30)

@bot.message_handler(func=lambda message: message.text == 'Stop')
def handle_stop(message):
    global is_running
    is_running = False
    bot.send_message(message.chat.id, "Остановлено.", reply_markup=keyboard)



bot.polling()