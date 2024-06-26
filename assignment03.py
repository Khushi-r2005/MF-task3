import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime

data=pd.read_csv(r"C:\Users\ranik\OneDrive\Desktop\assignments\householdtask3.csv")

display(data.head(10))

#satter plot with year against own
plt.scatter(data['year'],data['own'])
#adding title to the plot
plt.title('Scatter plot')
#setting the x and y labels
plt.xlabel('year')
plt.ylabel('own')
#adding the legends
plt.show()

#line chart with year against own
plt.plot(data['year'])
plt.plot(data['own'])
#adding title to the plot
plt.title('Line Chart')
#setting the x and y labels
plt.xlabel('year')
plt.ylabel('own')
#adding the legends
plt.show()

#Bar Chart
plt.bar(data['year'],data['own'])
#adding title to the plot
plt.title('Bar Chart')
#setting the x and y labels
plt.xlabel('year')
plt.ylabel('own')
#adding the legends
plt.show()

#Histogram
plt.hist(data['income'])
#adding title to the plot
plt.title('Histogram')
#adding the legends
plt.show()
