#!/usr/bin/env python
# coding: utf-8

# In[12]:


import pandas as pd
import numpy as np
import sys
from datetime import timedelta, datetime, date
import csv
import argparse


# In[13]:


parser = argparse.ArgumentParser()
parser.add_argument('--min-date', type=str, default='2021-01-08', help='Start of the date range')
parser.add_argument('--max-date', type=str, default='2021-05-30', help='End of the date range')
args = parser.parse_args()


print("Minimum Date:", args.min_date)
print("Maximum Date:", args.max_date)


# In[3]:


# Load data from CSV files
brands = pd.read_csv(r"C:\Users\melih\Desktop\brand.csv")
products = pd.read_csv(r"C:\Users\melih\Desktop\product.csv")
stores = pd.read_csv(r"C:\Users\melih\Desktop\store.csv")
sales = pd.read_csv(r"C:\Users\melih\Desktop\sales.csv")


# In[4]:


data = sales.merge(products, left_on="product", right_on="id")
data = data.merge(stores, left_on="store", right_on="id")


# In[5]:


# Convert "brand" column in data to string
data["brand"] = data["brand"].astype(str)


# In[6]:


# Merge data with the brands dataframe using the 'brand' column
data = data.merge(brands, left_on="brand", right_on="name")


# In[7]:


# Convert 'date' column to datetime format
data["date"] = pd.to_datetime(data["date"])


# In[8]:


# Filter data based on date range
filtered_data = data[(data["date"] >= args.min_date) & (data["date"] <= args.max_date)]


# In[9]:


grouped = filtered_data.groupby(["product", "store", "brand", "date"]).agg({"quantity": "sum"}).reset_index()
grouped.rename(columns={"quantity": "sales_product"}, inplace=True)

grouped["MA7_P"] = grouped.groupby("product")["sales_product"].transform(lambda x: x.rolling(window=7, min_periods=1).mean())
grouped["LAG7_P"] = grouped.groupby("product")["sales_product"].shift(7)

grouped["sales_brand"] = grouped.groupby(["brand", "store", "date"])["sales_product"].transform("sum")
grouped["MA7_B"] = grouped.groupby("brand")["sales_brand"].transform(lambda x: x.rolling(window=7, min_periods=1).mean())
grouped["LAG7_B"] = grouped.groupby("brand")["sales_brand"].shift(7)

grouped["sales_store"] = grouped.groupby(["store", "date"])["sales_product"].transform("sum")
grouped["MA7_S"] = grouped.groupby("store")["sales_store"].transform(lambda x: x.rolling(window=7, min_periods=1).mean())
grouped["LAG7_S"] = grouped.groupby("store")["sales_store"].shift(7)


# In[10]:


# Sort the dataframe as specified
result = grouped.sort_values(by=["product", "brand", "store", "date"])


# In[11]:


result.to_csv("features.csv", index=False)


# In[ ]:




