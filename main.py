from index.non_pos_index import NonPosIndex
from index.pos_index import PosIndex
from index.utils import extract_urls, save_index_to_json, save_metada_to_json
import click
import os
@click.command()
@click.option('--export_path_directory', default='.')
@click.option('--export_filename', default='index')
@click.option('--path_to_urls_json', default=os.path.join("data","crawled_urls.json"))

def main(export_path_directory,export_filename,path_to_urls_json):
    urls = extract_urls(path_to_urls_json)
     #### Non Positional Index ####
    urls = urls[:10]
    non_pos_index = NonPosIndex(urls)
    non_pos_index.create_inverse_index()
    reverse_index = non_pos_index.get_inverse_index()
    metadata = non_pos_index.get_stats()
    save_index_to_json(reverse_index,export_path_directory,export_filename,is_pos=False)
    save_metada_to_json(metadadata=metadata,path_directory=export_path_directory)

    #### Positional Index ####
    pos_index = PosIndex(urls)
    pos_index.create_inverse_index()
    reverse_pos_index = pos_index.get_inverse_index()
    save_index_to_json(reverse_pos_index,export_path_directory,export_filename,is_pos=True)
if __name__=="__main__":
    main()