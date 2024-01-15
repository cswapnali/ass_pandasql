import pandas as pd
from pandasql import sqldf

df = pd.read_csv('Assignment_Timecard.csv')

# print(df.head())

# employees who have worked for 7 consecutive days
def consecutive_days_query(df):
    query = """
        SELECT [Employee Name], [Position ID], MIN([Time]) as start_date, MAX([Time Out]) as end_date
        FROM df
        WHERE [Time] IS NOT NULL AND [Time Out] IS NOT NULL
    """
    result_df = sqldf(query, locals())

    result_df['start_date'] = pd.to_datetime(result_df['start_date'])
    result_df['end_date'] = pd.to_datetime(result_df['end_date'])

    result_df['days_worked'] = (result_df['end_date'] - result_df['start_date']).dt.days
    result_df = result_df[result_df['days_worked'] >= 6]

    return result_df

result = consecutive_days_query(df)
print('Employees who have worked for 7 consecutive days: \n', result[['Employee Name', 'Position ID']])
