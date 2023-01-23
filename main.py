from index.index import Index
from index.utils import extract_urls, save_index_to_json



if __name__=="__main__":
    urls = extract_urls()
    urls = urls[:50]
    index = Index(urls)
    index.get_iverse_index()
    print(index.get_stats())
    save_index_to_json(index.index,".","first_index")