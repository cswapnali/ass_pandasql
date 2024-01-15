import pandas as pd
import pandasql as ps

df = pd.read_csv('Assignment_Timecard.csv')

df['Time'] = pd.to_datetime(df['Time'])
df['Time Out'] = pd.to_datetime(df['Time Out'])

df.sort_values(['Employee Name', 'Time'], inplace=True)

# difference between two consecutive shifts
df['Time Difference'] = df.groupby('Employee Name')['Time'].diff()

# replace NaN values 
df['Time Difference'].fillna(pd.Timedelta(seconds=0), inplace=True)

# convert timedelta to seconds (integer) 
df['Time Difference'] = df['Time Difference'].dt.total_seconds().astype(int)

query = """
    SELECT DISTINCT "Employee Name", "Position ID", "Time Difference"
    FROM df
    WHERE "Time Difference" > 3600 AND "Time Difference" < 36000
"""

result = ps.sqldf(query, locals())
print('Employee who have less than 10 hours between shifts but greater than 1-hour: \n', result)