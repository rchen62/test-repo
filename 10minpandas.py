# -*- coding: utf-8 -*-
"""
Created on Thu Nov 16 12:24:54 2017

@author: rchen
"""

import pandas as pd
import numpy as np
#import matplotlib.pyplot as plt

'''
OBJECT CREATION
'''
#Creating a Series by passing a list of values, letting pandas create a default integer index:
s = pd.Series([1,3,5,np.nan,6,8])
print(s)


#Creating a DataFrame by passing a numpy array, with a datetime index and labeled columns:
dates = pd.date_range('20130101', periods=6)
print(dates)

df = pd.DataFrame(np.random.randn(6,4), index=dates, columns=list('ABCD'))
print(df)


#Creating a DataFrame by passing a dict of objects that can be converted to series-like.
df2 = pd.DataFrame({ 'A' : 1.,
                    'B' : pd.Timestamp('20130102'),
                    'C' : pd.Series(1,index=list(range(4)),dtype='float32'),
                    'D' : np.array([3] * 4,dtype='int32'),
                    'E' : pd.Categorical(["test","train","test","train"]),
                    'F' : 'foo' })

print(df2)

#show data types in dataframe
df2.dtypes


'''
VIEWING DATA
'''

#See the top & bottom rows of the frame
df.head()
df.tail(3)

#Display the index, columns, and the underlying numpy data
df.index
df.columns
df.values

#Describe shows a quick statistic summary of your data
df.describe()

#Transposing your data
df.T

#Sorting by an axis
df.sort_index(axis=1, ascending=False)

#Sorting by values
df.sort_values(by='B')


'''
SELECTION GETTING
'''

#Selecting a single column, which yields a Series, equivalent to df.A
df['A']

#slicing the rows
df[0:3]

'''
SELECTION BY LABEL
'''

#cross section using a label
df.loc[dates[0]]

#multi-axis by label
df.loc[:,['A','B']]
df.loc['20130102':'20130104',['A','B']]
df.loc['20130102',['A','B']]

#get scalar value
df.loc[dates[0],'A']


'''
SELECTION BY POSITION
'''

#select via the position of passed integer
df.iloc[3]

#select by slices
df.iloc[3:5,0:2]
df.iloc[[1,2,4],[0,2]]
df.iloc[1:3,:] 
df.iloc[:,1:3]

#get value explicitly
df.iloc[1,1]


'''
BOOLEAN INDEXING
'''

#Using a single column’s values to select data.
df[df.A > 0]


#select df on entire set
df[df > 0]


#Using the isin() method for filtering
df2 = df.copy()
df2['E'] = ['one', 'one','two','three','four','three']
df2
df2[df2['E'].isin(['two','four'])]


'''
SETTING
'''

#Setting a new column automatically aligns the data by the indexes
s1 = pd.Series([1,2,3,4,5,6], index=pd.date_range('20130102', periods=6))
s1

#add another column (F) to df
df['F'] = s1


#set new values
#by label
df.at[dates[0],'A'] = 0
#by position
df.iat[0,1] = 0
#by assigning with numpy array
df.loc[:,'D'] = np.array([5] * len(df))

print(df)

#A where operation with setting
df3 = df.copy()
df3[df3 > 0] = -df3
df3

'''
MISSING DATA
'''

