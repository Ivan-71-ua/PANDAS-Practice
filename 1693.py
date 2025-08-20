
import pandas as pd

def daily_leads_and_partners(daily_sales: pd.DataFrame) -> pd.DataFrame:
    grouped = daily_sales.groupby(['date_id', 'make_name'])
    counts = grouped[['date_id', 'make_name']].nunique()
    res = counts.reset_index()
    res.rename(columns = {'lead_id' : 'unique_leads', 'partner_id' : 'unique_partners'}, inplace = True)
    return res