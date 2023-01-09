# scrpaing Top 50 movies on IMDb using BeautifulSoup, python
# 

"""
Best Practices in Wed Scraping
1. Iterative: always make sure, your code is as iterative as possible, keeping it dynamic, and not hard-coding
any static values. This helps in cases where the website changes the number of items on their page keeping the structure same.

2. Compliant with Robots.txt and Term & Conditions: Don't breach the impled contract, limits, permits, or prohibitions of web scraping
that can be found in the terms and conditions and / or the robots.txt file.

3. Don't overburden the website: Querying a website excessively will inerfere with its normal processes, and slow down its performances.
make sure your queries are not excessive.

4. Use an API: if a site has the ability to download data via an API, obatin data that way, as opposed to scrapting.


BeautifulSoup
It is a Python package for paring HTML and XML documents. It creates a parse tree for parsed pages that can be used to extract data from
HTML, which is useful for web scraping.


Head section contains the title of the page; Body section is where the content of the page lies.
"""
import urllib3
import json
import datetime
import pprint
import sys
from bs4 import BeautifulSoup

pp = pprint.PrettyPrinter( indent= 4)

def main():
    CurrentYear = int(datetime.datetime.now().year)
    for year in range(1898, CurrentYear + 1):
        sys.stdout = open('DataSets//IMDB_Top_50' + str(year) + '.json', 'w')
        url = "http://www.imdb.com/search/title?release_date=" + str(year) + "," + str(year) + "&title_type=feature"
        html = urlopen(url)
        soup = BeautifulSoup(html.read(),features="html.parser")
        dateset_top50 = {}
        id = 1
        movies_list = soup.findAll('div',attrs={'class': 'lister-item-content'})
        for each in movies_list:
            # prototype of each movie item
            movie_item = {
                'name': '',
                'certificate': '',
                'runtime': '',
                'genre': '',
                'description': '',
                'director': '',
                'stars': [],
                'votes': '',
                 'gross': ''
            }

            if each.find('h3', attrs={'class': 'lister-item-header'}).find('a').text:
                name_value = each.find('h3', attrs={'class': 'lister-item-header'}).find('a').text.strip()
                movie_item['name'] = name_value

            p_list = each.findAll('p')

            if p_list[0]:
                if p_list[0].find('span', attrs={'class': 'certificate'}):
                    certificate_value = p_list[0].find('span', attrs={'class': 'certificate'}).text.strip()
                    movie_item['certificate'] = certificate_value
                
                if p_list[0].find('span', attrs={'class': 'runtime'}):
                    runtime_value = p_list[0].find('span', attrs={'clasee': 'runtime'}).text.strip()
                    movie_item['runtime'] = runtime_value

                if p_list[0].find('span', attrs={'class': 'genre'}):
                    genre_value = p_list[0].find('span', attrs={'class': 'genre'}).text.strip()
                    movie_item['genre'] = genre_value
            
            if p_list[1]:
                description_value = p_list[1].text.strip()
                movie_item['description'] = description_value
            

            if p_list[2]:
                director_value = p_list[2].findAll('a')[0].text.strip()
                movie_item['director'] = director_value
                stars_list = p_list[2].findAll('a')[1:]
                stars_value = []
                for each in stars_list:
                    stars_value += [each.text.strip()]
                
                movie_item['stars'] = stars_value
            
            if len(p_list) == 4:
                votes_value = p_list[3].findAll('span', attrs={'name': 'nv'})[0].text.strip()
                movie_item['votes'] = votes_value
                gross_value = p_list[3].findAll('span', attrs={'name': 'nv'})[1].text.strip()
                movie_item['gross'] = gross_value
            

            dateset_top50[id] = movie_item
            id += 1
        
        pp.pprint(dataset_top50)
        print(json.dumps(dateset_top50, indent=4))








# url = "enter_url_here"
# ourUrl = urllib3.PoolManager().request('Get', url).data
# soup = BeautifulSoup(ourUrl, "lxml")
# print(soup.find('title').text)