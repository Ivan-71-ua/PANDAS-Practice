from collections import defaultdict

import pandas as pd


def capital_gainloss(stocks: pd.DataFrame) -> pd.DataFrame:
    items = defaultdict(int)
    for row in stocks.itertuples():
        if row.operation == 'Buy':
            items[row.stock_name] -= row.price
        else:
            items[row.stock_name] += row.price

    result = []
    for k, v in items.items():
        result.append({'stock_name': k, 'capital_gain_loss': v})

    return pd.DataFrame(result)


