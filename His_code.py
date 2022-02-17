# Reading Data
import numpy as np
import pandas as pd

data = pd.read_csv("pd.csv")

data2= data.iloc[:,1:5]
data2

data2 = data2.sort_values(by=17, ascending=True, axis=1)
data2

capacity= pd.DataFrame(data=data.iloc[17,1:5])
capacity = capacity.transpose()
capacity

colname= data2.columns
colname
solve = pd.DataFrame(data= np.zeros((16, 4)),columns = colname)
2
solve

data3= data.iloc[:-3,-1:]
data3

frames= [solve,data3]
sol = pd.concat(frames, axis=1)
sol = pd.concat([sol,capacity], axis=0)
sol



for column in data2:
    for index in data2:
        if sol.at[17,column] > 0:
            min_col1= data2[column].idxmin()
            if sol.at[min_col1,'Demand'] > 0:
                sol.at[min_col1,column] = sol.at[min_col1,'Demand']
                sol.at[min_col1,'Demand']= sol.at[min_col1,'Demand']-sol.at[min_col1,'Demand']
                sol.at[17,column]= sol.at[17,column]-sol.at[min_col1,column]

print(data2)