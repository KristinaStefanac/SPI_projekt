#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import pandas as pd


# In[ ]:


#country_df


# In[ ]:


country_df = pd.read_csv('C:\\Users\\Kristina\\Tables2\\Country.csv')
country_df = country_df.drop_duplicates()
country_df = country_df.reset_index(drop=True)


# In[ ]:


country_df


# In[ ]:


#customer_df


# In[ ]:


customer_df = pd.read_csv('C:\\Users\\Kristina\\Desktop\\SPI\\customer.csv')
customer_df = customer_df.drop_duplicates()


# In[ ]:


customer_df


# In[ ]:


#DIMNEZIJSKA TABLICA CUSTOMER


# In[ ]:


dim_customer_df = pd.merge(customer_df, country_df, left_on="state_id", right_index=True, how="left")
dim_customer_df['dim_customer_id'] = dim_customer_df.index 
dim_customer_df['date_from'] = pd.Timestamp.today().date() 
dim_customer_df['date_to'] = pd.NaT

dim_customer_df


# In[ ]:


#product_subcategory_df


# In[ ]:


product_subcategory_df = pd.read_csv('C:\\Users\\Kristina\\Desktop\\SPI\\product_subcategory.csv')
product_subcategory_df = product_subcategory_df.drop_duplicates()
product_subcategory_df


# In[ ]:


#poduct_df


# In[ ]:


product_df = pd.read_csv('C:\\Users\\Kristina\\Desktop\\SPI\\product.csv')
customer_df = customer_df.drop_duplicates()
product_df


# In[ ]:


#DIMENZIJSKA TABLICA PRODUCT


# In[ ]:


merged_df = pd.merge(product_df, product_subcategory_df, left_on='product_subcategory_id', right_index=True, how='left')
dim_product_df = merged_df.copy()
dim_product_df['dim_product_id'] = dim_product_df.index 
dim_product_df['date_from'] = pd.Timestamp.today().date()  
dim_product_df['date_to'] = pd.NaT
dim_product_df = dim_product_df.drop_duplicates()

print(dim_product_df)
dim_product_df


# In[ ]:


#DIMNEZIJSKA TABLICA DATE


# In[ ]:


data = pd.read_csv('C:\\Users\\Kristina\\Desktop\\SPI\\Sales.csv')
dim_time_df = pd.DataFrame()
dim_time_df['date'] = pd.to_datetime(data['Date'])
dim_time_df['date_id'] = dim_time_df.index 
dim_time_df['day'] = data['Day']
dim_time_df['month'] = data['Month']
dim_time_df['year'] = data['Year']
dim_time_df['day_of_week'] = dim_time_df['date'].dt.day_name()
dim_time_df['month_name'] = dim_time_df['date'].dt.month_name()
dim_time_df['quarter'] = dim_time_df['date'].dt.quarter
dim_time_df = dim_time_df.drop_duplicates()

dim_time_df


# In[ ]:


#orders_df


# In[ ]:


orders_df = pd.read_csv('C:\\Users\\Kristina\\Desktop\\SPI\\orders.csv')
orders_df = orders_df.drop_duplicates()
orders_df
print("cao cao")


# In[ ]:


#Tablica činjenica Orders

