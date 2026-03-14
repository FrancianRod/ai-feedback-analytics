from sqlalchemy import create_engine

def get_engine():
    engine = create_engine("sqlite:///feedback.db")
    return engine

def save_to_database(df, table_name="feedback_analysis"):
    engine = get_engine()
    df.to_sql(table_name, engine, if_exists='append', index=False)
