from scraper.commands import crawler
import requests
from parsel import Selector
from pymongo import MongoClient, errors


def parser():
    """
    gets links an
    """

    list_link = crawler.execute()
    mongo_client = MongoClient('mongodb://127.0.0.1:27017/')
    db = mongo_client.worldart


    for link in list_link:
        item_features_dict = get_features_from_item(link)


def get_features_from_item(item_url: str):
    """
    takes item link
    and gets item's characteristics from its html

    :param item_url: item link
    :return:
    """

    item_response = requests.get(item_url)
    assert item_response.status_code == 200, f'bad status code: {response.status_code}'

    item_response_html = Selector(item_response.text)

    item_features = {
        'URL': item_url,
        'title': item_response_html.xpath(
        '//td[@class="review"]/b[text()="Название (англ.)"]/../following-sibling::*[2]/text()').get(),
        'country': item_response_html.xpath(
        '//td[@class="review"]/b[text()="Производство"]/../following-sibling::*[2]/text()').get(),
        'genres': item_response_html.xpath(
        '//td[@class="review"]/b[text()="Жанр"]/../following-sibling::*[2]/a/text()').getall(),
        'audience': item_response_html.xpath(
        '//td[@class="review"]/b[text()="Целевая аудитория"]/../following-sibling::*[2]/a/text()').get(),
        'season': item_response_html.xpath(
        '//td[@class="review"]/b[text()="Сезон"]/../following-sibling::*[2]/a/text()').get(),
        'based_on': item_response_html.xpath(
        '//td[@class="review"]/b[text()="Основа"]/../following-sibling::*[2]/a/text()').get(),
        'based_on_title': item_response_html.xpath(
        '//td[@class="review"]/b[text()="Снято по манге"]/../following-sibling::*[2]/a/text()').get(),
        'producer': item_response_html.xpath(
        '//td[@class="review"]/b[text()="Режиссёр"]/../following-sibling::*[2]/a/text()').get(),
        'original_author': item_response_html.xpath(
        '//td[@class="review"]/b[text()="Автор оригинала"]/../following-sibling::*[2]/a/text()').get(),
        'avg_point': item_response_html.xpath(
        '//td[@class="review"]/b[text()="Средний балл"]/../following-sibling::*[2]/text()').get().split(' ')[0][:3],
        'voters_num': item_response_html.xpath(
        '//td[@class="review"]/b[text()="Проголосовало"]/../following-sibling::*[2]/text()').get().split(' ')[0],
        'place': item_response_html.xpath(
        '//td[@class="review"]/b[text()="Место в "]/../following-sibling::*[2]/text()').get().split(' ')[0]
    }

    return item_features


parser()
