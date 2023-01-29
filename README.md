# 
# A Simple Index

Index positionnel et non-positionnel.

## Auteur

Francois Wallyn


## Installation des packages

```bash
  pip install -r requirements.txt
```
    
## Usage/Exemples
Pour lancer un exemple de crawler 

```bash
python3 main.py --path_to_urls_json ./data/crawled_urls.json --export_path_directory my/directory --export_filename my_index 
```
Avec les paramètres : 

- `--path_to_urls_json` : chemin vers le fichier json contenant la liste d'urls (défaut : "./data/crawled_urls.json")
- `--export_path_directory` : chemin vers le répertorire pour exporter l'index
- `--export_filename` nom de fichier d'index

Pour utiliser le framework et manipuler un index :

```python
from index.non_pos_index import NonPosIndex
from index.pos_index import PosIndex
from index.utils import extract_urls, save_index_to_json, save_metada_to_json


urls = extract_urls(path_to_urls_json)
crawler.run()
#### Non Positional Index ####
urls = urls
non_pos_index = NonPosIndex(urls)
non_pos_index.create_inverse_index()
reverse_index = non_pos_index.get_inverse_index()
metadata = non_pos_index.get_stats()
save_index_to_json(reverse_index,export_path_directory,export_filename)
save_metada_to_json(metadadata=metadata,path_directory=export_path_directory)

#### Positional Index ####
pos_index = PosIndex(urls)
pos_index.create_inverse_index()
reverse_pos_index = pos_index.get_inverse_index()
save_index_to_json(reverse_pos_index,export_path_directory,export_filename)
```