
import pandas as pd



def latest_login(logins: pd.DataFrame) -> pd.DataFrame:
    return (
        logins.groupby('user_id', as_index=False)
        .agg(
            last_stamp = ('time_stamp', lambda x: x[x.dt.year == 2020].max())
        ).dropna()
    )