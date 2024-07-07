from pathlib import Path

def total_salary(path):
    file_path = Path(path)
    if file_path.exists():
            with open(file_path, "r", encoding='utf-8') as fh:
                lines = [el.strip() for el in fh.readlines()]
                lines_splitted = []
                for i in lines:
                    i = i.split(",")
                    lines_splitted += i
                num_list = [int(item) for item in lines_splitted if item.isdigit()]
                total = int() 
                for i in num_list:
                    total += i
                average = total/len(num_list)
                
            return [total,average]         
    else :
      print(f'Файл {file_path} не існує')

              

