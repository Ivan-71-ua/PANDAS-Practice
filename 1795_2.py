import pandas as pd

def rearrange_products_table(products: pd.DataFrame) -> pd.DataFrame:
    stores = ['store1', 'store2', 'store3']
    mylist = []
    for row in products.itertuples():
        for store in stores:
            price = getattr(row, store)
            if pd.notna(price):
                mylist.append({
                    'product_id' : row.product_id,
                    'store' : store,
                    'price' : price,
                })
    return pd.DataFrame(mylist, columns=['product_id', 'store', 'price'])
