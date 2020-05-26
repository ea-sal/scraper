from parsel import Selector


def get_features_from_item(item_url_responce) -> dict:
    """
    takes item link
    and gets item's characteristics from link html

    :item_url_responce item's url response
    :return: item features as a dictionary
    """

    item_response_html = Selector(item_url_responce.text)

    item_features = {
        'URL': item_url_responce.url,
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
