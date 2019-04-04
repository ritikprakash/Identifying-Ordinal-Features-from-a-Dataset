
# coding: utf-8

# <div style="display:block">
#     <div style="width: 20%; display: inline-block; text-align: left;">
#         <div class="crop">
#             <img src="https://media.licdn.com/dms/image/C510BAQHYx68wy1dIng/company-logo_400_400/0?e=1551916800&v=beta&t=ZPw68MeIuGLt9obXpIsiWiB1QcyaniHjGk9doyJulys" style="height:75px; margin-left:0px" />
#         </div>
#     </div>
#     <div style="width: 59%; display: inline-block">
#         <h1  style="text-align: center">Identify_Ordinal_Features</h1><br>
#         <div style="width: 90%; text-align: center; display: inline-block;"><i>Author:</i> <strong>NetworthCorp</strong> </div>
#     </div>
#     <div style="width: 20%; text-align: right; display: inline-block;">
#         <div style="width: 100%; text-align: left; display: inline-block;">
#             <i>Created: </i>
#             <time datetime="Enter Date" pubdate>December, 2018</time>
#         </div>
#     </div>
# </div>

# ## || Functionality:
# __This Module enables user to Identify Ordinal Features in a Dataframe.__<br>
# It plots a Bar Graph of all the Categorical Features and Save in a PNG Format to your Directory. 

# ## || Input Parameters:
# * __source:__ It takes the Path or Name of the File..
# * __comp_col:__ The column name from which the data will be compared.

# ## || Return:
# __It returns the name of the Ordinal Columns in a Dataframe and Bar plot of all the Categorical Columns in a 'PNG' format.__

# ## || Code:

# In[192]:


import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
from scipy import stats

def ordinal_var(source=None,comp_col=None):
    
    data=pd.read_csv(source)
    anova=pd.DataFrame(columns = ['Name','F_Value','P_Value'])
    i=0
    leng=len(data.select_dtypes(include=[np.object]).columns)
    x=math.ceil(math.sqrt(leng))
    plt.figure(figsize=(15, 15))
    for col in (data.select_dtypes(include=[np.object])): 
        i=i+1
        plt.subplot(x, x, i)
        plt.tight_layout()
        data.groupby([col])[comp_col].mean().sort_values(ascending=True).plot(kind='bar')

    plt.savefig('ordinal_var.png')
    
    for col in (data.select_dtypes(include=[np.object])):
        samples = (condition[1] for condition in data.groupby([col])[comp_col])
        f_val, p_val = stats.f_oneway(*samples)
        anova=anova.append({'Name': col,'F_Value':f_val,'P_Value':round(p_val,3) },ignore_index=True)
    
    ordinal=anova[anova['P_Value']<0.05]
    ordinal = ordinal.reset_index(drop=True)
    ordinal=ordinal['Name']
    return(ordinal)
        
    


# ## || Test 1:

# In[191]:


ordinal_var('home_pred_train.csv','SalePrice')


# ## || Test 2:

# * __Note:__ Use Treated Datasets.<br>
# <br>
# This Dataset was Raw and contains NaN Values, So the output is not appropirate.

# In[193]:


dta=pd.read_csv('startup_funding.csv', sep=',', thousands=',')
dta['AmountInUSD']=dta['AmountInUSD'].fillna(0)

ordinal_var(dta,'AmountInUSD')

