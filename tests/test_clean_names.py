import pandas as pd

from functionfriday.clean_names import clean_names

def test_clean_names():
    df = pd.DataFrame({' A ': [1, 2], 'B': [3, 4], 'C D': [5, 6], 'A-b': [1, 2]})
    df_cleaned = clean_names(df)
    assert list(df_cleaned.columns) == ['a', 'b', 'c_d', 'a_b']  
    
test_clean_names()