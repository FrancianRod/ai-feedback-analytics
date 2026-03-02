import pandas as pd

def load_data(file_path: str) -> pd.DataFrame:
    df = pd.read_csv(file_path)
    return df

def preprocess_data(df: pd.DataFrame) -> pd.DataFrame:
    df['comment'] = df['comment'].astype(str)
    df.dropna(subset=['comment'], inplace=True)
    return df