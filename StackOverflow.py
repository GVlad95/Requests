import requests
from pprint import pprint
import datetime

n = int(input('Введите количество дней, за которые необходимо собрать данные: '))
tags = input('Введите ключевое слово для поиска: ')
current_date = datetime.datetime.today()
from_date = int((datetime.datetime.today() - datetime.timedelta(days=n)).timestamp())
params = {
    'fromdate': from_date,
    'order': 'desc',
    'tagged': tags,
    'site': 'stackoverflow'
}
url = 'https://api.stackexchange.com/2.3/questions?'
res = requests.get(url, params=params).json()
pprint(res)
print(len(res['items']))
