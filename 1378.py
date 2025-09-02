import pandas as pd

def replace_employee_id(employees: pd.DataFrame, employee_uni: pd.DataFrame) -> pd.DataFrame:
    jn = employees.merge(employee_uni, how='left', on='id')
    return jn[['unique_id', 'name']]