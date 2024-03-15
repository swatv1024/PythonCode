import pandas as pd

# Read data from CSV file into a DataFrame
data = pd.read_csv('data.csv')

# Display the first few rows of the DataFrame
print(data.head())

# Perform some basic analysis
print(data.describe())

# Selecting specific columns
print(data['column_name'])

# Filtering data
filtered_data = data[data['column_name'] > 100]

# Grouping data
grouped_data = data.groupby('column_name').mean()

# Plotting data (assuming Matplotlib is installed)
import matplotlib.pyplot as plt
data['column_name'].plot()
plt.show()
