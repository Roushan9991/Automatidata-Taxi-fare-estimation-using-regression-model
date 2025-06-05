import pandas as pd
from scipy import stats


# **Note:** As shown in this cell, the dataset has been automatically loaded in for you. You do not need to download the .csv file, or provide more code, in order to access the dataset and proceed with this lab. Please continue with this activity by completing the following instructions.

# In[3]:


taxi_data = pd.read_csv("2017_Yellow_Taxi_Trip_Data.csv", index_col = 0)


# <img src="images/Analyze.png" width="100" height="100" align=left>
# 
# <img src="images/Construct.png" width="100" height="100" align=left>
# 
# ## PACE: **Analyze and Construct**
# 
# In this stage, consider the following questions where applicable to complete your code response:
# 1. Data professionals use descriptive statistics for Exploratory Data Analysis. How can computing descriptive statistics help you learn more about your data in this stage of your analysis?
# 

# **Exemplar response:** In general, descriptive statistics are useful because they let you quickly explore and understand large amounts of data. In this case, computing descriptive statistics helps you quickly compare the average total fare amount among different payment types.
# 

# ### Task 2. Data exploration
# 
# Use descriptive statistics to conduct Exploratory Data Analysis (EDA).

# <details>
#   <summary><h4><strong>Hint: </strong></h4></summary>
# 
# Refer back to *Self Review Descriptive Statistics* for this step-by-step proccess.
# 
# </details>

# **Note:** In the dataset, `payment_type` is encoded in integers:
# *   1: Credit card
# *   2: Cash
# *   3: No charge
# *   4: Dispute
# *   5: Unknown
# 
# 

# In[4]:


# descriptive stats code for EDA
taxi_data.describe(include='all')


# You are interested in the relationship between payment type and the fare amount the customer pays. One approach is to look at the average fare amount for each payment type. 

# In[7]:


taxi_data.groupby('payment_type')['fare_amount'].mean()


# Based on the averages shown, it appears that customers who pay in credit card tend to pay a larger fare amount than customers who pay in cash. However, this difference might arise from random sampling, rather than being a true difference in fare amount. To assess whether the difference is statistically significant, you conduct a hypothesis test.

# 
# ### Task 3. Hypothesis testing
# 
# Before you conduct your hypothesis test, consider the following questions where applicable to complete your code response:
# 
# 1. Recall the difference between the null hypothesis and the alternative hypotheses. What are your hypotheses for this data project?

# **response:** 
# **Null hypothesis**: There is no difference in average fare between customers who use credit cards and customers who use cash. 
# **Alternative hypothesis**: There is a difference in average fare between customers who use credit cards and customers who use cash

# 
# 
# Your goal in this step is to conduct a two-sample t-test. Recall the steps for conducting a hypothesis test: 
# 
# 
# 1.   State the null hypothesis and the alternative hypothesis
# 2.   Choose a signficance level
# 3.   Find the p-value
# 4.   Reject or fail to reject the null hypothesis 
# 
# 

# **Note:** For the purpose of this exercise, your hypothesis test is the main component of your A/B test. 

# $H_0$: There is no difference in the average fare amount between customers who use credit cards and customers who use cash.
# 
# $H_A$: There is a difference in the average fare amount between customers who use credit cards and customers who use cash.

# You choose 5% as the significance level and proceed with a two-sample t-test.

# In[8]:


#hypothesis test, A/B test
#significance level

credit_card = taxi_data[taxi_data['payment_type'] == 1]['fare_amount']
cash = taxi_data[taxi_data['payment_type'] == 2]['fare_amount']
stats.ttest_ind(a=credit_card, b=cash, equal_var=False)


# **response:** Since the p-value is significantly smaller than the significance level of 5%, you reject the null hypothesis. 
# 
# *Notice the 'e-12' at the end of the pvalue result.*
# 
# We conclude that there is a statistically significant difference in the average fare amount between customers who use credit cards and customers who use cash.

