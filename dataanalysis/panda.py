import pandas as pd
import numpy as np
##Series
data=[1,2,3,4,5]
series=pd.Series(data)
print("Series",series)

## create a series form dictionary
data={'a':1,'b':2,'c':3}
series_dict=pd.Series(data)
print(series_dict)


data=[10,20,30]
index=['a','b','c']
pd.Series(data,index=index)

##Dataframe
data={
    'Name':["Krish","John","jack"],
     'Age':[25,30,45],
     'City':['Banglore','New york','Florida']
}
df=pd.DataFrame(data)
print(df)
print(np.array(df))


## Create a Dataframe from list of dictionaries
data=[
    {'Name':"Krish",'Age':32,'City':'Bangalore'},
    {'Name':"Jack",'Age':30,'City':'New york'},
    {'Name':"Man",'Age':25,'City':'Florida'}
]
df=pd.DataFrame(data)
print(df['Name'])
print(df.iloc[0][1])

#Accessing a specifid element
print(df['Name'])
print(df.at[2,'Name'])

#Accessing specified element using iat
df.iat[2,2]

##Data manipulation with dataframe
df['Salary']=[4000,5000,6000]
print(df)
df.drop('Salary',axis=1,inplace=True)
print(df)
df['Age']=df['Age']+1
print(df)
df.drop(0,inplace=True)
print(df)


# df=pd.read_csv('sales.csv')
# print(df.head(5))
# print(df['Region'])