import scrapy
import csv

def write_on_file(filename,movie, message):
    with open(filename,'a') as file:
        file.write(message)
        file.write(",")
        file.write(movie)
        file.write('\n')


def assign_value(expression, filename,movie,message):
    try:
        exp=expression
        return(exp)
    except:
        write_on_file(filename,movie,message)
        return("")

class FestivalSpider(scrapy.Spider):
    name = 'mojo'

    custom_settings = {
        "DOWNLOAD_DELAY": 3,
        "CONCURRENT_REQUESTS_PER_DOMAIN": 3,
        "HTTPCACHE_ENABLED": True
    }


    start_urls = [
        'http://www.boxofficemojo.com/genres/'
    ]
 

    def parse(self, response):
        # Extract the links to the individual festival pages
       
        geners_links=response.xpath('//*[@id="body"]/table[2]/tr/td[1]/table/tr/td[1]/font/b/a/@href').extract()
        geners_links=list(map(lambda x: self.start_urls[0]+x, geners_links))
        

        


        #for i in range(1):
        for i in range(len(geners_links)):
            
            yield scrapy.Request(
                url=geners_links[i],
                callback=self.parse_gener,
                meta={'list_of_genres:': geners_links[i]}
            )            
        



    def parse_gener(self, response):
        
        #url = response.request.meta['url']
        movie_path="http://www.boxofficemojo.com/"

        next_hundreds=response.xpath('//*[@id="body"]/table[2]/tr/td[1]/font[1]/b/a/@href').extract()
        next_hundreds=list(map(lambda x: movie_path+x, next_hundreds))
        
        list_of_movies_urls=response.xpath('//*[@id="body"]/table[2]/tr/td[1]/table/tr/td[2]/font/a/@href').extract()
        list_of_movies_urls=list(map(lambda x: movie_path+x, list_of_movies_urls[1:]))
         
        list_of_movies_names=response.xpath('//*[@id="body"]/table[2]/tr/td[1]/table/tr/td[2]/font/a/b/text()').extract() 
        list_of_movies_names=list_of_movies_names
         


        for i in range(len(list_of_movies_urls)):
            yield scrapy.Request(
                url=list_of_movies_urls[i],
                callback=self.parse_movie,
                meta={'url': list_of_movies_urls[i], "name": list_of_movies_names[i]}
            )

        
        
        for i in range(len(next_hundreds)):
            yield scrapy.Request(
                url=next_hundreds[i],
                callback=self.parse_gener
            )    

    def parse_movie(self, response):
        movie=response.request.meta["name"]
        write_on_file("movies_analysed.txt",movie, movie)
        try:
            oscar_nominations=response.xpath('//a/b[contains(text(),"Nominated for")]/text()').extract()[0]
        except: 
            oscar_nominations="zero"

        try:
            oscar_wins=response.xpath('//a/b[contains(text(),", Including")]/text()').extract()[0]
        except: 
            oscar_wins="zero"

        try:
            Gross=response.xpath('//td[@align="right"]/b/text()').extract()
            if len(Gross)==1:
                domestic_gross=Gross[0]
                international_movie=0
                international_gross=0
                worldwide_gross=0
            else:
                domestic_gross=Gross[0]
                international_movie=1
                international_gross=Gross[1]
                worldwide_gross=Gross[2]
        except:
            line=[response.request.meta["name"],response.request.meta["url"]]
            with open('no_gross_info.txt','a') as file:
                for l in line:
                    file.write(l)
                    if l != line[-1]:
                        file.write(",")
                file.write('\n')
                return()

        try:
            resu={
                "url": response.request.meta["url"],
                "name": response.request.meta["name"],
                "oscar_nominations":oscar_nominations,
                "main_genre" : response.xpath('//td[@valign= "top"]/b/text()').extract()[0],
                "run_time" : response.xpath('//td[@valign= "top"]/b/text()').extract()[1],            
                "mpaa" : response.xpath('//td[@valign= "top"]/b/text()').extract()[2],
                "budget" : response.xpath('//td[@valign= "top"]/b/text()').extract()[3],
                #"distributor":response.xpath('//td[contains(text(),"Distributor:")]/b/a/text()').extract()[0],
                
                "distributor":response.xpath('//td[contains(text(),"Distributor:")]/b//text()').extract()[0],
                "release_date":response.xpath('//td[contains(text(),"Release Date:")]/b/nobr//text()').extract()[0],
                "genres":response.xpath('//div[contains(text(),"Genres")]/parent::div[1]/div[2]/table/tr/td[1]/font/a//text()').extract(),
                "oscar_wins":oscar_wins,
                "domestic_gross":domestic_gross,
                "international_movie":international_movie,
                "international_gross":international_gross,
                "worldwide_gross":worldwide_gross

               }
            #To take all:
            #players=response.xpath('//div[contains(text(),"The Players")]/parent::div/div[2]/table/tr/td[1]/font//text()').extract()

                
            players=response.xpath('//div[contains(text(),"The Players")]/parent::div/div[2]/table/tr/td[1]/font/a/text()').extract()
            
            for i in range(len(players)):
                if players[i]!=":":
                    if players[i][-1]==":":
                        players[i]=players[i][:-1]
                    if players[i][-1]=="s":
                        players[i]=players[i][:-1]

                    resu[players[i]]=response.xpath('//div[contains(text(),"The Players")]/parent::div/div[2]/table/tr['+str(i+1)+']/td/font/a//text()').extract()[1:]
                    #resu[players[i]].extend(response.xpath('//div[contains(text(),"The Players")]/parent::div/div[2]/table/tr['+str(i+1)+']/td/font/text()').extract()[1:])
                    
            yield (resu)        


        except:
            line=[response.request.meta["name"],response.request.meta["url"]]
            with open('log.txt','a') as file:
                for l in line:
                    file.write(l)
                    if l != line[-1]:
                        file.write(",")
                file.write('\n')
        