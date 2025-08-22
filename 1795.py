import pandas as pd

def rearrange_products_table(products: pd.DataFrame) -> pd.DataFrame:
    mylist = []
    for _, row in products.iterrows():
        if pd.notna(row['store1']):
            mylist.append({'product_id' : row['product_id'], 'store' : 'store1', 'price' : row['store1']})
        if pd.notna(row['store2']):
            mylist.append({'product_id' : row['product_id'], 'store' : 'store2', 'price' : row['store2']})
        if pd.notna(row['store2']):
            mylist.append({'product_id' : row['product_id'], 'store' : 'store3', 'price' : row['store3']})
    mylist.sort(key = lambda i: i['product_id'])
    return pd.DataFrame(mylist)

