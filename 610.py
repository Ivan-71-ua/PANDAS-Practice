
import pandas as pd

def triangle_judgement(triangle: pd.DataFrame) -> pd.DataFrame:
    triangle['triangle'] = 'No'
    triangle.loc[(triangle['x'] + triangle['y'] > triangle['z']) & (triangle['x'] + triangle['z'] > triangle['y']) & (triangle['y'] + triangle['z'] > triangle['x']), 'triangle'] = 'Yes'
    return triangle