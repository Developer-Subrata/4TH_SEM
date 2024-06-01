import matplotlib.pyplot as plt
import pandas as pd 
df=pd.read_csv('MelaSales.csv')
df.plot(kind='line',color=['red','blue','brown'])
plt.title('Mela Sales Report')
plt.xlabel('Days')
plt.ylabel('Sales In Rs')
plt.show()