import scrapy


class ImdbSpider(scrapy.Spider):

    name = 'imdb_data'

    custom_settings = {
        "DOWNLOAD_DELAY": 2,
        "CONCURRENT_REQUESTS_PER_DOMAIN": 3,
        "HTTPCACHE_ENABLED": True
    }
    #title_codes = ['tt0468569','tt0120737']

    title_codes = open('/Users/Adam/Metis/notebooks/data/tconst.ls','r').read().strip().split(',')
    start_urls = ['http://www.imdb.com/title/'+i+'/' for i in title_codes]

    def parse(self, response):

        name = response.xpath('//*[@id="title-overview-widget"]/div[2]/div[2]/div/div[2]/div[2]/h1/text()').extract()

        budget = response.xpath('//*[@id="titleDetails"]/div[7]/text()').extract()

        openingWeekend = response.xpath('//*[@id="titleDetails"]/div[8]/text()[2]').extract()

        usaGross = response.xpath('//*[@id="titleDetails"]/div[9]/text()[2]').extract()

        MPAArating = response.xpath('//*[@id="title-overview-widget"]/div[2]/div[2]/div/div[2]/div[2]/div/text()[2]').extract()

        runtime = response.xpath('//*[@id="titleDetails"]/div[13]/time/text()').extract_first()

        ratingIMDB = response.xpath('//*[@id="title-overview-widget"]/div[2]/div[2]/div/div[1]/div[1]/div[1]/strong/span/text()').extract()

        tconst = response.url
        yield {
            'tconst': tconst,
            'name': name,
            'budget': budget,
            'openingWeekend': openingWeekend,
            'usaGross': usaGross,
            'MPAArating': MPAArating,
            'runtime': runtime,
            'ratingIMDB': ratingIMDB
        }
