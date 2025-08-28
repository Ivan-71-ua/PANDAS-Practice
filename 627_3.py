import numpy as np
import pandas as pd


def swap_salary(salary: pd.DataFrame) -> pd.DataFrame:
    salary['sex'] = np.where(salary['sex'] == 'm', 'f', 'm')
    return salary