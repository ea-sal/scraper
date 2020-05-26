import argparse

from scraper.commands import crawler
from scraper.engine import SIGN_STDOUT, FORMAT_CSV, FORMAT_JL


def parse():
    """
    parse arguments from command line
    """
    parser = argparse.ArgumentParser(prog='scraper')
    subparsers = parser.add_subparsers()

    parser_crawler = subparsers.add_parser('crawl')
    parser_crawler.add_argument('-o', '--outfile', metavar='FILE', default=SIGN_STDOUT)
    parser_crawler.add_argument('-f', '--format', default=FORMAT_CSV, choices=[FORMAT_CSV, FORMAT_JL])
    parser_crawler.set_defaults(func=crawler.execute)

    args = parser.parse_args()
    args.func(args)
