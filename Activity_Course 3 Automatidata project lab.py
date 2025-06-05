# Import packages and libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import datetime as dt
import seaborn as sns


# **Note:** As shown in this cell, the dataset has been automatically loaded in for you. You do not need to download the .csv file, or provide more code, in order to access the dataset and proceed with this lab. Please continue with this activity by completing the following instructions.

# In[2]:


# Load dataset into dataframe
df = pd.read_csv('2017_Yellow_Taxi_Trip_Data.csv')


# <img src="images/Analyze.png" width="100" height="100" align=left>
# 
# ## PACE: Analyze 
# 
# Consider the questions in your PACE Strategy Document to reflect on the Analyze stage.

# ### Task 2a. Data exploration and cleaning
# 
# Decide which columns are applicable
# 
# The first step is to assess your data. Check the Data Source page on Tableau Public to get a sense of the size, shape and makeup of the data set. Then answer these questions to yourself: 
# 
# Given our scenario, which data columns are most applicable? 
# Which data columns can I eliminate, knowing they won’t solve our problem scenario? 
# 
# Consider functions that help you understand and structure the data. 
# 
# *    head()
# *    describe()
# *    info()
# *    groupby()
# *    sortby()
# 
# What do you do about missing data (if any)? 
# 
# Are there data outliers? What are they and how might you handle them? 
# 
# What do the distributions of your variables tell you about the question you're asking or the problem you're trying to solve?
# 
# 
# 

# ==> ENTER YOUR RESPONSE HERE

# Start by discovering, using head and size. 

# In[3]:


df.head(10)


# In[6]:


df.size


# Use describe... 

# In[7]:


df.describe()


# And info. 

# In[10]:


df.info()


# ### Task 2b. Assess whether dimensions and measures are correct

# On the data source page in Tableau, double check the data types for the applicable columns you selected on the previous step. Pay close attention to the dimensions and measures to assure they are correct. 
# 
# In Python, consider the data types of the columns. *Consider:* Do they make sense? 

# Review the link provided in the previous activity instructions to create the required Tableau visualization. 

# ### Task 2c. Select visualization type(s)

# Select data visualization types that will help you understand and explain the data.
# 
# Now that you know which data columns you’ll use, it is time to decide which data visualization makes the most sense for EDA of the TLC dataset. What type of data visualization(s) would be most helpful? 
# 
# * Line graph
# * Bar chart
# * Box plot
# * Histogram
# * Heat map
# * Scatter plot
# * A geographic map

# <img src="images/Construct.png" width="100" height="100" align=left>
# 
# ## PACE: Construct 
# 
# Consider the questions in your PACE Strategy Document to reflect on the Construct stage.

# ### Task 3. Data visualization
# 
# You’ve assessed your data, and decided on which data variables are most applicable. It’s time to plot your visualization(s)!
# 

# ### Boxplots

# Perform a check for outliers on relevant columns such as trip distance and trip duration. Remember, some of the best ways to identify the presence of outliers in data are box plots and histograms. 
# 
# **Note:** Remember to convert your date columns to datetime in order to derive total trip duration.  

# In[25]:


# Convert data columns to datetime
cols_to_convert=['tpep_pickup_datetime','tpep_dropoff_datetime']
df[cols_to_convert]=df[cols_to_convert].apply(pd.to_datetime)


# **trip distance**

# In[13]:


# Create box plot of trip_distance
plt.figure(figsize=(7,2))
plt.title("Trip Distance Boxplot")
sns.boxplot(x=df['trip_distance'],fliersize=1)


# In[17]:


# Create histogram of trip_distance
plt.figure(figsize=(10,5))
plt.title("Trip Distance Histogram")
sns.histplot(df['trip_distance'],bins=range(0,26,1))


# **total amount**

# In[14]:


# Create box plot of total_amount
plt.figure(figsize=(8,3))
plt.title("Total Amount Boxplot")
sns.boxplot(x=df['total_amount'],fliersize=6)


# In[21]:


# Create histogram of total_amount
plt.figure(figsize=(10,5))
plt.title("Total Amount Histogram")
sns.histplot(df['total_amount'],bins=range(0,400,10))


# **tip amount**

# In[16]:


# Create box plot of tip_amount
plt.figure(figsize=(7,2))
plt.title("Tip Amount Boxplot")
sns.boxplot(x=df['tip_amount'],fliersize=5)


# In[23]:


# Create histogram of tip_amount
plt.figure(figsize=(8,4))
plt.title("Tip Amount Histogram")
sns.histplot(df['tip_amount'],bins=range(0,25,1))


# **tip_amount by vendor**

# In[3]:


# Create histogram of tip_amount by vendor
plt.figure(figsize=(12,7))
ax=sns.histplot(data=df,x='tip_amount',bins=range(0,21,1),hue='VendorID',multiple='stack',palette='pastel')
ax.set_xticks(range(0,21,1))
ax.set_xticklabels(range(0,21,1))
plt.title("Tip Amount by Vendor")


# Next, zoom in on the upper end of the range of tips to check whether vendor one gets noticeably more of the most generous tips.

# In[7]:


