import pandas as pd
import numpy as np
a=np.arange(9,13)
obj=pd.Series(index=a,data=a**2)
print(obj)