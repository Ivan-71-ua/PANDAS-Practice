

import pandas as pd


def capital_gainloss(stocks: pd.DataFrame) -> pd.DataFrame:
    sign = stocks['operation'].map({'Buy' : -1, 'Sell' : 1})
    stocks['signed_price'] = sign * stocks['price']
    return (
        stocks.groupby('stock_name')
        .agg(
            capital_gain_loss = ('signed_price', 'sum')
        ).reset_index()
    )






