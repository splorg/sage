import argparse
from scrapy.crawler import CrawlerProcess

from sage.spiders import QuotesSpider

def start_crawler(slug: str):
  process = CrawlerProcess(settings={
    'FEED_FORMAT': 'json',
    'FEED_URI': 'quotes.json',
  })

  process.crawl(QuotesSpider, slug=slug)
  
  process.start()

def main():
  print('Welcome to Sage - Get all popular quotes from a book.')
  print('\nFirst, search "your book" + quotes on Google, and check for the slug on it\'s Goodreads quotes page.')
  print('The URL must look like "goodreads.com/work/quotes/<slug>".')
  print('\n\nQuotes will be exported in ./quotes.json')

  slug = input("\nPlease enter the slug of the book: ")

  while not slug:
    slug = input("Please enter the slug of the book: ")
  
  start_crawler(slug)

if __name__ == '__main__':
  main()