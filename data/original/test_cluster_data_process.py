#Process shopping_trends.csv

import pandas as pd

df = pd.read_csv('test_cluster_data.csv')

print(df)

#Remove categorical data from the table

df = df.drop('Cluster_Label', axis='columns')
df = df.drop('Home State', axis='columns')
df = df.drop('Hobby', axis='columns')

df['time in store'] = (df['time in store'] - df['time in store'].mean()) / df['time in store'].std()
df['money spent'] = (df['money spent'] - df['money spent'].mean()) / df['money spent'].std()

df["Customer ID"] = [i for i in range(0,1000)]

print(df)
# Output to a CSV file
output_file = '../processed/test_cluster_data_processed.csv'
df.to_csv(output_file, index=False)

print(f"test data for clustering saved to {output_file}")