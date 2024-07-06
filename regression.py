# linear regression with python
# https://docs.google.com/spreadsheets/d/e/2PACX-1vQBtIFVKd7xxiax0qAjADYy5yMlHntbdF_pxRj67Qjbgl9a44qhw0AQ14_Eu8vAxiwHv7p9q8KAvp0B/pub?gid=1272501787&single=true&output=csv

# Importing the libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Importing the dataset
dataset = pd.read_csv('https://docs.google.com/spreadsheets/d/e/2PACX-1vQBtIFVKd7xxiax0qAjADYy5yMlHntbdF_pxRj67Qjbgl9a44qhw0AQ14_Eu8vAxiwHv7p9q8KAvp0B/pub?gid=1272501787&single=true&output=csv')

# Data Preprocessing
X = dataset.iloc[:, :-1].values
y = dataset.iloc[:, -1].values

# Splitting the dataset into the Training set and Test set
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = 0)

# Training the Simple Linear Regression model on the Training set
from sklearn.linear_model import LinearRegression
regressor = LinearRegression()
regressor.fit(X_train, y_train)

# Predicting the Test set results
y_pred = regressor.predict(X_test)

# Visualising the Training set results
plt.scatter(X_train, y_train, color = 'red')
plt.plot(X_train, regressor.predict(X_train), color = 'blue')
plt.title('Price vs Size (Training set)')
plt.xlabel('Size')
plt.ylabel('Price')
plt.show()

# Visualising the Test set results
plt.scatter(X_test, y_test, color = 'red')
plt.plot(X_train, regressor.predict(X_train), color = 'blue')
plt.title('Price vs Size (Test set)')
plt.xlabel('Size')
plt.ylabel('Price')
plt.show()

# Predicting the price of a house with size 750
print(regressor.predict([[2000]]))



