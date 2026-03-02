from data_processing import load_data, preprocess_data
from llm_integration import analyze_comment
from database import save_to_database
import pandas as pd


def run_pipeline():
    print("Starting pipeline...")

    # 1️⃣ Load and preprocess data
    df = load_data("sample_feedback.csv")
    df = preprocess_data(df)

    results = []

    # 2️⃣ LLM analysis (mock layer)
    for _, row in df.iterrows():
        analysis = analyze_comment(row["comment"])

        results.append({
            "id": row["id"],
            "date": row["date"],
            "area": row["area"],
            "comment": row["comment"],
            "rating": row["rating"],
            "category": analysis["category"],
            "sentiment": analysis["sentiment"],
            "main_theme": analysis["main_theme"],
            "sentiment_score": analysis["sentiment_score"],
            "summary": analysis["summary"]
        })

    final_df = pd.DataFrame(results)

    # 3️⃣ Save to SQLite
    save_to_database(final_df)
    print("Data saved to SQLite successfully.")

    # 4️⃣ Export CSV for Power BI
    final_df.to_csv("feedback_analysis.csv", index=False)
    print("CSV exported successfully.")

    print("Pipeline executed successfully.")


if __name__ == "__main__":
    run_pipeline()