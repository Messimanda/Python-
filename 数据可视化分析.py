#!/usr/bin/env python
# coding: utf-8

# In[4]:


#画散点图
import matplotlib.pyplot as plt
import pandas as pd
#设置图框大小
data1=pd.read_csv(open(r"C:\Users\江炳青\Desktop\Customers.csv"),encoding='utf-8',index_col=0)
fig = plt.figure(figsize=(10,6))
plt.plot(data1['Annual Income (k$)'],data1['Spending Score (1-100)'],"o")
#展示x，y轴标签
plt.xlabel('Annual Income (k$)')
plt.ylabel('Spending Score (1-100)')
plt.show()
#由散点图可知：消费群体大部分集中在消费分数40-60、平均工资40-60之间。


# In[ ]:




