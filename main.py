from data_processing import load_data, preprocess_data
from llm_integration import analyze_comment
from database import save_to_database
import pandas as pd

def run_pipeline():
    print("Iniciando processamento com dados do Kaggle...")
    
    # 1. Carrega e limpa os dados reais
    raw_df = load_data() 
    df = preprocess_data(raw_df)
    
    # 2. Amostra de segurança (20 linhas)
    df_sample = df.head(20)
    
    results = []
    print(f"Analisando {len(df_sample)} registros...")

    for index, row in df_sample.iterrows():
        analysis = analyze_comment(row['comentario'])
        
        results.append({
            "id": row['id'], # Agora vai funcionar porque o rename acima tratou isso
            "comentario_original": row['comentario'],
            "categoria_ia": analysis['category'],
            "sentimento": analysis['sentiment'],
            "tema_principal": analysis['main_theme'],
            "score": analysis['sentiment_score'],
            "resumo": analysis['summary']
        })
    
    final_df = pd.DataFrame(results)

    # 3. Salva no SQLite (feedback.db)
    save_to_database(final_df)
    print("✅ Dados salvos no SQLite com sucesso.")

    # 4. Exporta CSV para o Power BI
    final_df.to_csv("feedback_analysis.csv", index=False)
    print("📊 CSV exportado com sucesso.")

    print("🏁 Pipeline finalizado!")

if __name__ == "__main__":
    run_pipeline()