# 9.
# Imports Excel data into a Pandas DataFrame and filters the list of employees based on hire_date falling between specific months and years.

import pandas as pd

# Load Excel data into a Pandas DataFrame
file_path = 'employee_data.xlsx'
df = pd.read_excel(file_path)

# Convert 'hire_date' column to datetime
df['hire_date'] = pd.to_datetime(df['hire_date'])

# Define the start and end dates for filtering
start_date = pd.to_datetime('2020-01-01')
end_date = pd.to_datetime('2021-12-31')

# Filter employees based on hire_date
filtered_employees = df[(df['hire_date'] >= start_date) & (df['hire_date'] <= end_date)]

# Display the filtered employees
print("List of employees hired between Jan 2020 and Dec 2021:")
print(filtered_employees)