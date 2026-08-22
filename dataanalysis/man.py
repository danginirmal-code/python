import pandas as pd
# df=pd.read_csv('sales.csv')
# print(df.head)
# print(df.describe())

# ##Handling missing values
# print(df.isnull().any(axis=1))
# print(df.isnull().sum())
# df['Sales_fillNA']=df['Sales'].fillne(df['Sales'].mean())
# df=df.rename(columns={'Date':'Sale Date'})
# df.head()
# df['Value_new']=df['Value'].fillna(df['Value'].mean()).astype(int)
# df.head()
# df['New Value']=df['Value'].apply(lambda x:x*2)
# df.head()

# grouped_sum=df.groupby(['Product','Region'])['Value'].sum()
# print(grouped_sum)

# grouped_sum=df.groupby(['Product','Region'])['Value'].mean()
# print(grouped_sum)

# group_agg=df.groupby('Region')['Value'].agg(['mean','sum','count'])
# group_agg

#Merging and joining data frames
df1=pd.DataFrame({'key':['A','B','C'],'value':[1,2,3]})
df2=pd.DataFrame({'key':['A','B','D'],'value':[4,5,6]})
# print(df1)
# print(df2)
print(pd.merge(df1,df2,on='key',how='inner'))
print(pd.merge(df1,df2,on='key',how='outer'))
print(pd.merge(df1,df2,on='key',how='left'))
print(pd.merge(df1,df2,on='key',how='right'))