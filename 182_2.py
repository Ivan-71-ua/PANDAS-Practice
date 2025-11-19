
import pandas as pd



def duplicate_emails(person: pd.DataFrame) -> pd.DataFrame:
    grp = person.groupby('email').size().reset_index(name = 'cnt')
    return grp.loc[grp.cnt > 1, ['email']]