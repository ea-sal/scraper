from scraper import engine


def execute(args):
    engine.parse(engine.start_url, args.outfile, args.format)
