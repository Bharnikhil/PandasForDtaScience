# -*- coding: utf-8 -*-
"""
Created on Mon Mar 18 00:48:38 2024

@author: NIKHIL
"""

import pandas as pd
"""
What is a DataFrame?
A Pandas DataFrame is a 2 dimensional data structure, like a 2 dimensional array, or a table with rows and columns.
"""
data={
      "Calories":[30,40,50],
      "Duration":[2,3,4]
      }
df=pd.DataFrame(data,index=["a","b","c"])
print(df)

"""
Locate Row
As you can see from the result above, the DataFrame is like a table with rows and columns.

Pandas use the loc attribute to return one or more specified row(s)
"""
print(df.loc["a"])


#Note: This example returns a Pandas Series.
print(df.loc[["a","b"]])
#When using [], the result is a Pandas DataFrame.
#With the index argument, you can name your own indexes.

"""
Locate Named Indexes
Use the named index in the loc attribute to return the specified row(s).
print(df.loc["a"])
"""

"""
Load Files Into a DataFrame
If your data sets are stored in a file, Pandas can load them into a DataFrame.
"""
df=pd.read_csv(r"C:\Users\NIKHIL\Documents\Book1.csv")
print(df)