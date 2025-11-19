import pandas as pd


import pandas as pd

def duplicate_emails(person: pd.DataFrame) -> pd.DataFrame:
    cnt = person.email.value_counts()
    return pd.DataFrame(cnt[cnt > 1].index)