



import pandas as pd


def total_time(employees: pd.DataFrame) -> pd.DataFrame:
    employees['duration'] = employees['out_time'] - employees['in_time']
    grp = employees.groupby(['event_day', 'emp_id'])['duration']
    total = grp.sum()
    total = total.reset_index()
    total.columns = ['day', 'emp_id', 'total_time']
    return total

