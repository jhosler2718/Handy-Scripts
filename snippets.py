# -*- coding: utf-8 -*-
"""
Created on Thu Jul 25 07:37:07 2024

@author: jason.hosler
"""

# Create a string named str
str = "Rahim and Karim"

# Convert a string to uppercase
str.upper() # 'RAHIM AND KARIM'

# Convert a string to lowercase
str.lower() # 'rahim and karim'

# Convert a string to title case
str.title() # 'Rahim And Karim' 

# Replaces matches of a substring with another
str.replace("J", "P") # 'Kahim and Rarim'


#Handle Missing Values & Remove Duplicates❓
df.dropna(inplace=True)  # Drop missing values
df.fillna(df.mean(), inplace=True)  # Fill missing values with mean

df.drop_duplicates(inplace=True)


#Rename Columns
df.rename(columns={'old_name': 'new_name'}, inplace=True)


#Group By and Aggregate
grouped_df = df.groupby('column').agg({'col1': 'sum', 'col2': 'mean'})


#Merge DataFrames
merged_df = pd.merge(df1, df2, on='common_column', how='inner')

#Pivot Table
pivot = df.pivot_table(values='value', index='index', columns='columns', aggfunc='mean')


#Apply Function to Column
df['new_column'] = df['column'].apply(lambda x: x*2)


#Model Evaluation — MSE and R²
mse = mean_squared_error(y_test, predictions)
r2 = r2_score(y_test, predictions)
print(f'MSE: {mse}, R²: {r2}')


#Time Series — Convert to Datetime
df['date'] = pd.to_datetime(df['date'])
df.set_index('date', inplace=True)


#Rolling Window Calculation
df['rolling_mean'] = df['column'].rolling(window=12).mean()


#Perform SQL Query on DataFrame
import pandasql as psql
query = "SELECT * FROM df WHERE column > value"
result = psql.sqldf(query, locals())


#Create a Dashboard with Plotly
import plotly.express as px
fig = px.line(df, x='date', y='value')
fig.show()






















