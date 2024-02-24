from scrapy.crawler import CrawlerProcess

from sage.spiders import QuotesSpider


def start_crawler(slug: str, languageCode: str):
    process = CrawlerProcess(
        settings={
            "FEED_FORMAT": "json",
            "FEED_URI": "quotes.json",
        }
    )

    process.crawl(QuotesSpider, slug=slug, lang=languageCode)

    process.start()


def main():
    print("Welcome to Sage - Get all popular quotes from a book!")
    print(
        '\nSearch "<your book> quotes" on your search engine, and check for the slug on it\'s Goodreads quotes page URL.'
    )
    print('The URL must look like "goodreads.com/work/quotes/<slug>".')
    print("\n\nQuotes will be exported to ./quotes.json")

    slug = input("\nPlease enter the slug of the book: ")

    while not slug:
        slug = input("Please enter the slug of the book: ")

    languageCode = input(
        '\nPlease enter the desired language code (ex: "en" for english): '
    )

    while not languageCode:
        languageCode = input(
            'Please enter the desired language code (ex: "en" for english): '
        )

    start_crawler(slug, languageCode)


if __name__ == "__main__":
    main()
