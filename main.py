import os
import requests
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv('API_KEY')

if not API_KEY:
    print('Ключ не найден!!!')
else:
    print('Ключ загружен...')

url = f'https://v6.exchangerate-api.com/v6/{API_KEY}/latest/USD'
response = requests.get(url)

if response.status_code == 200:
    print('Все работает!')
    date = response.json()
    print(f'Курс: 1 USD = {date['conversion_rates'] ['RUB']} RUB')
else:
    print(f'API НЕ ОТВЕЧАЕТ: КОД ОШИБКИ {response.status_code}')
    print(f'Сообщение от сервера: {response.text}')