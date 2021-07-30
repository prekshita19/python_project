import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# For Linux
train=pd.read_csv("/home/emirates/Dropbox/Tops/Project/Project - Churn Reduction/Train_data.csv")
test=pd.read_csv("/home/emirates/Dropbox/Tops/Project/Project - Churn Reduction/Test_data.csv")

# For Windows
# train=pd.read_csv("C:/Users/Fly-Emirates/Dropbox/Tops/Project/Project - Churn Reduction/Train_data.csv")
# test=pd.read_csv("C:/Users/Fly-Emirates/Dropbox/Tops/Project/Project - Churn Reduction/Test_data.csv")

# using is_null().sum() to check the number of values that are null
# train_null=train.isnull().sum()
# test_null=test.isnull().sum()

del train["phone number"]     # Not of use
del test["phone number"]      # Not of use

column_type=train.columns[(train.dtypes=="float64")].tolist()

categories_name=train.select_dtypes(exclude=np.number).columns.tolist()
del categories_name[3]

def num(df):
    for i in range(0,df.shape[1]):                             # For train data  
        if(df.iloc[:,i].dtypes == "object"):
            df.iloc[:,i]=pd.Categorical(df.iloc[:,i])       # Making the data Categorical.
            df.iloc[:,i]=df.iloc[:,i].cat.codes             # concating the data.
            df.iloc[:,i]=df.iloc[:,i].astype("object")      # converting the type of columns.
    return df

train=num(train)
test=num(test)

