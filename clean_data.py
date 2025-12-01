#clean dataset (no missing value,standard format,
# no duplicates, correct data type,valid data)
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np


data_file = pd.read_csv('/mnt/c/Users/User/Desktop/chrome_history.csv')
print(data_file.shape)

#check for missing value
print(data_file.isnull().sum())

# url                                    0
# url_clean                              0
# url_domain                            13
# title                                  8
# time                                   0

#clean the missing value of url_domain by dropping the row
data_file = data_file.dropna(subset=['url_domain'])

data_file = data_file.dropna(subset=['title'])



data_file.head()

#drop column that i dont want to use
data_file = data_file.drop(['hour','day_of_week','is_weekend','week_of_month'], axis = 1)

#after drop unwanted column,save new csv,now we work in the cleaned one
#data_file.to_csv('/mnt/c/Users/User/Desktop/chrome_history_cleaned_1.csv', index=False)
#data_file = pd.read_csv('/mnt/c/Users/User/Desktop/chrome_history_cleaned_1.csv')



                    #----after the data is cleaned----#



#1. clean anything browse/related to chatgpt
data_file = data_file[~data_file['url'].str.contains('chatgpt|openai', case=False, na=False)]

#2.time must be in format (month/year) 

# data_file['time'] = pd.to_datetime(data_file['time'])
# data_file['month_year'] = data_file['time'].dt.to_period('M').astype(str)



#3.how many time i spend on instagram



data_file.to_csv('/mnt/c/Users/User/Desktop/chrome_history_cleaned.csv', index=False)