import requests
from parsel import Selector
from typing import List


def execute() -> List[str]:
    """
    goes to URL, parses URL's html, returns list of item limks
    """
    url = 'http://www.world-art.ru/animation/rating_top.php'
    response = requests.get(url)
    assert response.status_code == 200, f'bad status code: {response.status_code}'

    response_html = Selector(response.text)
    links_to_films = response_html.xpath('//td[@class="review"]/a[@class="review"]/@href').getall()

    return links_to_films
