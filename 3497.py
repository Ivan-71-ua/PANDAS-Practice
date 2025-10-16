
import pandas as pd

def analyze_subscription_conversion(user_activity: pd.DataFrame) -> pd.DataFrame:
    round2 = lambda x: round(x + 0.0001, 2)

    trial = (
        user_activity[user_activity['activity_type'] == 'free_trial']
        .groupby('user_id', as_index = False)['activity_duration']
        .mean()
        .rename(columns={'activity_duration': 'trial_avg_duration'})
    )

    paid = (
        user_activity[user_activity['activity_type'] == 'paid']
        .groupby('user_id', as_index = False)['activity_duration']
        .mean()
        .rename(columns={'activity_duration': 'paid_avg_duration'})
    )

    mr = pd.merge(trial, paid, on = 'user_id')

    mr['trial_avg_duration'] = mr['trial_avg_duration'].apply(round2)
    mr['paid_avg_duration'] = mr['paid_avg_duration'].apply(round2)
    return mr.sort_values('user_id')