import requests


def get_wildberries_items(query):
    url = f'https://search.wb.ru/exactmatch/ru/common/v4/search?query={query}&regions=64,83,4,38,30,33,70,69,22,31,66,68,40,48,1,80,71&resultset=catalog&sort=popular'
    response = requests.get(url)
    data = response.json()

    items = []
    for item in data['data']['products'][:10]:
        items.append({
            'name': item['name'],
            'link': f'https://www.wildberries.ru/catalog/{item["id"]}/detail.aspx'
        })

    return items
