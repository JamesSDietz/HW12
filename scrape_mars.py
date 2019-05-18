#  James S Dietz, HW 12 Python Code, WebScraping



# Dependencies
from bs4 import BeautifulSoup
import requests
from splinter import Browser
from splinter.exceptions import ElementDoesNotExist
import pandas as pd
import time


def scrape():

    mars = {}

# NASA Mars News

    executable_path = {'executable_path': '/usr/local/bin/chromedriver'}
    browser = Browser('chrome', **executable_path, headless=False)
    time.sleep(2) 
    url = 'https://mars.nasa.gov/news/?page=0&per_page=40&order=publish_date+desc%2Ccreated_at+desc&search=&category=19%2C165%2C184%2C204&blank_scope=Latest'
    browser.visit(url)
    time.sleep(2) 
    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')
    news = soup.find('ul', class_="item_list")
    stories = news.find_all('li')
    summary_list = []
    title_list = []
    for story in stories:
        summary = story.text.strip()
        summary_list.append(summary) 
        story_url = story.find('a')['href']
        title_list.append(story_url)
        title_list = [word.replace('-',' ') for word in title_list]
        title_list = [word.replace('/','') for word in title_list]
        title_list = [word.replace("news8438nasas","NASA's") for word in title_list]
    mars['news_title'] = title_list[0]
    mars['news_story'] = summary_list[0]

    time.sleep(1) 

# JPL Mars Space Images - Featured Image
# note on featured image: This code works fine in Jupyter notebook but it gives
#    me an error here.  I am therefore substituting alt code that this accepts bc
#    I am out of time.

    url2 = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'
    executable_path = {'executable_path': '/usr/local/bin/chromedriver'}
    browser = Browser('chrome', **executable_path, headless=False)
    time.sleep(2) 
    browser.visit(url2)
    time.sleep(2) 
    html = browser.html
    soup2 = BeautifulSoup(html, 'html.parser')
    #image_code = soup2.find(class_="lede").find('a')['href']
    #code from notebook above, alt code below
    for div in soup2.find_all('div', attrs={'class':'img'}):
        image_code = (div.find('img')['src'])
    url3 = 'https://www.jpl.nasa.gov'
    featured_image_url = url3 + image_code   
    mars['featured_image_url'] = featured_image_url

    time.sleep(1) 

# Mars Weather

    url4 = 'https://twitter.com/marswxreport?lang=en'
    executable_path = {'executable_path': '/usr/local/bin/chromedriver'}
    browser = Browser('chrome', **executable_path, headless=False)
    time.sleep(2) 
    browser.visit(url4)
    time.sleep(2) 
    html = browser.html
    soup3 = BeautifulSoup(html, 'html.parser')
    weather_report = soup3.find_all(class_="TweetTextSize TweetTextSize--normal js-tweet-text tweet-text")
    weather_list = []
    for report in weather_report:
        wr = report.text.strip()
        weather_list.append(wr)
    desiredwords = ['InSight']
    pruned_weather_list = [x for x in weather_list if any(word in x for word in desiredwords)]
    mars_weather = pruned_weather_list[0]
    mars['mars_weather'] = mars_weather
    
    time.sleep(1) 

# Mars Facts

    url5 = 'https://space-facts.com/mars/'
    tables = pd.read_html(url5)
    mars_facts_df = tables[0]
    mars_facts_df.columns = ['Fact', 'Mars Data']
    mars_df = mars_facts_df.set_index('Fact')
    mars_facts = mars_df.to_html(justify='left')
    mars['mars_facts'] = mars_facts

# Mars Hemispheres


    root_usgs_url = 'https://astrogeology.usgs.gov'

    url_cerberus = 'https://astrogeology.usgs.gov/search/map/Mars/Viking/cerberus_enhanced'
    executable_path = {'executable_path': '/usr/local/bin/chromedriver'}
    browser = Browser('chrome', **executable_path, headless=False)
    time.sleep(2) 
    browser.visit(url_cerberus)
    time.sleep(2)
    html = browser.html
    soup_cerberus = BeautifulSoup(html, 'html.parser')
    cerberus = soup_cerberus.find_all(class_="wide-image")
    for link in cerberus:
        cerberus_image_link = (link['src'])
    cerberus_url = root_usgs_url + cerberus_image_link

    url_schiaparelli = 'https://astrogeology.usgs.gov/search/map/Mars/Viking/schiaparelli_enhanced'
    executable_path = {'executable_path': '/usr/local/bin/chromedriver'}
    browser = Browser('chrome', **executable_path, headless=False)
    time.sleep(2) 
    browser.visit(url_schiaparelli)
    time.sleep(2) 
    html = browser.html
    soup_schiaparelli = BeautifulSoup(html, 'html.parser')
    schiaparelli = soup_schiaparelli.find_all(class_="wide-image")
    for link in schiaparelli:
        schiaparelli_image_link = (link['src'])
    schiaparelli_url = root_usgs_url + schiaparelli_image_link

    url_syrtis = 'https://astrogeology.usgs.gov/search/map/Mars/Viking/syrtis_major_enhanced'
    executable_path = {'executable_path': '/usr/local/bin/chromedriver'}
    browser = Browser('chrome', **executable_path, headless=False)
    time.sleep(2) 
    browser.visit(url_syrtis)
    time.sleep(2) 
    html = browser.html
    soup_syrtis = BeautifulSoup(html, 'html.parser')
    syrtis = soup_syrtis.find_all(class_="wide-image")
    for link in syrtis:
        syrtis_image_link = (link['src'])
    syrtis_url = root_usgs_url + syrtis_image_link

    url_valles = 'https://astrogeology.usgs.gov/search/map/Mars/Viking/valles_marineris_enhanced'
    executable_path = {'executable_path': '/usr/local/bin/chromedriver'}
    browser = Browser('chrome', **executable_path, headless=False)
    time.sleep(2)
    browser.visit(url_valles)
    time.sleep(2)
    html = browser.html
    soup_valles = BeautifulSoup(html, 'html.parser')
    valles = soup_valles.find_all(class_="wide-image")
    for link in valles:
        valles_image_link = (link['src'])
    valles_url = root_usgs_url + valles_image_link

    cerberus_title = "Cerberus Hemisphere"
    schiaparelli_title = "Schiaparelli Hemisphere"
    syrtis_title = "Syrtis Major Hemisphere"
    valles_title = "Valles Marineris Hemisphere"

    hemisphere_image_urls = [{"title": cerberus_title, "img_url": cerberus_url}, 
                            {"title": schiaparelli_title, "img_url": schiaparelli_url},
                            {"title": syrtis_title, "img_url": syrtis_url},
                            {"title": valles_title, "img_url": valles_url}
                            ]
    mars['hemisphere_urls'] = hemisphere_image_urls
    
    mars['cerberus_title'] = cerberus_title
    mars['schiaparelli_title'] = schiaparelli_title
    mars['syrtis_title'] = syrtis_title
    mars['valles_title'] = valles_title
    mars['cerberus_url'] = cerberus_url
    mars['schiaparelli_url'] = schiaparelli_url
    mars['syrtis_url'] = syrtis_url
    mars['valles_url'] = valles_url

    # Return Library
    return mars


