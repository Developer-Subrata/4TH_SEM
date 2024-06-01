import pandas as pd
import matplotlib.pyplot as plt
df= pd.read_csv('MelaSales2.csv')
df.plot(kind='bar',x='DAYS',title='Mela Sales Report')
plt.ylabel('Sales in Rs')
plt.show()