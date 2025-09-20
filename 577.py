
import pandas as pd


def employee_bonus(employee: pd.DataFrame, bonus: pd.DataFrame) -> pd.DataFrame:
    mrdb = employee.merge(bonus, how = "left", on = "empId")
    filter = mrdb.loc[(mrdb.bonus < 1000) | (mrdb.bonus.isnull())]
    return filter[['name', 'bonus']]