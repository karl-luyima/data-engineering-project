import scrapy


class CveSpider(scrapy.Spider):  #creates a clas called CveSpider. it inherits from Scrapy's spider class
    name = "cve"
    allowed_domains = ["cve.mitre.org"] #restricts the spider to this domain
    start_urls = ["https://www.cve.org/Resources/Media/Archives/OldWebsite/index.html"] #specifies the webpage spider should visit

    def parse(self, response):
        table =response.xpath('//table')[3]

        for row in table.xpath('.//tr') :
            try:
                print(row.xpath('.//td/text()')[0].extract())
            except IndexError:
                pass    
