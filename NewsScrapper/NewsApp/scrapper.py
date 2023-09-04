import requests
from bs4 import BeautifulSoup


def Scrapper(newslist):

     # create a list to store the value of news 
    NewsData = []
    
    # loop through the list to access the website
    for news in newslist:
        response = requests.get(news)

        # check if module succesfully get the request 
        if response.status_code == 200:
            
            
            # create a Soup With html content
            Soup = BeautifulSoup(response.content , 'html.parser')
            
            # Find Category 
            news_category = Soup.find('h2' , attrs={ 'class':'BPNpve' })
            
            
            # find div that conatins the news 
            Heading_Class = Soup.find_all('c-wiz' , attrs={ 'class':'PO9Zff Ccj79 kUVvS' })
            
            # looping through all the class to acess news one by one 
            for Heading_links in Heading_Class:
                
                
                
                # Find Heading 
                Heading_tag = Heading_links.find('h4' , attrs={ 'class':'gPFEn' })
                
                # fetch image 
                Image_figure = Heading_links.find('img' , attrs={ 'class':'Quavad' })
                
                # find appropriate news icon div 
                News_web_icon = Heading_links.find('div' , attrs={ 'class':'MCAGUe' })
                
                
                # Find Upload time 
                Upload_Time = Heading_links.find('div' , attrs={ 'class':'UOVeFe' })
                
                
                if  Heading_tag is None or Upload_Time is None or Image_figure is None or News_web_icon is None :
                    continue
                else:
                    # get text of article 
                    Heading = Heading_tag.text
                    
                    # fetch Images Src
                    Headline_image = Image_figure.get('src')
                    
                    # Find link to Full Report 
                    Link_tab = Heading_links.find('a')
                    Link_Src = Link_tab.get('href')
                    
                    # fetch the upload time of article 
                    Upload_Time = Upload_Time.text
                    
                    # fetch the News website icon src 
                    News_Icon = News_web_icon.find('img')['src']
                    
                    # Combine link_src with domian to request the web 
                    domian = "https://news.google.com/" + Link_Src
                    
                    
                    news_article = {
                        'domian':domian ,
                        'heading':Heading , 
                        'News_Icon':News_Icon,
                        'Category':news_category,
                        'Upload_Time':Upload_Time,
                        'article_image':Headline_image ,
                    }
                    
                    
                    # append news details to list 
                    NewsData.append(news_article ) 

    # return the list with values
    return NewsData 

def HeadlineScrapper(url):
    NewsData = Scrapper([url])
    return NewsData

def CategoryScrapper(url):
    NewData = Scrapper([url])
    return NewData

def BuisnessScrapper(url):
    NewsData = Scrapper([url])
    return NewsData

def WorldNewsScrapper(url):
    NewsData = Scrapper([url])
    return NewsData

def TechnologyScrapper(url):
    NewsData = Scrapper([url])
    return NewsData

def SportsScrapper(url):
    NewsData = Scrapper([url])
    return NewsData



