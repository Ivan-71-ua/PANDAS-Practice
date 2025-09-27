
import pandas as pd

def reformat_table(department: pd.DataFrame) -> pd.DataFrame:
    perf = department.pivot(index = 'id', columns = 'month', values = 'revenue')
    month = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
    perf = perf.reindex(columns = month)
    perf = perf.add_suffix('_Revenue').reset_index()
    return perf
