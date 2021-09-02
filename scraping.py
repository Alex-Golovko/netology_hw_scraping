import requests
from bs4 import BeautifulSoup

URL = 'https://habr.com'
# DESIRED_HUBS = {'Python', 'Java*', 'Python*'}
KEYWORDS = {'дизайн', 'фото', 'web', 'python'}

response = requests.get('https://habr.com/ru/all/')

response.raise_for_status()

soup = BeautifulSoup(response.text, features='html.parser')
article = soup.find('article')
articles = soup.find_all('article')

for article in articles:
    hubs = article.find_all('a', class_='tm-article-snippet__hubs-item-link')
    hubs = {hub.text.strip() for hub in hubs}
    spans = article.find('a', class_ = 'tm-article-snippet__readmore')
    spans = {span.text.strip() for span in spans}

    if KEYWORDS & spans:
        time_pub = article.find('span', class_ = 'tm-article-snippet__datetime-published')
        title = article.find('h2')
        href = title.find('a').attrs.get('href')
        print(title.text, URL + href, time_pub.text)