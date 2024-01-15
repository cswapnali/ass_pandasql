import pandas as pd
import pandasql as ps

df = pd.read_csv('Assignment_Timecard.csv')

df['Time'] = pd.to_datetime(df['Time'], errors='coerce')
df['Time Out'] = pd.to_datetime(df['Time Out'], errors='coerce')

# calculate shift duration in hours
df['Shift Duration'] = (df['Time Out'] - df['Time']).dt.total_seconds() / 3600

query = """
    SELECT DISTINCT "Employee Name", "Position ID"
    FROM df
    WHERE "Shift Duration" > 14
"""

result = ps.sqldf(query, locals())

print('Employee who has worked for more than 14 hours in a single shift: \n', result)