import pandas as pd
import numpy  as np
arr=[31,28,31,30]
mon=['jan','feb','mar','apr']
obj=pd.Series(data=arr,index=mon)
print(obj)