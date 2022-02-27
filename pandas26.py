import pandas as pd
import numpy as np
data={'a':0,'b':1.,'c':2.,'d':3.}
s=pd.Series(data,index=['b','c','d','a'])
print(s)