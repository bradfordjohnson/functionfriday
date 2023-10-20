import pandas as pd

def clean_names(df):
    """
    Clean the column names of the given DataFrame:
    - remove leading and trailing spaces
    - replace spaces with underscores
    - convert to lowercase
    """
    df.columns = df.columns.str.strip().str.lower().str.replace(' ', '_')
    return df