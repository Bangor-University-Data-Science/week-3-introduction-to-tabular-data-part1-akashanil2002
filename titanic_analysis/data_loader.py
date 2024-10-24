import pandas as pd

def load_titanic_data(filepath: str) -> pd.DataFrame:
    dt = pd.read_csv(filepath)
    return dt