# -*- coding: utf-8 -*-
"""
Created on Mon Mar 18 21:29:33 2024

@author: NIKHIL
"""

import pandas as pd
list_1=[[1,2,3,4,5],[11,12,13,14,15]]
print(pd.DataFrame(list_1))



sr={"s":pd.Series([1,2,3,4]),"r":pd.Series([1,2,3,4])}
var3=pd.DataFrame(sr)
print(var3)