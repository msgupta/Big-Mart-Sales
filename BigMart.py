# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import pandas as pd
import numpy as np

#Read files
train = pd.read_csv("Train.csv")
test = pd.read_csv("Test.csv")

train['Source'] = 'train'
test['Source'] = 'test'

data = pd.concat([train, test], ignore_index = True)

sum(data.Outlet_Size.isnull())

data.apply(lambda x: sum(x.isnull()))
train.apply(lambda x: sum(x.isnull()))
data.describe()

#Item_Weight, Outlet_Size
len(data.Item_Identifier.unique())
data.apply(lambda x: len(x.unique()))
# 1559 Items, 16 Item types, 10 Outlets, 4 Outlet types

#Filter categorical variables

data.dtypes
categorical_columns = [x for x in data.dtypes.index if data.dtypes[x] == 'object']

#Exclude ID cols and source

categorical_columns = [x for x in categorical_columns if x not in ['Item_Identifier', 'Outlet_Identifier', 'Source']]

for col in categorical_columns:
    print '\nFrequency of categories for variable %s'%col
    print data[col].value_counts()

## Data Cleaning ##

item_avg_weight = data.pivot_table(values=["Item_Weight"], index=["Item_Identifier"])
miss_bool = data['Item_Weight'].isnull()

data.loc[miss_bool,'Item_Weight']
data.loc[miss_bool,'Item_Identifier']

data.loc[miss_bool,'Item_Weight'] = data.loc[miss_bool,'Item_Identifier'].apply(lambda x: item_avg_weight[x])










