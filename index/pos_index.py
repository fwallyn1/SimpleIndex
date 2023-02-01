from typing import List, Dict, Union
import string

from index.utils import download_url, extract_titles_from_html, flatten
from copy import deepcopy

class PosIndex():
    def __init__(self,urls:List[str]=None) -> None:
        self.urls : List[str] = urls
        self.index : Dict[int,List[Dict[int,Dict[str,Union[int,List[int]]]]]]= {}
        self.stats = {
            "n_doc": 0,
            "n_token" : 1,
        }
        self.known_urls : Dict[int,Dict[int,int]]= {}
    
    def tokenize(self,title:str):
        token_title = title.translate(str.maketrans('', '', string.punctuation)).lower().strip('').split(sep=" ")
        token_title = [word for word in token_title if word]
        self.stats["n_token"] += len(token_title)
        return token_title      


    def create_inverse_index(self) -> None:
        for i,url in enumerate(self.urls):
            print(i,url)
            #print(self.index)
            html = download_url(url)
            if not html :
                print("URL : ", url, "not available")
                pass
            else :
                self.stats["n_doc"] += 1
                titles = extract_titles_from_html(html)
                token_titles = []
                for title in titles :
                    token_titles+=self.tokenize(title)
                for j,token in enumerate(token_titles) :
                    # Si le token n'est pas dans l'index
                    if token not in self.index.keys():
                        self.index[token]= [{i:{"count":1,"position":[j]}}]
                        self.known_urls[token] = {i : len(self.index[token])-1}
                    # Si le token est dans l'index mais n'est pas apparu dans le document i
                    elif i not in self.known_urls[token].keys() :
                        self.index[token].append({i:{"count":1,"position":[j]}})
                        self.known_urls[token][i] = len(self.index[token])-1
                    else :
                        self.index[token][self.known_urls[token][i]][i]["count"] += 1
                        self.index[token][self.known_urls[token][i]][i]["position"].append(j)
    
    def get_inverse_index(self) -> Dict:
        return self.index
    
    def get_stats(self):
        self.stats["mean_token_per_doc"] = self.stats["n_token"]/self.stats["n_doc"] if self.stats["n_doc"]!=0 else 0
        return self.stats