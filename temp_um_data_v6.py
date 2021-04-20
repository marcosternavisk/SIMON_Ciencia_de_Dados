#!/usr/bin/env python
# coding: utf-8

# In[32]:


import os, json


# In[33]:


import matplotlib.pyplot as plt


# In[34]:


import numpy as np


# In[35]:


import time


# In[36]:


diretorio_json = 'reg/'


# In[37]:


temperatura = []


# In[38]:


umidade = []


# In[39]:


data =[]


# In[ ]:


for file_name in [file for file in os.listdir(diretorio_json) if file.endswith('.json')]:
    with open(diretorio_json + file_name) as json_file:
        data = json.load(json_file)
        temperatura = list(data.values())[0]
        temp_arr_numpy = np.array(temperatura)
        umidade = list(data.values())[1]
        umidade_arr_numpy = np.array(umidade)
        data = list(data.values())[2]
        data_formatada = time.strftime('%d-%m-%y %H:%M:%S', time.localtime(data))
        #data_arr_numpy = np.array(data)
        #data_formatada_arr_numpy = np.array(data_formatada)
        #print(data_formatada_arr_numpy)
        #print(temp_arr_numpy)
        #print(umidade_arr_numpy)
        #print(data_formatada)
        #print(temperatura)
        
        #x = np.linspace(0, 2, num = 100)
        
        plt.plot([data], [temperatura])
        plt.xlabel('Data')
        plt.ylabel('Temperatura')
        plt.show()
        
        


# In[35]:


plt.plot(data_formatada_arr_numpy, temp_arr_numpy)
        
plt.xlabel('Data')
plt.ylabel('Temperatura')
        
plt.show

