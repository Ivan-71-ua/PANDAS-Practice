
import pandas as pd

def total_time(employees: pd.DataFrame) -> pd.DataFrame:
    data = {}
    for _, row in employees.iterrows():
        if (row['day'], row['emp_id']) not in data:
            data[(row['day'], row['emp_id'])] = 0
        data[(row['day'], row['emp_id'])] += row['out_time'] - row['in_time']
    rows = []
    for (day, emp_id), total in data.items():
        rows.append({'day' : day, 'emp_id' : emp_id, 'total_time' : total})
    return pd.DataFrame(rows)