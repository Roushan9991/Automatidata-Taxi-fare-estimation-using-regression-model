
import pandas as pd
import numpy as np

# Load dataset into dataframe
df = pd.read_csv('2017_Yellow_Taxi_Trip_Data.csv')
print("done")


# ### **Task 2b. Understand the data - Inspect the data**
# 
# View and inspect summary information about the dataframe by coding the following:
# 
# 1. `df.head(10)`
# 2. `df.info()`
# 3. `df.describe()`
# 
# Consider the following two questions:
# 
# **Question 1:** When reviewing the `df.info()` output, what do you notice about the different variables? Are there any null values? Are all of the variables numeric? Does anything else stand out?
# 
# **Question 2:** When reviewing the `df.describe()` output, what do you notice about the distributions of each variable? Are there any questionable values?

# **Answer 1:** There are no null values in the output and all the variables are numeric, date is picking up as object rather than datetime. Memory is used 3.1 MB. There is no proper naming given to the first column, not sure what that is representing.
# 
# **Answer 2:** Minimum is coming negative for the fare amount which ideally should not, need to check this.

# In[4]:


df.head(10)


# In[2]:


df.info()


# In[7]:


df.describe()


# ### **Task 2c. Understand the data - Investigate the variables**
# 
# Sort and interpret the data table for two variables:`trip_distance` and `total_amount`.
# 
# **Answer the following three questions:**
# 
# **Question 1:** Sort your first variable (`trip_distance`) from maximum to minimum value, do the values seem normal?
# 
# **Question 2:** Sort by your second variable (`total_amount`), are any values unusual?
# 
# **Question 3:** Are the resulting rows similar for both sorts? Why or why not?

# **Answer:** Total amount based on the trip distance is not normal, There are instances when the total_amount is less for the long trip than some short trip. This is probably due to other factors like tip amount, toll amount and improvement surcharge.

# In[4]:


df_sorted=df.sort_values(by='trip_distance', ascending=False)
df_sorted[['trip_distance','total_amount']].head(20)

# Sort the data by trip distance from maximum to minimum value


# In[5]:


df_sorted=df.sort_values(by='total_amount', ascending=False)
df_sorted[['trip_distance','total_amount']].head(20)

# Sort the data by total amount and print the top 20 values


# In[6]:


df_sorted[['trip_distance','total_amount']].tail(20)

# Sort the data by total amount and print the bottom 20 values


# In[7]:


df['payment_type'].unique()

# How many of each payment type are represented in the data?


# According to the data dictionary, the payment method was encoded as follows:
# 
# 1 = Credit card  
# 2 = Cash  
# 3 = No charge  
# 4 = Dispute  
# 5 = Unknown  
# 6 = Voided trip

# In[7]:


df.groupby('payment_type')['tip_amount'].mean()

# What is the average tip for trips paid for with credit card?



# What is the average tip for trips paid for with cash?


# In[5]:


df.groupby('VendorID')['VendorID'].size()

# How many times is each vendor ID represented in the data?


# In[8]:


df.groupby('VendorID')['total_amount'].mean()

# What is the mean total amount for each vendor?


# In[4]:


df[df['payment_type']==1]

# Filter the data for credit card payments only

df[df['payment_type']==1].groupby('passenger_count').count()

# Filter the credit-card-only data for passenger count only


# In[11]:


df[df['payment_type']==1].groupby('passenger_count')['tip_amount'].mean()

