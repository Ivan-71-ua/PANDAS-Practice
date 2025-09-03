



import pandas as pd

def account_summary(users: pd.DataFrame, transactions: pd.DataFrame) -> pd.DataFrame:
    merg = users.merge(transactions, how='left', on='account')
    gr=(
        merg.groupby('name')
        .agg(
            balance=('amount', 'sum')
        ).reset_index()
    )
    #gr.loc[gr['balance'] > 0] also fine
    return gr.loc[gr['balance'] > 10000, ['name', 'balance']]