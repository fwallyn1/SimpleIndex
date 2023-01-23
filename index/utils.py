import json 
import os
from bs4 import  BeautifulSoup
import requests
import time
from typing import List,Dict
import socket

def extract_urls():
    path_to_file = os.path.join("data","crawled_urls.json")
    with open(path_to_file) as f :
        json_list = json.load(f)
    return json_list

def download_url(url:str):
        try:
            x = requests.get(url,timeout=2)
            data = x.text
        except : 
            data = None
        return data

def extract_titles_from_html(html) -> List:
        soup = BeautifulSoup(html, 'html.parser')
        titles = []
        for t in soup.find_all('title'):
            title = t.get_text()
            titles.append(title)
        return titles

def flatten(l):
    return [item for sublist in l for item in sublist]


def save_index_to_json(index:Dict, path_directory, file_name):
    file_path = os.path.join(path_directory,file_name+".json")
    with open(file_path,'w') as f:
        f.write(json.dumps(index,ensure_ascii=False)) 
