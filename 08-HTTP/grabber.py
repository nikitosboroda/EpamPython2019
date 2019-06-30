import requests
import config
from bs4 import BeautifulSoup
import time
from collections import Counter


class PikGrabber():
    # HOME = "https://pikabu.ru/subs/"
    HEADERS = {
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
        "Accept-Encoding": "gzip, deflate, br",
        "Accept-Language": "ru-RU,ru;q=0.8,en-US;q=0.5,en;q=0.3",
        "Cache-Control": "max-age=0",
        "Connection": "keep-alive",
        "Cookie": config.cookie,
        "DNT": "1",
        "Host": "pikabu.ru",
        "Referer": "https://www.google.com/",
        "TE": "Trailers",
        "Upgrade-Insecure-Requests": "1",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:67.0) Gecko/20100101 Firefox/67.0",
    }

    def __init__(self):
        self.session = requests.Session()  # переменная для храннения Сессии
        self.session.headers = self.HEADERS
        self.number = 1
        self.query = "https://pikabu.ru/subs/"

    def getPage(self):
        return self.session.get(self.query)

    def open_new_page(self):
        self.number += 1
        self.query = f'https://pikabu.ru/subs?page={self.number}'


if __name__ == '__main__':
    grabber = PikGrabber()
    html_page = grabber.getPage()
    print(html_page)
    soup = BeautifulSoup(html_page.text, 'html.parser')
    div = soup.find_all('div', class_='story__tags tags')
    # print(div)
    tags = []
    for s in div:
        tags += [tag.get('data-tag') for tag in s.find_all('a') if tag.get('data-tag')]
    # print(tags)
    count_tags = Counter(tags)
    # print(count_tags)
    for i in range(4):
        grabber.open_new_page()
        time.sleep(10)
        page = grabber.getPage()
        if page.status_code != 200:
            print('ERROR', page.status_code)
            break
        soup = BeautifulSoup(page.text, 'html.parser')
        div = soup.find_all('div', class_='story__tags tags')
        tags = []
        for s in div:
            tags += [tag.get('data-tag') for tag in s.find_all('a') if tag.get('data-tag')]
        # print(tags)
        count_tags.update(tags)
    with open('counted_tags.txt', 'w') as result:
        if len(count_tags) > 10:
            most_common_tags = count_tags.most_common(10)
        else:
            most_common_tags = count_tags.most_common()
        for tag in most_common_tags:
            result.write(f'tag {tag[0]} occurs {tag[1]} times;\n')
    print(count_tags)
