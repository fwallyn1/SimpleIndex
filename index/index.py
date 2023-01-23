from typing import List
import string

from index.utils import download_url, extract_titles_from_html, flatten


class Index():
    def __init__(self,urls:List[str]) -> None:
        self.urls = urls
        self.index = {}
        self.stats = {
            "n_doc": 0,
            "n_token" : 1,
        }
        self.known_urls = {}
    
    def tokenize(self,title:str):
        token_title = title.split(sep=" ")
        for t in token_title:
            t = t.translate(str.maketrans('', '', string.punctuation))
        self.stats["n_token"] += len(token_title)
        return token_title        


    def get_iverse_index(self):
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
                j = 0
                for token in token_titles :
                    # Si le token n'est pas dans l'index
                    if token not in self.index.keys():
                        self.index[token]= [{i:1}]
                        self.known_urls[token] = {i : j}
                        j+=1
                    # Si le token est dans l'index mais n'est pas apparu dans le document i
                    elif url not in self.known_urls[token].keys() :
                        self.index[token].append({i:1})
                        self.known_urls[token][i] = j
                        j+=1
                    else :
                        self.index[token][self.known_urls[i]][i] += 1

                
    
    def get_stats(self):
        self.stats["mean_token_per_doc"] = self.stats["n_token"]/self.stats["n_token"] if self.stats["n_token"]!=0 else 0
        return self.stats
    

    

    