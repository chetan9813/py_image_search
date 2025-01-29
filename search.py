#!/usr/bin/env python3

import requests
from bs4 import BeautifulSoup
import webbrowser

def open_in_browser(image_url_list, cnt): 
    lcnt = 0
    for STR in image_url_list: 
        if lcnt >= cnt: 
            break 
        else: 
            lcnt += 1
            webbrowser.open(STR)
            
    return 

def search_google_images(query):
    url = f"https://www.google.com/search?tbm=isch&q={query}"
    headers = {'User-Agent': 'Mozilla/5.0'}
    response = requests.get(url, headers=headers)
    
    toret = [] 
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        images = soup.find_all('img')

        for idx, image in enumerate(images):
            image_url = image['src']
            toret.append(f"{image_url}")
    else:
        print("Failed to retrieve search results.")
    
    return toret

def get_urls_of_images(prompt): 
    urls = search_google_images(prompt)
    if urls:
        urls.remove(urls[0])  # Remove the first URL (usually a logo or irrelevant)
    return urls

fixed_prompt = "your_college_name_+_city_name"
temp_prompt = input("Give the temp_prompt : ")

open_in_browser(get_urls_of_images(temp_prompt + fixed_prompt), 2)
