import pandas as pd


def categorize_products(dp: pd.DataFrame) -> pd.DataFrame:
    return (
        dp.groupby('sell_date', as_index = False)
        .agg(
            num_sold = ('product', 'nunique'),
            products = ('product',
                        lambda s: ','.join(sorted(s.unique())))
        )
    )
