import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
dataset=pd.read_csv('D:/mybooks/bank-full.csv',sep=';')
age=dataset['age']
#print('age=',age)
balance=dataset['balance']
#print('balance=',balance)
print(len(age));print(len(balance))

plt.scatter(age, balance , color='green')
#print(age,balance)
plt.title('age vs balance', fontsize=14)
plt.xlabel('age', fontsize=14)
plt.ylabel('balance', fontsize=14)
plt.grid(True)
plt.show()