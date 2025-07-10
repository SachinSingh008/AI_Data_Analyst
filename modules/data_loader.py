import pandas as pd

def load_data(uploaded_file):
    try:
        if uploaded_file.name.endswith(".csv"):
            try:
                return pd.read_csv(uploaded_file)
            except UnicodeDecodeError:
                return pd.read_csv(uploaded_file, encoding="ISO-8859-1")
        elif uploaded_file.name.endswith(".xlsx"):
            return pd.read_excel(uploaded_file)
        elif uploaded_file.name.endswith(".json"):
            return pd.read_json(uploaded_file)
        else:
            raise ValueError("Unsupported file format")
    except Exception as e:
        raise ValueError(f"Error loading file: {e}")
