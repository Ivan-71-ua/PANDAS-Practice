
import pandas as pd

def find_primary_department(employee: pd.DataFrame) -> pd.DataFrame:
    dept_cnt = employee.groupby('employee_id')['department_id'].transform('nunique')

    mask = ((employee.primary_flag == 'Y') | (dept_cnt == 1))

    return employee.loc[mask, ['employee_id', 'department_id']]

