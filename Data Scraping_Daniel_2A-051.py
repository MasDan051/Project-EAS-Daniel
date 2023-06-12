#!/usr/bin/env python
# coding: utf-8

# In[1]:


import requests
import pandas as pd
from bs4 import BeautifulSoup


# In[3]:


from selenium import webdriver
import chromedriver_autoinstaller


# In[8]:


chromedriver_autoinstaller.install()
browser = webdriver.Chrome()


# In[9]:


browser.get('https://www.xaviermarks.com/property-search/?key=&sort=&jualsewa=0&tipeproperti=RUMAH&alamat=&ProvinceID=9&WilayahDataID=1&SubdistrictID=&kota=&pjp=&hargamin=500000000&hargamax=1500000000&IsVerified=&IsHotProperty=&IsMap=&latitude=&longitude=&OfficeID=&page=1')


# In[14]:


data_title = []
data_location = []
data_ppp_number = []
data_price = []

for index in range(1,100):
    browser_index = requests.get(f'https://www.xaviermarks.com/property-search/?key=&sort=&jualsewa=0&tipeproperti=RUMAH&alamat=&ProvinceID=9&WilayahDataID=1&SubdistrictID=&kota=&pjp=&hargamin=500000000&hargamax=1500000000&IsVerified=&IsHotProperty=&IsMap=&latitude=&longitude=&OfficeID=&page={index}')
    soup_index = BeautifulSoup(browser_index.content, 'html.parser')
    
    title = soup_index.find_all('h3', class_='title-sin_map')
    for each_title in title:
        data_title.append(each_title.text.strip())
    
    location = soup_index.find_all('div', class_='geodir-category-location fl-wrap')
    for each_location in location:
        data_location.append(each_location.text.strip())
        
    ppp_number = soup_index.find_all('p', class_='small-text')
    for each_ppp_number in ppp_number:
        data_ppp_number.append(each_ppp_number.text.strip())
    
    price = soup_index.find_all('h4', class_='listing-item-category-wrap')
    for each_price in price:
        data_price.append(each_price.text.strip())


# In[15]:


data = {
    'title' : data_title,
    'location' : data_location,
    'ppp_number' : data_ppp_number,
    'price' : data_price
}


# In[22]:


file = pd.DataFrame(data)


# In[23]:


file.to_csv('Data Scraping_Daniel_051.csv')

