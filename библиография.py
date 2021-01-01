import requests
from bs4 import BeautifulSoup
import datetime

url = input('Введите ссылку на сайт:')

response = requests.get(url)
soup = BeautifulSoup(response.text, 'lxml' )
quotes = soup.find_all('title')
data = datetime.datetime.now().strftime("%d.%m.%Y")
articles = url.split('/')

for quot in quotes:
    print(f'{quot.text} [Электронный ресурс], Статьи на {articles[2]} URL: {url} (Дата обращения: {data})')


    
    

