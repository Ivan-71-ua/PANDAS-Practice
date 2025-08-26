

import pandas as pd

import numpy as np


def capital_gainloss(stocks: pd.DataFrame) -> pd.DataFrame:
    stocks['price'] = np.where(stocks['operation'] == 'Buy', stocks['price'] * -1, stocks['price'])
    stocks = stocks.groupby('stock_name').agg({'price' : 'sum'}).reset_index()
    stocks.rename(columns={'price' : 'capital_gain_loss'}, inplace=True)
    return stocks
