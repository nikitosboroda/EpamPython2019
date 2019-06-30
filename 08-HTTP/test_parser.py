import bs4
from bs4 import BeautifulSoup


def main():
    html = open('Hot.html').read()
    soup = BeautifulSoup(html, 'html.parser')
    div = soup.find_all('div', class_='story__tags tags')
    # links = div.find_all('a')
    # for i in links:
    #     lnk = i.get('data-tag')
    #     print(lnk)
    count = 1
    for j in div:
        print(f'post ------> {count}')
        links = j.find_all('a')
        for k in links:
            lnk = k.get('data-tag')
            print(lnk)
        count += 1


def get_links() -> list:
    html = open('Hot.html').read()
    soup = BeautifulSoup(html, "html.parser")
    titles = soup.find_all("h2", class_="story__title")
    print(len(titles))
    links = []
    for title in titles:
        info = title.find("a")
        links.append((info.get("href"), info.text.strip()))

    return links


if __name__ == '__main__':
    main()
    for i in get_links():
        print(i)
