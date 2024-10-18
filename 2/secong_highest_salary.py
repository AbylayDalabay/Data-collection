import pandas as pd

def second_highest_salary(employee: pd.DataFrame) -> pd.DataFrame:
    best = sorted(list(set(employee['salary'])))

    return pd.DataFrame({
        'SecondHighestSalary': [best[-2] if len(best) >= 2 else None]
    })