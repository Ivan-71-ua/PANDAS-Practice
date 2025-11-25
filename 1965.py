
import pandas as pd

def find_employees(employees: pd.DataFrame, salaries: pd.DataFrame) -> pd.DataFrame:
    merged = employees.merge(salaries, on='employee_id', how='outer')
    filter = merged[merged.name.isna() | merged.salary.isna()]
    return filter[['employee_id']].sort_values(by='employee_id')
