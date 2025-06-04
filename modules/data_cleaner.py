# data_cleaner.py
def clean_data(df):
    df = df.dropna(how='all')  # Drop empty rows
    df.columns = df.columns.str.strip()
    return df
