import pandas as pd
from io import StringIO
Data = '''
{"name": "John", "age": 25}
{"name": "Alice", "age": 30}
{"name": "Bob", "age": 35}
'''

df = pd.read_json(StringIO(Data), lines=True)

print(df)
print(df.to_json(orient='records'))

df=pd.read_csv('sales.csv',header=None)
print(df.head)
df.to_csv('wine.csv')

url="https://www.fdic.gov/bank-failures/failed-bank-list"
df=pd.read_html(url)
print(df)

