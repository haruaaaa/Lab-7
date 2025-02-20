import json
import requests

#часть 1
city_name = "Staryy Oskol"
key = "ae5632602334b079d5c2b4e90057b430"
response = requests.post(f"https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={key}")
result1 = json.loads(response.text)
print('City for analysis: Staryy Oskol \nWeather results:', 
    result1['weather'][0]['description'], 
    '\nHumidity results:', result1['main']['humidity'],
    '%\nPressure results:', result1['main']['pressure'])



#часть 2
from newsapi import NewsApiClient

newsapi = NewsApiClient(api_key='e53dd6c3e004483e9a2460ad9c8b3d3a') 

def get_top_headlines_bbc():

    top_headlines = newsapi.get_top_headlines(sources='bbc-news')
    result_top = json.dumps(top_headlines)
    return result_top


def get_theme_by_keywords(keywords):

    theme = newsapi.get_everything(q= keywords)
    return theme


choice = int(input('What do you want to find? 1 - top BBC news, 2 - news by keywords: '))

if choice == 1:
    print('Top news of BBC:', get_top_headlines_bbc())

elif choice == 2:
        
    keywords = input( '\nEnter keywords to search for news:' )
    data = get_theme_by_keywords(keywords)
    
    if data['totalResults'] != 0:
        print('First 10 articles to be found:')
        for article in data['articles'][:10]:
            print(f"Title: {article['title']}")
            print(f"URL: {article['url']}\n")
    else:
        print('Sorry, found nothing for you')
        

