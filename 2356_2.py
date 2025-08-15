
import pandas as pd


def count_unique_subjects(teacher: pd.DataFrame) -> pd.DataFrame:
    grouped = teacher.groupby('teacher_id')

    subjects = grouped['subject_id']

    counts = subjects.nunique()

    result = counts.reset_index()
    result.columns = ['teacher_id', 'cnt']

    return result
