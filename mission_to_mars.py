#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Dependencies
from bs4 import BeautifulSoup
import requests
from splinter import Browser
from splinter.exceptions import ElementDoesNotExist
import pandas as pd


# In[2]:


executable_path = {'executable_path': '/usr/local/bin/chromedriver'}
browser = Browser('chrome', **executable_path, headless=False)


# # Step One: Scraping

# ## NASA Mars News

# In[3]:


# NASA MARS NEWS URL

url = 'https://mars.nasa.gov/news/?page=0&per_page=40&order=publish_date+desc%2Ccreated_at+desc&search=&category=19%2C165%2C184%2C204&blank_scope=Latest'


# In[4]:


browser.visit(url)


# In[5]:


html = browser.html
soup = BeautifulSoup(html, 'html.parser')


# In[6]:


news = soup.find('ul', class_="item_list")
print(news)


# In[7]:


stories = news.find_all('li')


# In[8]:


print(stories)


# In[9]:


summary_list = []
title_list = []

for story in stories:
    summary = story.text.strip()
    summary_list.append(summary) 
    story_url = story.find('a')['href']
    title_list.append(story_url)
    
     
    print("News Story Title: " + story_url)
    print(" ")
    print("Summary: ")
    print(summary)
    print (" ")
    print("________")
    print(" ")

print("News Story Scraping Complete")


# In[10]:


print("LATEST News Story Title and Summary: " + title_list[0] + ":  " + summary_list[0])


# ## JPL Mars Space Images - Featured Image

# In[14]:


url2 = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'


# In[15]:


executable_path = {'executable_path': '/usr/local/bin/chromedriver'}
browser = Browser('chrome', **executable_path, headless=False)


# In[16]:


browser.visit(url2)
html = browser.html
soup = BeautifulSoup(html, 'html.parser')


# In[17]:


soup = BeautifulSoup(html, 'html.parser')
print(soup.prettify())


# In[18]:


imagecode = soup.find('a', class_="fancybox")
print(imagecode)


# In[19]:


image_link = imagecode.get('data-link')


# In[20]:


print(image_link)


# In[21]:


url3 = 'https://www.jpl.nasa.gov'


# In[22]:


featured_image_url = url3 + image_link
print(featured_image_url)


# ## Mars Weather

# In[29]:


url4 = 'https://twitter.com/marswxreport?lang=en'


# In[28]:


executable_path = {'executable_path': '/usr/local/bin/chromedriver'}
browser = Browser('chrome', **executable_path, headless=False)


# In[30]:


browser.visit(url4)
html = browser.html
soup = BeautifulSoup(html, 'html.parser')


# In[31]:


soup = BeautifulSoup(html, 'html.parser')
print(soup.prettify())


# In[32]:


weather_report = soup.find_all(class_="TweetTextSize TweetTextSize--normal js-tweet-text tweet-text")
weather_report[1]


# In[33]:


weather_list = []
for report in weather_report:
    wr = report.text.strip()
    weather_list.append(wr)
print("Scraping Complete")


# In[34]:


# Latest Mars Weather Report
mars_weather = weather_list[1]
print (mars_weather)


# ## Mars Facts

# In[ ]:


url5 = 'https://space-facts.com/mars/'


# In[ ]:


tables = pd.read_html(url5)
tables


# In[ ]:


mars_facts_df = tables[0]
mars_facts_df.columns = ['Fact', 'Mars Data']

mars_facts_df


# In[ ]:


mars_df = mars_facts_df.set_index('Fact')
mars_df


# In[ ]:


mars_facts_html_table = mars_df.to_html()
mars_facts_html_table 


# In[ ]:


clean_mars_facts_html_table = mars_facts_html_table.replace('\n', '')


# In[ ]:


clean_mars_facts_html_table


# In[ ]:


mars_df.to_html('mars_table.html')


# ## Mars Hemispheres

# In[64]:


url_cerberus = 'https://astrogeology.usgs.gov/search/map/Mars/Viking/cerberus_enhanced'


# In[89]:


executable_path = {'executable_path': '/usr/local/bin/chromedriver'}
browser = Browser('chrome', **executable_path, headless=False)


# In[90]:


browser.visit(url_cerberus)
html = browser.html
soup = BeautifulSoup(html, 'html.parser')


# In[91]:


cerberus = soup.find_all(class_="wide-image")
cerberus


# In[92]:


for link in cerberus:
    cerberus_image_link = (link['src'])


# In[93]:


print(cerberus_image_link)


# In[94]:


root_usgs_url = 'https://astrogeology.usgs.gov'


# In[95]:


cerberus_url = root_usgs_url + cerberus_image_link


# In[96]:


cerberus_url


# In[97]:


url_schiaparelli = 'https://astrogeology.usgs.gov/search/map/Mars/Viking/schiaparelli_enhanced'


# In[98]:


executable_path = {'executable_path': '/usr/local/bin/chromedriver'}
browser = Browser('chrome', **executable_path, headless=False)


# In[99]:


browser.visit(url_schiaparelli)
html = browser.html
soup = BeautifulSoup(html, 'html.parser')


# In[100]:


schiaparelli = soup.find_all(class_="wide-image")
schiaparelli


# In[101]:


for link in schiaparelli:
    schiaparelli_image_link = (link['src'])
schiaparelli_image_link


# In[103]:


schiaparelli_url = root_usgs_url + schiaparelli_image_link
schiaparelli_url


# In[104]:


url_syrtis = 'https://astrogeology.usgs.gov/search/map/Mars/Viking/syrtis_major_enhanced'


# In[105]:


executable_path = {'executable_path': '/usr/local/bin/chromedriver'}
browser = Browser('chrome', **executable_path, headless=False)


# In[106]:


browser.visit(url_syrtis)
html = browser.html
soup = BeautifulSoup(html, 'html.parser')


# In[107]:


syrtis = soup.find_all(class_="wide-image")
syrtis


# In[108]:


for link in syrtis:
    syrtis_image_link = (link['src'])
syrtis_image_link


# In[109]:


syrtis_url = root_usgs_url + syrtis_image_link
syrtis_url


# In[110]:


url_valles = 'https://astrogeology.usgs.gov/search/map/Mars/Viking/valles_marineris_enhanced'


# In[111]:


executable_path = {'executable_path': '/usr/local/bin/chromedriver'}
browser = Browser('chrome', **executable_path, headless=False)


# In[112]:


browser.visit(url_valles)
html = browser.html
soup = BeautifulSoup(html, 'html.parser')


# In[113]:


valles = soup.find_all(class_="wide-image")
valles


# In[114]:


for link in valles:
    valles_image_link = (link['src'])
valles_image_link


# In[115]:


valles_url = root_usgs_url + valles_image_link
valles_url


# In[116]:


cerberus_title = "Cerberus Hemisphere"


# In[117]:


schiaparelli_title = "Schiaparelli Hemisphere"


# In[118]:


syrtis_title = "Syrtis Major Hemisphere"


# In[119]:


valles_title = "Valles Marineris Hemisphere"


# In[120]:


hemisphere_image_urls = [{"title": cerberus_title, "img_url": cerberus_url}, 
                         {"title": schiaparelli_title, "img_url": schiaparelli_url},
                         {"title": syrtis_title, "img_url": syrtis_url},
                         {"title": valles_title, "img_url": valles_url}
                        ]


# In[121]:


hemisphere_image_urls


# In[ ]:




