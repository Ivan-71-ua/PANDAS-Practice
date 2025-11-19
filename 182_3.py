import pandas as pd

def duplicate_emails(person: pd.DataFrame) -> pd.DataFrame:
    dup = person[person.email.duplicated(keep=False)]
    return dup[['email']].drop_duplicates()