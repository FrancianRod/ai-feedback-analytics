import pandas as pd
import kagglehub
from kagglehub import KaggleDatasetAdapter

def load_data():
    print("Baixando dataset do Kaggle...")
    df = kagglehub.load_dataset(
        KaggleDatasetAdapter.PANDAS,
        "akashbommidi/customer-support-data",
        "Customer_support_data.csv",
    )
    
    # Remove espaços em branco invisíveis nos nomes das colunas
    df.columns = df.columns.str.strip()

    # Mapeamento corrigido baseado no seu terminal
    mapping = {
        'Unique id': 'id',
        'Customer Remarks': 'comentario',
        'category': 'area'
    }
    
    print("Aplicando mapeamento de colunas...")
    df = df.rename(columns=mapping)
    return df

def preprocess_data(df):
    # Garante que os comentários sejam strings e remove nulos
    df['comentario'] = df['comentario'].astype(str)
    df = df.dropna(subset=['comentario'])
    return df