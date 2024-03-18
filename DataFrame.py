# -*- coding: utf-8 -*-
"""
Created on Mon Mar 18 00:24:00 2024

@author: NIKHIL
"""
"""
Pandas is usually imported under the pd alias.
alias: In Python alias are an alternate name for referring to the same thing.

Create an alias with the as keyword while importing:
 """

import pandas as pd
mydataset={
    'Cars':["Verna","Audi","Lambo","KTM"],
    'Price':[20,30,40,50]

          }
myval=pd.DataFrame(mydataset);
print(myval)

print(pd.__version__)




