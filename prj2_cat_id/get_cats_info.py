from pathlib import Path

def get_cats_info(path):
    file_path = Path(path)
    if file_path.exists():
            with open(file_path, "r", encoding='utf-8') as fh:
                lines = [el.strip() for el in fh.readlines()]
                list_of_lists = [item.split(',') for item in lines]             
                keys = ["id", "name", "age"]
                list_of_dicts = [dict(zip(keys, item)) for item in list_of_lists]
                return list_of_dicts          
    else :
        print(f'Файл {file_path} не існує')

