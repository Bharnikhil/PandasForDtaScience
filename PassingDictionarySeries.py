# -*- coding: utf-8 -*-
"""
Created on Mon Mar 18 21:11:05 2024

@author: NIKHIL
"""

import pandas as pd
mydata={"language":["java","c","c++","python"],"popularity":[20,30,40,50],"rank":[1,2,3,4]}
myvar= pd.Series(mydata)
print(myvar)


s1=pd.Series(12,index=[1,2,3,4,5])
#print(s1)
s2=pd.Series(12,index=[1,2])
print(s1+s2)



d={"a":[1,2,3,4,5],"s":[1,2,3,4,5],"d":[1,2,3,4,5]}
var1=pd.DataFrame(d,columns=["a","d"],index=["k","l","m","n","o"]) # when you only want to see a particular column
print(var1)


print(var1["a"]["k"])