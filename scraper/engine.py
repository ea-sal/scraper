import sys
import csv
import requests
from parsel import Selector
from scraper.parser import get_features_from_item


start_url = 'http://www.world-art.ru/animation/rating_top.php'

SIGN_STDOUT = '-'
FORMAT_CSV = 'csv'
FORMAT_JL = 'jl'


def parse(url: str, out_path: str, out_format: str):
    """
    gets link and returns the response
    """

    response = requests.get(url)
    assert response.status_code == 200, f'bad status code: {response.status_code}'

    response_html = Selector(response.text)
    links_to_films = response_html.xpath('//td[@class="review"]/a[@class="review"]/@href').getall()

    out_file = sys.stdout if out_path == SIGN_STDOUT else open(out_path, 'w', buffering=1, newline='')

    for link in links_to_films:
        item_response = requests.get(link)
        assert response.status_code == 200, f'bad status code: {item_response.status_code}'

        item = get_features_from_item(item_response)

        if out_format == FORMAT_CSV:
            item_writer = csv.writer(out_file, delimiter=' ', quotechar=',', quoting=csv.QUOTE_MINIMAL)
            item_writer.writerow(item.values())

    out_file.close()

    return
