import pandas as pd
import numpy as np
import kaggle 
import os 

def get_outliers(sales_data):
    print('Outliers by week \n')
    sales_np_array = np.array(sales_data.loc[:, sales_data.columns[1:53]])
    print("\n")
    for row in sales_np_array:
        mean = np.mean(row)
        std  = np.std(row)
        scores = [(i-mean) / std for i in row]
        index_data = np.array(np.where(np.abs(scores) > 3)).tolist()
        print(sales_data.columns[[i for index in index_data for i in index ]])
    


def bi_weekly(sales_data): 
    print('Bi Weekly 5 Lowest product \n')
    col1 = sales_data.columns[1::2]
    col2 = sales_data.columns[2::2]
    print(sales_data.columns)
    for i in range(0,len(col1)):
        sales_data['temp'] = sales_data[col1[i]] + sales_data[col2[i]]
        print (col1[i] +' '+ col2[i])
        print(sales_data.sort_values(by=['temp'])['Product_Code'].head(5))
    sales_data.drop(columns=['temp'])

def promising_product(sales_data):
    print('Promising Product \n')
    print(sales_data.loc[sales_data.diff(axis=1).sum(axis=1).idxmax(axis=0),['Product_Code']])


def best_performing(sales_data):
    print('Best Performing Product \n')
    print(sales_data.loc[sales_data.sum(axis=1).idxmax(axis=0),['Product_Code']] )

def basic_calculation(sales_data):
    print(sales_data[sales_data.columns[:53]].mean(axis=1).head(5))
    print(sales_data[sales_data.columns[:53]].median(axis=1).head(5))
    print(sales_data[sales_data.columns[:53]].max(axis=1).head(5))
    print(sales_data[sales_data.columns[:53]].min(axis=1).head(5))

def read_csv_file():
    path = os.getcwd()
    file_name = "Sales_Transactions_Dataset_Weekly.csv"
    url = 'https://www.kaggle.com/crawford/weekly-sales-transactions/downloads/Sales_Transactions_Dataset_Weekly.csv'
    k =  kaggle.download_from_kaggle(url, file_name, path)
    df = pd.read_csv(file_name)
    sales_data = df.loc[:, df.columns[:53]]
    return sales_data

def main():
    sales_data = read_csv_file() 
    #print(sales_data.head())
    basic_calculation(sales_data)
    best_performing(sales_data)
    promising_product(sales_data)
    bi_weekly(sales_data)
    get_outliers(sales_data)

if __name__ == '__main__':
    main()