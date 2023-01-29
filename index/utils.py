import json 
import os
from bs4 import  BeautifulSoup
import requests
import time
from typing import List,Dict
import socket

def extract_urls(path_to_urls_json):
    with open(path_to_urls_json) as f :
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


def save_index_to_json(index:Dict, path_directory, file_name,is_pos=False):
    pos_str = ".pos_index" if is_pos else ".non_pos_index"
    file_path = os.path.join(path_directory,file_name+pos_str+".json")
    with open(file_path,'w') as f:
        f.write(json.dumps(index,ensure_ascii=False)) 

def save_metada_to_json(metadadata:Dict,path_directory : str):
    file_path = os.path.join(path_directory,"metadata.json")
    with open(file_path,'w') as f:
        f.write(json.dumps(metadadata,ensure_ascii=False))
