
import pandas as pd

def account_summary(users: pd.DataFrame, transactions: pd.DataFrame) -> pd.DataFrame:
    merg = users.merge(transactions, how='left', on='account')
    gr=(
        merg.groupby('name', as_index=False)
        .agg(
            balance=('amount', 'sum')
        )
    )
    gr = gr[gr['balance'] > 10000]
    return gr