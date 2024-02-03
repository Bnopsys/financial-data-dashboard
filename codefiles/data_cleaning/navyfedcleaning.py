import pandas as pd
import numpy as np
import os

# define checkings file
path_of_folder = '/Users/roddystones/Documents/datafiles'

checkings_file = os.path.join(path_of_folder, 'NavyFedCheckings.CSV')
visa_credit_file = os.path.join(path_of_folder, 'NavyFedCredit.csv')

default_categories = {'Restaurants/Dining': 'Food', 
                      'Groceries': 'Food', 
                      'Credit Card Payments': 'Payment/FromCheckings', 
                      'Income': 'Income',
                      'General Merchandise': 'Merchandise', 
                      'Payment/ToCredit': 'Payment/ToCredit'}


def checkings(file):
    checking_df = pd.read_csv(file)
    determining_category(checking_df)
    datetime_date(checking_df)
    return checking_df


def visa_credit(file):
    credit_df = pd.read_csv(file)
    adjusting_date_col(credit_df)
    converting_amount_indicator(credit_df)
    datetime_date(credit_df)
    return credit_df


def desired_col(df):
    df = df[['Date', 
             'User', 
             'Category', 
             'Description', 
             'Debit', 
             'Credit', 
             'Table']]
    return df
    
def adding_cols(df):
    df['User'] = 'Roderick S.'
    df['Table'] = 'Navy Fed'
    return df['User'], df['Table']

def converting_amount_indicator(df):
    df['Credit'] = np.where(df['Credit Debit Indicator'] == 'Credit', df['Amount'], 'NaN')
    df['Debit'] = np.where(df['Credit Debit Indicator'] == 'Debit', df['Amount'], 'NaN')
    return df['Credit'], df['Debit']

def determining_category(df):
    df['Category'] = np.where(df['Debit'].isna(), 'Income', 'Payment/ToCredit')
    return df['Category']

def adjusting_date_col(df):
    df['Date'] = df['Booking Date']
    return df['Date']

def datetime_date(df):
    df['Date'] = pd.to_datetime(df['Date'])
    df['Date'] = df['Date'].dt.date
    return df

def merging_checkings_credit(checkings_df, credit_df):
    merged_df = pd.concat([checkings_df, credit_df])
    adding_cols(merged_df)
    merged_df = desired_col(merged_df)
    merged_df = merged_df.sort_values(by=['Date'])
    merged_df.reset_index(inplace=True, drop=True)
    merged_df['Category'] = merged_df['Category'].map(default_categories)
    return merged_df

def navy_fed_to_csv(debit_csv, credit_csv):
    merged_df = merging_checkings_credit(
                                    checkings_df=checkings(debit_csv), 
                                    credit_df=visa_credit(credit_csv))
    
    return merged_df.to_csv(os.path.join(path_of_folder, 'func_data_files', 'navyfed_data.csv'))

if __name__ == '__main__': 
    checkings_df = checkings(checkings_file)
    credit_df = visa_credit(visa_credit_file)
    nfcu_df = merging_checkings_credit(checkings_df, credit_df)
    print(nfcu_df)