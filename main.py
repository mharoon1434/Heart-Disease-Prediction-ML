# import the packages
# data manipulation package
import numpy as np
import pandas as pd 


# data visualization packages 
import matplotlib.pyplot as plt 
import  seaborn as sns 

# model related package 
# logistic regression model
from sklearn.tree import DecisionTreeRegressor 
from sklearn.model_selection import train_test_split 
from sklearn.preprocessing import StandardScaler 
from sklearn.metrics import accuracy_score, precision_score, recall_score, confusion_matrix

# load data
data = pd.read_csv("heart.csv")

# remove outlier
# remove the outliers from the column
def remove_outliers(data , columns):
    for column in columns:
        if column in data.columns:
            Q1 = data[column].quantile(0.25)
            Q3 = data[column].quantile(0.75)
            IQR = Q3 - Q1
            lower_bound = Q1 - 1.5 * IQR 
            upper_bound = Q3 + 1.5 * IQR
            data = data[(data[column] >= lower_bound) & (data[column] <= upper_bound)]
    return data 
data = remove_outliers(data, data.columns)


# create the x and y variable 
X = data.drop(columns="target")
y = data['target']

# split the data into training and testing 
X_train, X_test, y_train, y_test =train_test_split(X , y ,test_size=0.2, random_state=100)

# standardization or scalling of the data 
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)


# model creation and training 
dt_reg = DecisionTreeRegressor()
dt_reg.fit(X_train_scaled, y_train)

# testing of the model
y_pred = dt_reg.predict(X_test_scaled)

# accuracy of the model
print(accuracy_score(y_test, y_pred))