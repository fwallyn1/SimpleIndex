from index.index import Index
from index.utils import extract_urls, save_index_to_json



if __name__=="__main__":
    urls = extract_urls()
    urls = urls[30:40]
    index = Index(urls)
    index.create_iverse_index()
    reverse_index = index.get_inverse_index()
    print(index.get_stats())
    save_index_to_json(reverse_index,".","first_index")