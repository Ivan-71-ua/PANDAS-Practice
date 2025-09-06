
import pandas as pd

def categorize_products(dp: pd.DataFrame) -> pd.DataFrame:
    cnt = (
        dp.groupby('sell_date', as_index = False)
        .agg(
            num_sold = ('product', 'nunique')
        )
    )
    names = (
        dp.groupby('sell_date', as_index = False)
        .agg(
            products = ('product',
                        lambda s: ','.join(sorted(s.unique(), key = str.lower))),
        )
    )
    return cnt.merge(names, how='inner', on='sell_date')
