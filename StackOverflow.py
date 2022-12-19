import requests
from pprint import pprint
import datetime

current_date = datetime.datetime.today()
from_date = int((datetime.datetime.today() - datetime.timedelta(days=2)).timestamp())
params = {
    'fromdate': from_date,
    'order': 'desc',
    'tagged': 'Python',
    'site': 'stackoverflow'
}
url = 'https://api.stackexchange.com/2.3/questions?'
res = requests.get(url, params=params).json()
pprint(res)
