from unicodedata import name
import re
import numpy as np
from attr import attributes, attrs
import pandas as pd
import requests
from bs4 import BeautifulSoup
import csv
import pprint

dict1 = []

web_developers = requests.get("https://clutch.co/web-developers")
soup = BeautifulSoup(web_developers.text, 'lxml')


web_developers1 = requests.get("https://clutch.co/web-developers?page=1")
soup1 = BeautifulSoup(web_developers1.text, 'lxml')

mobile_app_developers = requests.get("https://clutch.co/directory/mobile-application-developers")
soup2 = BeautifulSoup(mobile_app_developers.text, 'lxml')

mobile_app_developers1 = requests.get("https://clutch.co/directory/mobile-application-developers?page=1")
soup3 = BeautifulSoup(mobile_app_developers1.text, 'lxml')

soft_developers = requests.get("https://clutch.co/developers")
soup4 = BeautifulSoup(soft_developers.text, 'lxml')

soft_developers1 = requests.get("https://clutch.co/developers?page=1")
soup5 = BeautifulSoup(soft_developers1.text, 'lxml')

ar_reality = requests.get("https://clutch.co/developers/virtual-reality")
soup6 = BeautifulSoup(ar_reality.text, 'lxml')

ar_reality1 = requests.get("https://clutch.co/developers/virtual-reality?page=1")
soup7 = BeautifulSoup(ar_reality1.text, 'lxml')

ai_dev = requests.get("https://clutch.co/developers/artificial-intelligence")
soup8 = BeautifulSoup(ai_dev.text, 'lxml')

ai_dev1 = requests.get("https://clutch.co/developers/artificial-intelligence?page=1")
soup9 = BeautifulSoup(ai_dev1.text, 'lxml')

blockchain_dev = requests.get("https://clutch.co/developers/blockchain")
soup10 = BeautifulSoup(blockchain_dev.text, 'lxml')

blockchain_dev1 = requests.get("https://clutch.co/developers/blockchain?page=1")
soup11 = BeautifulSoup(blockchain_dev1.text, 'lxml')


def GetData(mega_soup):
    company = []
    website = []
    rating = []
    review_count = []
    min_projectSize = []
    hourly_rate = []
    employess = []
    location = []
    attributes = []

    companies = mega_soup.find_all('h3', attrs={'class':'company_info'})
    for i in companies:
        name = i.text.replace('\n', '')
        company.append(name)

    websites = mega_soup.select('.website-link__item')
    for i in websites:
        link = i.get('href', None)
        website.append(link)

    ratings = mega_soup.find_all('span', attrs= {'class': 'rating sg-rating__number'})
    for i in ratings:
        rat = i.text
        rating.append(rat)

    reviews = mega_soup.find_all('a', attrs={'class':'reviews-link sg-rating__reviews'})
    for i in reviews:
        rev = i.text.replace("\n", "")
        review_count.append(rev)

    for a in mega_soup.find_all('div', attrs={"class":"module-list"}):
        rates = a.find_all('span')
        for i in rates:
            attributes.append(i.text)

    for i in range(0,len(attributes)):
        if(i%4==0):
            min_projectSize.append(attributes[i])
        elif(i%4==1):
            hourly_rate.append(attributes[i])
        elif(i%4==2):
            employess.append(attributes[i])
        else:
            location.append(attributes[i])

    dict1 = {"Company":company,"Website": website, "Rating": rating, "Review Count": review_count, "Min Project Size": min_projectSize, "Hourly Rate" : hourly_rate, "Employees": employess, "location": location }
    return dict1

GetData(soup)
GetData(soup1)
GetData(soup2)
GetData(soup3)
GetData(soup4)
GetData(soup5)
GetData(soup6)
GetData(soup7)
GetData(soup8)
GetData(soup9)
GetData(soup10)
GetData(soup11)

df = pd.DataFrame(dict1)
df.to_csv('Output.csv')