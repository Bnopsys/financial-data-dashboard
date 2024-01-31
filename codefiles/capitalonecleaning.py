import pandas as pd
import os

path_of_folder = '/Users/roddystones/Documents/datafiles'

datafile = os.path.join(path_of_folder, 'captialoneTransactionsDecember.csv')

card_users = {
        9623: 'Reanne C.', 
        3176: 'Roderick S.'}

def main(file):
    df = pd.read_csv(file)
    df = columns_modified(df)
    df = sort_and_index_reset(df)
    return df

default_categories = {'Other Services': 'Misc', 
                      'Merchandise': 'Merchandise', 
                      'Payment/Credit': 'Payment/FromCheckings', 
                      'Dining': 'Food', 
                      'Gas/Automotive': 'Transportation', 
                      'Insurance': 'Insurance', 
                      'Internet': 'Misc', 
                      'Entertainment': 'Entertainment'}

def columns_modified(df):
    df['User'] = df['Card No.'].map(card_users)
    df['Category'] = df['Category'].map(default_categories)
    df['Date'] = pd.to_datetime(df['Transaction Date'])
    df['Date'] = df['Date'].dt.date
    df['Table'] = 'Capital One'
    df = df[['Date', 
            'User', 
            'Category', 
            'Description', 
            'Debit', 
            'Credit', 
            'Table']]
    return df
    
def sort_and_index_reset(df):
    df = df.sort_values(by=['Date'])
    df.reset_index(inplace=True, drop=True)
    return df

def cof_to_csv(file):
    return main(file).to_csv(os.path.join(path_of_folder, 'func_data_files', 'capitalone_data.csv'))

if __name__ == '__main__':
    tableEx = main(datafile)
    print(tableEx)