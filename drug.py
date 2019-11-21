import pandas as pd 
import matplotlib.pyplot as plt
import tkinter as tk 
master = tk.Tk()
tk.Label(master, text="drug example:").grid(row=0)
entry = tk.Entry(master)
entry.grid(row=0, column=1)
master.mainloop()
#string=input('enter a drug example:')
data=pd.read_csv('D:\\mybooks\\usp_drug_classification.csv')
x=data[['drug_example','usp_category','usp_class']]
y=x[x.drug_example.str.contains(entry,regex =True,na=False)].drop_duplicates()
print()
i=1
for ind in y.index: 
    print(i,'drug:',x['drug_example'][ind], ' usp category: ', x['usp_category'][ind], ' usp class : ',x['usp_class'][ind]) 
    i+=1

#plots
y['usp_category'].hist(xrot=270)
plt.show()

