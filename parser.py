import requests
from bs4 import BeautifulSoup

def parse_wildberries(query):
    url = f"https://www.wildberries.ru/catalog/0/search.aspx?search={query}"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    items = soup.find_all('div', class_='product-card__wrapper', limit=10)
    result = []
    for item in items:
        name = item.find('span', class_='goods-name').text
        link = item.find('a', class_='product-card__main j-card-link').get('href')
        result.append({"name": name, "link": link})
    return result
