#   __import__("atexit").register(lambda: open("display_runtime.txt", "w").write("0"))


import pandas as pd

def combine_two_tables(person: pd.DataFrame, address: pd.DataFrame) -> pd.DataFrame:
    merged = person.merge(address, how='left', on='personId')
    return merged[['lastName', 'firstName', 'city', 'state']]