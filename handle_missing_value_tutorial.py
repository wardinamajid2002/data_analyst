import pandas as pd
import numpy as np

# read  data
read_data = pd.read_csv("Building_Permits.csv")
print(f'-----Data is being read-----')


#  reproducibility
np.random.seed(0) 

first_five = read_data.head()
# print(first_five)

missing_value = read_data.isnull().sum()

print(missing_value)


total_cells = np.prod(read_data.shape)
total_missing = missing_value.sum()

print(f'Calculating percent of missing......%')
percent_missing = (total_missing/total_cells) * 100
print(f"{percent_missing:.2f}%")

print(missing_value[0:10])


#remove missing value
# read_data.dropna()