def LocalNewsScrapper(newslist):
        # loop through the list to access the website
        for news in newslist:
            response = requests.get(news)

            # create a list to store the value of news 
            LocalNewsList = []
            
            # check if module succesfully get the request 
            if response.status_code == 200:
                
                # create a Soup With html content
                Soup = BeautifulSoup(response.content , 'html.parser')
                
                # Find Category 
                news_category = Soup.find('h2' , attrs={ 'class':'BPNpve' })
                
                # find div that conatins the news 
                Heading_Class = Soup.find_all('c-wiz' , attrs={ 'class':'PO9Zff Ccj79 kUVvS' })
                
                # print(Heading_Class , "########### Heading Class")
             
                # looping through all the class to acess news one by one 
                for counter ,Heading_links in enumerate(Heading_Class):
                    
                    # Find Heading 
                    Heading_tag = Heading_links.find('h4' , attrs={ 'class':'JtKRv' })
                    
                    # fetch image 
                    Image_figure = Heading_links.find('img' , attrs={ 'class':'Quavad' })
                    
                    # find appropriate news icon div 
                    News_web_icon = Heading_links.find('div' , attrs={ 'class':'MCAGUe' })
                    
                    
                    # Find Upload time 
                    Upload_Time = Heading_links.find('div' , attrs={ 'class':'UOVeFe' })
                    
                    
                    if  Heading_tag is None or Upload_Time is None or Image_figure is None or News_web_icon is None :
                        continue
                    else:
                        # get text of article 
                        Heading = Heading_tag.text
                        
                        # fetch Images Src
                        Headline_image = Image_figure.get('src')
                        
                        # Find link to Full Report 
                        Link_tab = Heading_links.find('a')
                        Link_Src = Link_tab.get('href')
                        
                        # fetch the upload time of article 
                        Upload_Time = Upload_Time.text
                        
                        # fetch the News website icon src 
                        News_Icon = News_web_icon.find('img')['src']
                        
                        # Combine link_src with domian to request the web 
                        domian = "https://news.google.com/" + Link_Src
                        
                        
                        news_article = {
                            'domian':domian ,
                            'heading':Heading , 
                            'News_Icon':News_Icon,
                            'Category':news_category,
                            'Upload_Time':Upload_Time,
                            'article_image':Headline_image ,
                        }
                        
                 
                        # append news details to list 
                        LocalNewsList.append(news_article) 
            
        # return the list with values
        return LocalNewsList 
    
    
def EntertainmentScrapper(newslist):
        # create a list to store the value of news 
        EntertanimentNewsList = []
            
        # loop through the list to access the website
        for news in newslist:
            response = requests.get(news)

            # check if module succesfully get the request 
            if response.status_code == 200:
                
                # create a Soup With html content
                Soup = BeautifulSoup(response.content , 'html.parser')
                
                # Find Category 
                news_category = Soup.find('h2' , attrs={ 'class':'BPNpve' })
                
                # find div that conatins the news 
                Heading_Class = Soup.find_all('c-wiz' , attrs={ 'class':'PO9Zff Ccj79 kUVvS' })
                
             
                # looping through all the class to acess news one by one 
                for counter ,Heading_links in enumerate(Heading_Class):
                    
                    # Find Heading 
                    Heading_tag = Heading_links.find('h4' , attrs={ 'class':'JtKRv' })
                    
                    # fetch image 
                    Image_figure = Heading_links.find('img' , attrs={ 'class':'Quavad' })
                    
                    # find appropriate news icon div 
                    News_web_icon = Heading_links.find('div' , attrs={ 'class':'MCAGUe' })
                    
                    
                    # Find Upload time 
                    Upload_Time = Heading_links.find('div' , attrs={ 'class':'UOVeFe' })
                    
                    
                    if  Heading_tag is None or Upload_Time is None or Image_figure is None or News_web_icon is None :
                        continue
                    else:
                        # get text of article 
                        Heading = Heading_tag.text
                        
                        # fetch Images Src
                        Headline_image = Image_figure.get('src')
                        
                        # Find link to Full Report 
                        Link_tab = Heading_links.find('a')
                        Link_Src = Link_tab.get('href')
                        
                        # fetch the upload time of article 
                        Upload_Time = Upload_Time.text
                        
                        # fetch the News website icon src 
                        News_Icon = News_web_icon.find('img')['src']
                        
                        # Combine link_src with domian to request the web 
                        domian = "https://news.google.com/" + Link_Src
                        
                        
                        news_article = {
                            'domian':domian ,
                            'heading':Heading , 
                            'News_Icon':News_Icon,
                            'Category':news_category,
                            'Upload_Time':Upload_Time,
                            'article_image':Headline_image ,
                        }
                        
                       
                        # append news details to list 
                        EntertanimentNewsList.append(news_article) 
                        
                        
      
        # return the list with values
        return EntertanimentNewsList 
            






