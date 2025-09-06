
import pandas as pd

def categorize_products(activities: pd.DataFrame) -> pd.DataFrame:
    dp = activities[['sell_date', 'product']].drop_duplicates()
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
    mr = cnt.merge(names, how='inner', on='sell_date')
    return mr
