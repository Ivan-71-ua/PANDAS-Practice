

import pandas as pd

def account_summary(users: pd.DataFrame, transactions: pd.DataFrame) -> pd.DataFrame:
    balc = (
        transactions.groupby('account', as_index=False)
        .agg(
            balance=('amount', 'sum')
        )
    )
    df = users.merge(balc, how='left', on = 'account')
    return df.loc[df['balance'] > 10000, ['name', 'balance']]