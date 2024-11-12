import os
import pandas as pd

def save_dataset_to_csv(dataset, filename, directory = '../results/'):
    if not os.path.exists(directory):
        os.makedirs(directory)
    file_path = os.path.join(directory, filename)
    
    #dataset.to_csv(file_path, index=False)
    dataset.to_csv(file_path, sep='\t', index=False)

    
    print(f"Dataset saved to: {os.path.abspath(file_path)}")

