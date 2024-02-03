import pandas as pd
import numpy as np
import os

# rules:
# 1. Dont call anything outside of functions: only lists, dictionaries, and variables
# 2. Functions only do ONE thing

# capital one---------------------------------------------------------------------------
path_of_data_folder = '/Users/roddystones/Documents/datafiles'
capital_one_file = os.path.join(path_of_data_folder, 'CapitalOneTrans.csv') # change name to match snake case

card_users = {9623: 'Reanne C.', 
              3176: 'Roderick S.'}

default_categories_cof = {'Other Services': 'Misc', 
                      'Merchandise': 'Merchandise', 
                      'Payment/Credit': 'Payment/FromCheckings', 
                      'Dining': 'Food', 
                      'Gas/Automotive': 'Transportation', 
                      'Insurance': 'Insurance', 
                      'Internet': 'Misc', 
                      'Entertainment': 'Entertainment'}

def read_data(datafile, skiprows=None):
    return pd.read_csv(datafile, skiprows=skiprows)
    

def add_users_map(df):
    df['User'] = df['Card No.'].map(card_users)
    return df['User']

def modify_cols(df, tablename, User=None, Date=None):
    df['Table'] = tablename
    if User != None:
        df['User'] = User
    if Date != None:
        df['Date'] = df[Date]
    df = df[['Date', 'User', 'Category', 'Description', 'Debit', 'Credit', 'Table']]
    return df

def func_default_categories(df, categroies_dict):
    df['Category'] = df['Category'].map(categroies_dict)
    return df['Category']

def set_datetime(df, col_name):
    df['Date'] = pd.to_datetime(df[col_name])
    df['Date'] = df['Date'].dt.date
    return df['Date']

def sort_on_date(df):
    df = df.sort_values(by=['Date'])
    df.reset_index(inplace=True, drop=True)
    return df

def send_to_csv(df):
    return df.to_csv(os.path.join(path_of_data_folder, 'func_data_files', 'capital_one_data.csv'))

"""if __name__ == '__main__':
    # basic capital one file
    df = read_data(capital_one_file)
    add_users_map(df)
    func_default_categories(df, default_categories_cof)
    set_datetime(df, 'Transaction Date')
    df = sort_on_date(df)
    df = modify_cols(df, 'Capital One')
    print(df)
    # send_to_csv(df)"""
    
# Citi ------------------------------------------------------------------------------------------------

debit_file = os.path.join(path_of_data_folder, 'CitiDebit.csv')
credit_file = os.path.join(path_of_data_folder, 'CitiCredit.csv')

default_categories_citi = {'Payment/FromCheckings': 'Payment/FromCheckings', 
                      'Restaurants': 'Food', 
                      'Vehicle Services': 'Transportation', 
                      'Merchandise': 'Merchandise', 
                      'Services': 'Misc'}

# debit

def filter_out_debit_charges(df):
    df_filter = df[df['Credit'] < 0]
    return df_filter

def positive_values_amounts(df, col_name):
    df[col_name] = df[col_name].abs()
    return df[col_name]

def payment_category(df):
    df['Category'] = 'Payment/FromCheckings'
    return df['Category']

def users_roderick(df):
    df['User'] = 'Roderick S.'
    return df['User']

def merge_dataframes(debit_df, credit_df):
    return pd.concat([debit_df, credit_df])

def func_default_categories_citi(df):
    df['Category'] = df['Category'].map(default_categories_citi)




"""if __name__ == '__main__':
    # debit
    debit_df = read_data(debit_file, skiprows=5)
    set_datetime(debit_df, 'Date')
    debit_df = modify_cols(debit_df, 'Citi', 'Roderick S.')
    
    # credit
    citi_credit_df = read_data(credit_file)
    citi_credit_df = filter_out_debit_charges(citi_credit_df)
    positive_values_amounts(citi_credit_df, 'Credit')
    payment_category(citi_credit_df)
    users_roderick(citi_credit_df)
    set_datetime(citi_credit_df, 'Date')
    citi_credit_df = modify_cols(citi_credit_df, 'Citi')

    # combined
    citi_merged_df = merge_dataframes(debit_df, citi_credit_df)
    citi_merged_df = sort_on_date(citi_merged_df)
    func_default_categories(citi_merged_df, default_categories_citi)
    send_to_csv(citi_merged_df)
    print(citi_merged_df)"""
    
# Navy Fed -------------------------------------------------------------------------------------------

checkings_file = os.path.join(path_of_data_folder, 'NavyFedCheckings.csv')
visa_credit_file = os.path.join(path_of_data_folder, 'NavyFedCredit.csv')

default_categories_navyfed = {'Restaurants/Dining': 'Food', 
                      'Groceries': 'Food', 
                      'Credit Card Payments': 'Payment/FromCheckings', 
                      'Income': 'Income',
                      'General Merchandise': 'Merchandise', 
                      'Payment/ToCredit': 'Payment/ToCredit'}

def determining_category(df):
    df['Category'] = np.where(df['Debit'].isna(), 'Income', 'Payment/ToCredit')
    return df['Category']

def converting_amount_indicator(df):
    df['Credit'] = np.where(df['Credit Debit Indicator'] == 'Credit', df['Amount'], 'NaN')
    df['Debit'] = np.where(df['Credit Debit Indicator'] == 'Debit', df['Amount'], 'NaN')
    return df['Credit'], df['Debit']



if __name__ == '__main__':
    # checkings
    checking_df = read_data(checkings_file)
    determining_category(checking_df)
    set_datetime(checking_df, 'Date')
    checking_df = modify_cols(checking_df,'Navy Fed', 'Roderick S.')
    
    # credit
    nf_credit_df = read_data(visa_credit_file)
    converting_amount_indicator(nf_credit_df)
    nf_credit_df = modify_cols(nf_credit_df, 'Navy Fed', User='Roderick S.', Date='Booking Date')
    set_datetime(nf_credit_df,'Date')
    
    # merged 
    nf_merged_df = merge_dataframes(checking_df, nf_credit_df)
    nf_merged_df = sort_on_date(nf_merged_df)
    func_default_categories(nf_merged_df, default_categories_navyfed)
    # send_to_csv(nf_merged_df)
    print(nf_merged_df)