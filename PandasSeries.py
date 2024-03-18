# -*- coding: utf-8 -*-
"""
Created on Mon Mar 18 00:28:11 2024

@author: NIKHIL
"""
"""
What is a Series?
A Pandas Series is like a column in a table.

It is a one-dimensional array holding data of any type.
"""

import pandas as pd
a=[1,3,4]
myvar= pd.Series(a)
print(myvar)
"""
Labels
If nothing else is specified, the values are labeled with their index number. First value has index 0, second value has index 1 etc.

This label can be used to access a specified value.

"""
print(myvar[1])

"""
Create Labels
With the index argument, you can name your own labels.
"""

mylabel=pd.Series(a,index=["x","y","z"],dtype="float",name="python")
print(mylabel)

# access the values of the series by your own labels
print(mylabel["y"])

"""
Key/Value Objects as Series

"""
Calories={"Day1":500,"Day2":5005,"Day3":3000,"Day4":1800}
mySeries=pd.Series(Calories)
print(mySeries)
"""
just like dictionary the keys of the series becomes labels
"""

#To select only some of the items in the dictionary, use the index argument and specify only the items you want to include in the Series.

Calories2={"Day1":3000,"Day2":3400,"Day3":3400,"Day5":5000}
myvar2=pd.Series(Calories2,index=["Day1","Day2"])
print(myvar2)
"""
DataFrames
Data sets in Pandas are usually multi-dimensional tables, called DataFrames.

Series is like a column, a DataFrame is the whole table.
"""
data = {
  "Days":["Day1","Day2","Day3"],
  "calories": [420, 380, 390],
  "duration": [50, 40, 45]
}

myvar4 = pd.DataFrame(data,index=[".",".","."])

print(myvar4)