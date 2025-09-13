import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


try:
    #load the tips dataset
    url = 'https://raw.githubusercontent.com/mwaskom/seaborn-data/master/tips.csv'
    tips = pd.read_csv(url)
    print('data set loaded successfully')
except Exception as e:

    print(f"Failed to load dataset: {e}")
    exit()

try:
    #display the first few rows of the dataset
    print(tips.head())

    print(tips.info())
    print(tips.isnull().sum())

except Exception as e:
    print(f"Failed to display dataset information: {e}")
    

try:
    #compute basic statistics of numerical columns

    print(tips.describe())
    #group by sex and compute mean of total bill
    print(tips.groupby('sex')['total_bill'].mean())

except Exception as e:   
    print(f"Failed to perform basic data analysis: {e}")
    
   
try:
    #bar chart
    plt.figure(figsize=(10,6))
    sns.barplot(x='sex', y ='total_bill', data=tips)
    plt.title('Average Total Bill Accross Sex')
    plt.xlabel('Sex')
    plt.ylabel('Average Total Bill')
    plt.show()
except Exception as e:   
    print(f"Failed to create bar chart: {e}")
   
    #Histogram
try:
     plt.figure(figsize=(10,6))
     sns.histplot(tips['total_bill'], bins=10, kde=True)
     plt.title('Distribution of Total bills')
     plt.xlabel('Total Bill')
     plt.ylabel('Frequency')
     plt.show()
except Exception as e:   
    print(f"Failed to create histogram: {e}")
   
   
try:
    #Scatter plot
    plt.figure(figsize=(10,6))
    sns.scatterplot(x='total_bill', y ='tip', data=tips)
    plt.title('Relationship Between Total Bill and Tip')
    plt.xlabel('Total Bill')
    plt.ylabel('Tip')
    plt.show()
except Exception as e:   
    print(f"Failed to create Scatter plot: {e}")
   

try:
    #Box plot
    plt.figure(figsize=(10,6))
    sns.boxplot(x='day', y ='tip', data=tips)
    plt.title('Distribution of Tip across Day')
    plt.xlabel('Day')
    plt.ylabel('Tip')
    plt.show()
except Exception as e:   
    print(f"Failed to create box chart: {e}")
   

try:
    #line chart
    plt.figure(figsize=(10,6))
    sns.barplot(x='day', y ='total_bill', data=tips.groupby('day')['total_bill'].mean().reset_index())
    plt.title('Average Total Bill over Time')
    plt.xlabel('Day')
    plt.ylabel('Average Total Bill')
    plt.show();
except Exception as e:   
    print(f"Failed to create line chart: {e}")

