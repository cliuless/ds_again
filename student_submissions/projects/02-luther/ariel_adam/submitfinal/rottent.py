import scrapy


class ImdbSpider(scrapy.Spider):

    name = 'rottent_data'

    custom_settings = {
        "DOWNLOAD_DELAY": 1,
        "CONCURRENT_REQUESTS_PER_DOMAIN": 3,
        "HTTPCACHE_ENABLED": True
    }
    #title_names = ['the_lord_of_the_rings_the_fellowship_of_the_ring','kate_and_leopold','glitter']

    title_names = open('/Users/Adam/Metis/notebooks/data/rottentitles.ls','r').read().strip().split(',')
    start_urls = ['https://www.rottentomatoes.com/m/'+i+'/' for i in title_names]

    def parse(self, response):

        tmall = response.xpath('//*[@id="tomato_meter_link"]/span[2]/span/text()').extract()[0]
        tmallave = response.xpath('//*[@id="scoreStats"]/div[1]/text()[2]').extract()[0]

        tmtop = response.xpath('//*[@id="tomato_meter_link"]/span[2]/span/text()').extract()[1]
        tmtopave = response.xpath('//*[@id="scoreStats"]/div[1]/text()[2]').extract()[1]

        audiencescore = response.xpath('//*[@id="scorePanel"]/div[2]/div[1]/a/div/div[2]/div[1]/span/text()').extract()

        ratingRT = response.xpath('//*[@id="mainColumn"]/section[2]/div/div/ul/li[1]/div[2]/text()').extract()

        boxofficeRT = response.xpath('//*[@id="mainColumn"]/section[2]/div/div/ul/li[7]/div[2]/text()').extract()

        runtimeRT = response.xpath('//*[@id="mainColumn"]/section[2]/div/div/ul/li[8]/div[2]/time/text()').extract()


        url = response.url

        yield {
            'url': url,
            'tmall': tmall,
            'tmallave': tmallave,
            'tmtop': tmtop,
            'tmtopave': tmtopave,
            'audiencescore': audiencescore,
            'ratingRT': ratingRT,
            'boxofficeRT': boxofficeRT,
            'runtimeRT': runtimeRT,
        }
