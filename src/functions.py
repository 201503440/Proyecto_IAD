import os
import pandas as pd

# Funcion para guardar archivos CSV
def save_dataset_to_csv(dataset, filename, directory = '../results/'):
    if not os.path.exists(directory):
        os.makedirs(directory)
    file_path = os.path.join(directory, filename)
    
    #dataset.to_csv(file_path, index=False)
    dataset.to_csv(file_path, sep='\t', index=False)

    
    print(f"Dataset saved to: {os.path.abspath(file_path)}")


# Funcion para convertir string 'number+number' o 'number-number' a operacion de numeros o numero normal
def convert_and_sum(val):
    if isinstance(val, str) and '+' in val:
        nums = val.split('+')
        return int(nums[0]) + int(nums[1])
    elif isinstance(val, str) and '-' in val:
        nums = val.split('-')
        return int(nums[0]) - int(nums[1])
    elif isinstance(val, str) and val == 'UNKNOWN':
        return int(0)
    else:
        return int(val)