from django.shortcuts import render , redirect
from .scrapper import *
from django.contrib import messages
# Create your views here.


def headline(request):
    try:
        news = list(HeadlineScrapper('https://news.google.com/topics/CAAqKggKIiRDQkFTRlFvSUwyMHZNRFZxYUdjU0JXVnVMVWRDR2dKSlRpZ0FQAQ?hl=en-IN&gl=IN&ceid=IN%3Aen'))
        news = news[0:11]
        catenews = list(CategoryScrapper('https://news.google.com/topics/CAAqJQgKIh9DQkFTRVFvSUwyMHZNRE55YXpBU0JXVnVMVWRDS0FBUAE?hl=en-IN&gl=IN&ceid=IN%3Aen'))
        catenews = catenews[0:5]
        localNews = list(LocalNewsScrapper(['https://news.google.com/topics/CAAqHAgKIhZDQklTQ2pvSWJHOWpZV3hmZGpJb0FBUAE/sections/CAQiWENCSVNQRG9JYkc5allXeGZkakpDRUd4dlkyRnNYM1l5WDNObFkzUnBiMjV5RGhJTUwyY3ZNVEZuZWpZMVp6aGplZzRLREM5bkx6RXhaM28yTldjNFl5Z0EqNQgAKjEICiIrQ0JJU0dqb0liRzlqWVd4ZmRqSjZEZ29NTDJjdk1URm5lalkxWnpoaktBQVABUAE?hl=en-IN&gl=IN&ceid=IN%3Aen']))
        localNews = localNews[0:10]
        BuisnessNews = list(BuisnessScrapper('https://news.google.com/topics/CAAqKggKIiRDQkFTRlFvSUwyMHZNRGx6TVdZU0JXVnVMVWRDR2dKSlRpZ0FQAQ?hl=en-IN&gl=IN&ceid=IN%3Aen'))
        BuisnessNews = BuisnessNews[0:10]
        
        worldNews = list(WorldNewsScrapper('https://news.google.com/topics/CAAqKggKIiRDQkFTRlFvSUwyMHZNRGx1YlY4U0JXVnVMVWRDR2dKSlRpZ0FQAQ?hl=en-IN&gl=IN&ceid=IN%3Aen'))
        worldNews = worldNews[0:45]
        
        EntertainmentNews = list(EntertainmentScrapper(['https://news.google.com/topics/CAAqKggKIiRDQkFTRlFvSUwyMHZNREpxYW5RU0JXVnVMVWRDR2dKSlRpZ0FQAQ?hl=en-IN&gl=IN&ceid=IN%3Aen']))
        EntertainmentNews = EntertainmentNews[0:20]
        
        TechnologyNews = TechnologyScrapper('https://news.google.com/topics/CAAqKggKIiRDQkFTRlFvSUwyMHZNRGRqTVhZU0JXVnVMVWRDR2dKSlRpZ0FQAQ?hl=en-IN&gl=IN&ceid=IN%3Aen')
        TechnologyNews = TechnologyNews[0:20]
        
        SportsNews = SportsScrapper('https://news.google.com/topics/CAAqKggKIiRDQkFTRlFvSUwyMHZNRFp1ZEdvU0JXVnVMVWRDR2dKSlRpZ0FQAQ?hl=en-IN&gl=IN&ceid=IN%3Aen')
        SportsNews = SportsNews[0:30]
        Context = {'news':news, 'catenews':catenews ,'localNews':localNews  , 'BuisnessNews':BuisnessNews , 'EntertainmentNews':EntertainmentNews , 'worldNews':worldNews , 'TechnologyNews':TechnologyNews , 'SportsNews':SportsNews }
        return render(request , 'news/headline.html' , Context )
    except Exception as error:
        messages.warning(request , 'Failed to fetch the Data please refresh or wait sometime !')
        return render(request , 'news/headline.html')
        



def ReadArticles(request , domian):
    
    try:
        if domian == 'news':
            news = list(HeadlineScrapper('https://news.google.com/topics/CAAqKggKIiRDQkFTRlFvSUwyMHZNRFZxYUdjU0JXVnVMVWRDR2dKSlRpZ0FQAQ?hl=en-IN&gl=IN&ceid=IN%3Aen'))
        if domian == 'catenews':
            news = list(CategoryScrapper('https://news.google.com/topics/CAAqJQgKIh9DQkFTRVFvSUwyMHZNRE55YXpBU0JXVnVMVWRDS0FBUAE?hl=en-IN&gl=IN&ceid=IN%3Aen'))
        if domian == 'localNews':
            news = list(LocalNewsScrapper(['https://news.google.com/topics/CAAqHAgKIhZDQklTQ2pvSWJHOWpZV3hmZGpJb0FBUAE/sections/CAQiWENCSVNQRG9JYkc5allXeGZkakpDRUd4dlkyRnNYM1l5WDNObFkzUnBiMjV5RGhJTUwyY3ZNVEZuZWpZMVp6aGplZzRLREM5bkx6RXhaM28yTldjNFl5Z0EqNQgAKjEICiIrQ0JJU0dqb0liRzlqWVd4ZmRqSjZEZ29NTDJjdk1URm5lalkxWnpoaktBQVABUAE?hl=en-IN&gl=IN&ceid=IN%3Aen']))
        if domian == 'BuisnessNews':
            news = list(BuisnessScrapper('https://news.google.com/topics/CAAqKggKIiRDQkFTRlFvSUwyMHZNRGx6TVdZU0JXVnVMVWRDR2dKSlRpZ0FQAQ?hl=en-IN&gl=IN&ceid=IN%3Aen'))
        if domian == 'worldNews':
            news = list(WorldNewsScrapper('https://news.google.com/topics/CAAqKggKIiRDQkFTRlFvSUwyMHZNRGx1YlY4U0JXVnVMVWRDR2dKSlRpZ0FQAQ?hl=en-IN&gl=IN&ceid=IN%3Aen'))
        if domian == 'EntertainmentNews':
            news = list(EntertainmentScrapper(['https://news.google.com/topics/CAAqKggKIiRDQkFTRlFvSUwyMHZNREpxYW5RU0JXVnVMVWRDR2dKSlRpZ0FQAQ?hl=en-IN&gl=IN&ceid=IN%3Aen']))
        if domian == 'TechnologyNews':
            news = TechnologyScrapper('https://news.google.com/topics/CAAqKggKIiRDQkFTRlFvSUwyMHZNRGRqTVhZU0JXVnVMVWRDR2dKSlRpZ0FQAQ?hl=en-IN&gl=IN&ceid=IN%3Aen')
        if domian == 'SportsNews':
            news = SportsScrapper('https://news.google.com/topics/CAAqKggKIiRDQkFTRlFvSUwyMHZNRFp1ZEdvU0JXVnVMVWRDR2dKSlRpZ0FQAQ?hl=en-IN&gl=IN&ceid=IN%3Aen')
        Context = {'news':news }
        return render(request , 'news/Readmore.html' , Context)
    except Exception as error:
        messages.WARNING(request , 'Failed to fetch the full article! please retry after some time')
        return render(request , 'news/Readmore.html')