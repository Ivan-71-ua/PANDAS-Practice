import pandas as pd


def count_unique_subjects(teacher: pd.DataFrame) -> pd.DataFrame:
    mydict = {}
    for _, row in teacher.iterrows():
        id = row['teacher_id']
        sub = row['subject_id']
        print(id, sub)
        if id not in mydict:
            mydict[id] = set()

        mydict[id].add(sub)

    mylist = []

    for id, sub in mydict.items():
        mylist.append({'teacher_id': id, 'cnt': len(sub)})

    return pd.DataFrame(mylist)