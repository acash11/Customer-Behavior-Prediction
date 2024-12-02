#Process shopping_trends.csv

import pandas as pd

df = pd.read_csv('shopping_trends.csv')

print(df)

#unique_values = df['Frequency of Purchases'].unique()
#print(unique_values)


#Change Frequency to numerical data
frequency_mapping = {
    'Weekly': 52,
    'Fortnightly': 26,
    'Bi-Weekly': 26,
    'Monthly': 12,
    'Quarterly': 4,
    'Every 3 Months': 4,
    'Annually': 1
}

df['Frequency of Purchases (per year)'] = df['Frequency of Purchases'].map(frequency_mapping)
df = df.drop('Frequency of Purchases', axis='columns')
print(df['Frequency of Purchases (per year)'])

#Remove categorical data from the table

df = df[['Customer ID', 'Purchase Amount (USD)', 'Frequency of Purchases (per year)', 'Previous Purchases']]

df['Purchase Amount (USD)'] = (df['Purchase Amount (USD)'] - df['Purchase Amount (USD)'].mean()) / df['Purchase Amount (USD)'].std()
df['Frequency of Purchases (per year)'] = (df['Frequency of Purchases (per year)'] - df['Frequency of Purchases (per year)'].mean()) / df['Frequency of Purchases (per year)'].std()
df['Previous Purchases'] = (df['Previous Purchases'] - df['Previous Purchases'].mean()) / df['Previous Purchases'].std()

print(df)

output_file = '../../processed/shopping_trends_processed.csv'
df.to_csv(output_file, index=False)

