from langdetect import detect
import scrapy


class QuotesSpider(scrapy.Spider):
    name = "quotes"

    def __init__(self, slug=None, lang=None, *args, **kwargs):
        super(QuotesSpider, self).__init__(*args, **kwargs)
        self.start_urls = ["https://www.goodreads.com/work/quotes/" + slug]
        self.slug = slug
        self.lang = lang
        self.quotes_seen = set()

    def parse(self, response):
        quote_divs = response.xpath('//div[@class="quote"]')

        for quote in quote_divs:
            quote_text = quote.xpath('.//div[@class="quoteText"]/text()').get().strip()

            author = (
                quote.xpath('.//span[@class="authorOrTitle"]/text()')
                .get()
                .replace(",", "")
                .strip()
            )

            if detect(quote_text) == self.lang:
                if quote_text not in self.quotes_seen:
                    self.quotes_seen.add(quote_text)
                    yield {"quote": quote_text, "author": author}

        next_page = response.xpath('//a[@class="next_page"]/@href').get()

        if next_page:
            next_page_url = response.urljoin(next_page)

            page_number = int(next_page.split("=")[-1])

            self.logger.info(f"Scraping page {page_number}!")

            yield scrapy.Request(next_page_url, callback=self.parse)