# Create histogram of tip_amount by vendor for tips > $10 
tip_data=df[df['tip_amount']>10]
plt.figure(figsize=(12,7))
ax=sns.histplot(data=tip_data,x='tip_amount',bins=range(10,21,1),hue='VendorID',multiple='stack',palette='pastel')
ax.set_xticks(range(10,21,1))
ax.set_xticklabels(range(10,21,1))
plt.title("Tip Amount by Vendor")


# **Mean tips by passenger count**
# 
# Examine the unique values in the `passenger_count` column.

# In[8]:


df['passenger_count'].value_counts()


# In[17]:


# Calculate mean tips by passenger_count
mean_tip_by_passenger_count=df.groupby(['passenger_count']).mean()[['tip_amount']]
mean_tip_by_passenger_count


# In[18]:


# Create bar plot for mean tips by passenger count
data = mean_tip_by_passenger_count.tail(-1)
pal = sns.color_palette("Greens_d", len(data))
rank = data['tip_amount'].argsort().argsort()
plt.figure(figsize=(12,7))
ax = sns.barplot(x=data.index,
            y=data['tip_amount'],
            palette=np.array(pal[::-1])[rank])
ax.axhline(df['tip_amount'].mean(), ls='--', color='red', label='global mean')
ax.legend()
plt.title('Mean tip amount by passenger count', fontsize=16);


# **Create month and day columns**

# In[26]:


# Create a month column
df['month']=df['tpep_pickup_datetime'].dt.month_name()

# Create a day column
df['day']=df['tpep_pickup_datetime'].dt.day_name()
df.head(10)


# **Plot total ride count by month**
# 
# Begin by calculating total ride count by month.

# In[33]:


# Get total number of rides for each month
monthly_rides=df['month'].value_counts()


# Reorder the results to put the months in calendar order.

# In[34]:


# Reorder the monthly ride list so months go in order
month_order = ['January', 'February', 'March', 'April', 'May', 'June', 'July',
         'August', 'September', 'October', 'November', 'December']

monthly_rides = monthly_rides.reindex(index=month_order)
monthly_rides


# In[35]:


# Show the index
monthly_rides.index


# In[36]:


# Create a bar plot of total rides per month
plt.figure(figsize=(12,7))
ax = sns.barplot(x=monthly_rides.index, y=monthly_rides)
ax.set_xticklabels(month_order)
plt.title('Ride count by month', fontsize=16);


# **Plot total ride count by day**
# 
# Repeat the above process, but now calculate the total rides by day of the week.

# In[40]:


# Repeat the above process, this time for rides by day
daily_rides=df['day'].value_counts()
day_order=['Sunday','Monday','Tuesday','Wednesday','Thursday','Friday','Saturday']
daily_rides=daily_rides.reindex(index=day_order)
daily_rides


# In[41]:


# Create bar plot for ride count by day
plt.figure(figsize=(12,7))
ax = sns.barplot(x=daily_rides.index, y=daily_rides)
plt.title('Ride count by day', fontsize=16);


# **Plot total revenue by day of the week**
# 
# Repeat the above process, but now calculate the total revenue by day of the week.

# In[52]:


# Repeat the process, this time for total revenue by day
total_amount_day=df.groupby('day').sum()[['total_amount']]
total_amount_day=total_amount_day.reindex(index=day_order)


# In[53]:


# Create bar plot of total revenue by day
plt.figure(figsize=(12,7))
ax = sns.barplot(x=total_amount_day.index, y=total_amount_day['total_amount'])
ax.set_ylabel('Revenue (USD)')
plt.title('Total revenue by day', fontsize=16);


# **Plot total revenue by month**

# In[54]:


# Repeat the process, this time for total revenue by month
total_amount_month = df.groupby('month').sum()[['total_amount']]
total_amount_month = total_amount_month.reindex(index=month_order)
total_amount_month


# In[55]:


# Create a bar plot of total revenue by month
plt.figure(figsize=(12,7))
ax = sns.barplot(x=total_amount_month.index, y=total_amount_month['total_amount'])
plt.title('Total revenue by month', fontsize=16);


# #### Scatter plot

# You can create a scatterplot in Tableau Public, which can be easier to manipulate and present. If you'd like step by step instructions, you can review the following link. Those instructions create a scatterplot showing the relationship between total_amount and trip_distance. Consider adding the Tableau visualization to your executive summary, and adding key insights from your findings on those two variables.

# [Tableau visualization guidelines](https://docs.google.com/document/d/1pcfUlttD2Y_a9A4VrKPzikZWCAfFLsBAhuKuomjcUjA/template/preview)

# **Plot mean trip distance by drop-off location**

# In[56]:


# Get number of unique drop-off location IDs
df['DOLocationID'].nunique()


# In[57]:


# Calculate the mean trip distance for each drop-off location
distance_by_dropoff = df.groupby('DOLocationID').mean()[['trip_distance']]

# Sort the results in descending order by mean trip distance
distance_by_dropoff = distance_by_dropoff.sort_values(by='trip_distance')
distance_by_dropoff 


# In[58]:


# Create a bar plot of mean trip distances by drop-off location in ascending order by distance
plt.figure(figsize=(14,6))
ax = sns.barplot(x=distance_by_dropoff.index, 
                 y=distance_by_dropoff['trip_distance'],
                 order=distance_by_dropoff.index)
ax.set_xticklabels([])
ax.set_xticks([])
plt.title('Mean trip distance by drop-off location', fontsize=16);
