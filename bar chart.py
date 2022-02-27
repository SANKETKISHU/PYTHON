import pandas as pd
x=pd.Series([10,12,13],index=['dhanbad','asansol','durgapur'])
y=pd.Series([1200,1300,1400],index=['dhanbad','asansol','durgapur'])
dft={'id':x,'salary':y}
dft1=pd.DataFrame(dft)                                       
print(dft1)
dft1.plot(kind='bar',x='id',y='salary')
