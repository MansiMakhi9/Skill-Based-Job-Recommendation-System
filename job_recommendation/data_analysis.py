import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib as map
import matplotlib.pyplot as plt

######kaggle dataset : - https://www.kaggle.com/datasets/tondji/jobs-data-for-recommender-systems?resource=download
#To ignore warnings.
import warnings
warnings.filterwarnings('ignore')

#saving model
#from sklearn.externals import joblib

##################Loading the Dataset

df_all_offers = pd.read_csv('ALL_Offers.csv')
     

df_offers = pd.read_csv('offers.csv')
     

df_org = pd.read_csv('organizations.csv')
     
############Exploratory Data Analysis
###############Data Analysis of All_offers.csv

#Let's understand the data
print(df_all_offers.head())



#Number of Rows in the dataset
print("Number of Rows are:",df_all_offers.shape[0])
     

#Number of Columns/features in dataset
print("Number of Columns are:",df_all_offers.shape[1])
     

#List of Available features in dataset
print("Available Features are:",df_all_offers.columns.tolist())

# Let's checkout which feature contains which kind of values i.e int /float /etc or what is the data type of values.
print(df_all_offers.info())
     


#Checking is their any missing values are available in the dataset

print("Missing values:\n ",df_all_offers.isnull().sum())


# check for duplicate values
a = df_all_offers.duplicated().sum()

print(a)    
#checing number of unique values available in each column
print(df_all_offers.nunique())

#########Data Analysis of offers.csv


#Let's understand the data
print(df_offers.head())

#Number of Rows in the dataset
print("Number of Rows are:",df_offers.shape[0])
     

#Number of Columns/features in dataset
print("Number of Columns are:",df_offers.shape[1])
     

#List of Available features in dataset
print("Available Features are:",df_offers.columns.tolist())
     

# Let's checkout which feature contains which kind of values i.e int /float /etc or what is the data type of values.
print(df_offers.info())
#Checking is their any missing values are available in the dataset

print("Missing values:\n ",df_offers.isnull().sum())


# check for duplicate values
print(df_offers.duplicated().sum())
     


#checing number of unique values available in each column
print(df_offers.nunique())

################Data Analysis of Users.csv


#Let's understand the data
print(df_org.head())


#Number of Rows in the dataset
print("Number of Rows are:",df_org.shape[0])
     

#Number of Columns/features in dataset
print("Number of Columns are:",df_org.shape[1])
     

#List of Available features in dataset
print("Available Features are:",df_org.columns.tolist())
     

# Let's checkout which feature contains which kind of values i.e int /float /etc or what is the data type of values.
print(df_offers.info())
#Checking is their any missing values are available in the dataset

print("Missing values:\n ",df_org.isnull().sum())
     

# check for duplicate values
print(df_org.duplicated().sum())
     


#checing number of unique values available in each column
print(df_org.nunique())

################Combining the Datasets


#Combining the dataset Offers.csv and Org.csv
df_combined1=pd.merge(df_offers,df_org)
print(df_combined1.head())
     
#Number of Rows in the dataset
print("Number of Rows are:",df_combined1.shape[0])
#Number of Columns/features in dataset
print("Number of Columns are:",df_combined1.shape[1])


#Combining the Datasets All_offers.csv and Org.csv
df_combined1['contracts'].unique()
     

jobs = df_combined1['job_title'].unique()
print(jobs)
len(jobs)
     


newdf = df_combined1[['user_id', 'job_title','skills']]
print(newdf)

skillss = []
for j in jobs:
  skillss.append(newdf.loc[newdf['job_title'] == j]['skills'])
print(skillss)
     

skillss[0]
     
     


     






