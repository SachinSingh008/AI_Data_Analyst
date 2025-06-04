# data_loader.py
import pandas as pd

def load_data(file_path: str):
    try:
        return pd.read_csv(file_path)
    except Exception as e:
        raise ValueError(f"Error loading file: {e}")
