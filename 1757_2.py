

import pandas as pd


def find_products(products: pd.DataFrame) -> pd.DataFrame:
    mask_low = products['low_fats'] == 'Y'
    mask_rec = products['recyclable'] == 'Y'
    both = mask_low & mask_rec
    #res = products[both][['product_id']]
    #not really need
    #res.reset_index(drop=True, inplace=True)
    return products[both][['product_id']]