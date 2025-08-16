import pandas as pd


def find_products(products: pd.DataFrame) -> pd.DataFrame:
    list_id = []
    for _, row in products.iterrows():
        if row['low_fats'] == 'Y' and row['recyclable'] == 'Y':
            list_id.append(row['product_id'])
    return pd.DataFrame({'product_id' : list_id})