# -*- coding: utf-8 -*-
import scrapy
from oddsScraper.items import GameItem

class FootballSpider(scrapy.Spider):
    name = "football"
    allowed_domains = ["oddschecker.com"]
    start_urls = (
        'http://www.oddschecker.com/football/football-coupons/major-leagues-cups',
    )
    root_domain = 'http://oddschecker.com'

    def parse(self, response):

        file=open("filename.txt", "wb")
        file.write(response.body)

        all_links = response.xpath('//td[@class="betting"]/a/@href').extract()
        for link in all_links:
            yield scrapy.Request( self.root_domain + link, callback = self.parse_football_match )

    def parse_football_match(self, response):
        item = GameItem()
        
        match_id = response.xpath('//div[@id="oddsTableContainer"]/table/@data-mid').extract_first()
        name = response.xpath('//div[@id="oddsTableContainer"]/table/@data-sname').extract_first()
        datetime = response.xpath('//div[@id="oddsTableContainer"]/table/@data-time').extract_first()
        tournament = response.xpath('//div[@id="oddsTableContainer"]/table/@data-ename').extract_first()

        bookkeepers = response.xpath('//tr[@class="eventTableHeader"]/td/aside/a/@title').extract()

        teams = response.xpath('//div[@id="oddsTableContainer"]/table/tbody/tr')
        odds = {}

        for team in teams:
            team_name = team.xpath('./@data-bname').extract_first()
            team_odds = team.xpath('.//td/text()').extract()
            team_best = team.xpath('.//td[contains(concat(" ", @class, " "), " b ")]/@data-o').extract_first()
            odds[team_name] = {
                'for': team_name,
                'odds': dict(zip(bookkeepers,team_odds)),
                'best': team_best
            }

        item['match_id'] = match_id
        item['match'] = name
        item['tournament'] = tournament
        item['datetime'] = datetime
        item['odds'] = odds

        yield item

