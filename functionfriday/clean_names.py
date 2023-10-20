import pandas as pd


def clean_names(df):
    """
    Clean column names of a pandas DataFrame.
    
    Standardize column names by:
    - removing leading and trailing whitespace
    - converting to lowercase
    - replacing spaces and dashes with underscores
    
    Args:
        df (pd.DataFrame): DataFrame with dirty column names.

    Returns:
        pd.DataFrame: DataFrame with cleaned column names.
    """
    unwanted_chars = [' ', '-']
    for char in unwanted_chars:
        df.columns = df.columns.str.strip().str.lower().str.replace(char, '_')
    return df
