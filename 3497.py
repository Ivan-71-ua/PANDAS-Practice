
import pandas as pd

def analyze_subscription_conversion(user_activity: pd.DataFrame) -> pd.DataFrame:
    grp = user_activity.groupby('user_id', as_index = False).agg(
        trial_avg_duration = ('activity_duration', 'mean'),
        paid_avg_duration = ('activity_duration', 'mean')
    )
    return grp.loc[grp['paid_avg_duration'] > 0]