import requests
from bs4 import BeautifulSoup

URL = 'https://habr.com'

KEYWORDS = {'дизайн', 'фото', 'web', 'python'}

response = requests.get('https://habr.com/ru/all/')

response.raise_for_status()

soup = BeautifulSoup(response.text, features='html.parser')

articles = soup.find_all('article', class_='tm-articles-list__item')

for article in articles:
    article_time = article.find('span', class_='tm-article-snippet__datetime-published').text
    article_title = article.find('h2', class_ = 'tm-article-snippet__title tm-article-snippet__title_h2').text
    article_title_links = article.find('a', class_='tm-article-snippet__title-link').attrs.get('href')
    article_title_link = URL + article_title_links

    article_text = article.find('div', class_='tm-article-body tm-article-snippet__lead').text

    article_word = {word for word in article_text.split(' ')}

    if KEYWORDS & article_word:
        print(f'{article_time} - {article_title} - {article_title_link}')







