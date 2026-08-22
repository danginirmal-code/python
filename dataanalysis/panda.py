import pandas as pd
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

