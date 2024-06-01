# python for data science - sales data analysis

# Importing the libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Importing the dataset
dataset = pd.read_csv('sales_data_sample.csv', encoding = 'latin1')
dataset.head()

# Data Preprocessing
dataset = dataset.dropna()
dataset = dataset.drop_duplicates()
dataset = dataset[dataset['SALES'] > 0]
dataset = dataset[dataset['QUANTITYORDERED'] > 0]
dataset = dataset[dataset['PRICEEACH'] > 0]
dataset = dataset[dataset['ORDERNUMBER'] > 0]
dataset = dataset[dataset['ORDERLINENUMBER'] > 0]
dataset = dataset[dataset['QTR_ID'] > 0]
dataset = dataset[dataset['MONTH_ID'] > 0]
dataset = dataset[dataset['YEAR_ID'] > 0]
dataset = dataset[dataset['PRODUCTLINE'] != '']
dataset = dataset[dataset['MSRP'] > 0]
dataset = dataset[dataset['PRODUCTCODE'] != '']
dataset = dataset[dataset['CUSTOMERNAME'] != '']
dataset = dataset[dataset['PHONE'] != '']
dataset = dataset[dataset['ADDRESSLINE1'] != '']
dataset = dataset[dataset['CITY'] != '']
dataset = dataset[dataset['STATE'] != '']
dataset = dataset[dataset['POSTALCODE'] != '']
dataset = dataset[dataset['COUNTRY'] != '']
dataset = dataset[dataset['TERRITORY'] != '']
dataset = dataset[dataset['CONTACTLASTNAME'] != '']
dataset = dataset[dataset['CONTACTFIRSTNAME'] != '']
dataset = dataset[dataset['DEALSIZE'] != '']

# Data Analysis
# Total Sales by Year
total_sales_by_year = dataset.groupby('YEAR_ID')['SALES'].sum()
total_sales_by_year.plot(kind='bar', color='blue')
plt.title('Total Sales by Year')
plt.xlabel('Year')
plt.ylabel('Total Sales')
plt.show()

# Total Sales by Quarter
total_sales_by_quarter = dataset.groupby('QTR_ID')['SALES'].sum()
total_sales_by_quarter.plot(kind='bar', color='green')
plt.title('Total Sales by Quarter')
plt.xlabel('Quarter')
plt.ylabel('Total Sales')
plt.show()

# Total Sales by Month
total_sales_by_month = dataset.groupby('MONTH_ID')['SALES'].sum()
total_sales_by_month.plot(kind='bar', color='red')
plt.title('Total Sales by Month')
plt.xlabel('Month')
plt.ylabel('Total Sales')
plt.show()

# Total Sales by Product Line
total_sales_by_product_line = dataset.groupby('PRODUCTLINE')['SALES'].sum()
total_sales_by_product_line.plot(kind='bar', color='purple')
plt.title('Total Sales by Product Line')
plt.xlabel('Product Line')
plt.ylabel('Total Sales')
plt.show()

# Total Sales by Territory
total_sales_by_territory = dataset.groupby('TERRITORY')['SALES'].sum()
total_sales_by_territory.plot(kind='bar', color='orange')
plt.title('Total Sales by Territory')
plt.xlabel('Territory')
plt.ylabel('Total Sales')
plt.show()


