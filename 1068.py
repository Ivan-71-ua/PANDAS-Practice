
import pandas as pd



def sales_analysis(sales: pd.DataFrame, product: pd.DataFrame) -> pd.DataFrame:
    res = sales.merge(product, how ='inner', on = 'product_id')
    return res[['product_name', 'year', 'price']]