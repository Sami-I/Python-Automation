import pandas as pd

df = pd.read_excel('supermarket_sales.xlsx')

#Indicate columns to select
df = df[['Gender', 'Product line', 'Total']]

print(df)

pivot_table = df.pivot_table(index='Gender', columns='Product line', values='Total', aggfunc='sum').round(0)

pivot_table.to_excel('pivot_tab'
                     'le.xlsx', 'Report', startrow=4)