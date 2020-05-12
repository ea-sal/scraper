import argparse

from scraper.commands import crawler


def parse():
    """
    parse arguments from command line
    """
    parser = argparse.ArgumentParser(prog='scraper')
    subparsers = parser.add_subparsers()

    parser_crawler = subparsers.add_parser('crawl')
    parser_crawler.set_defaults(func=crawler.execute)

    #args = parser.parse_args()
    crawler.execute()
