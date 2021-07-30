import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

#tips=pd.read_csv("tips.csv")
tips=sns.load_dataset("tips")
sns.barplot(x='day',y='tip',data=tips)
