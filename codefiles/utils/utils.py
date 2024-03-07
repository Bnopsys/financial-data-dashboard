import pandas as pd
import numpy as np
import os


# rules:
# 1. Dont call anything outside of functions: only lists, dictionaries, and variables
#   Good general rule but this is now a utils file so it is only functions
# 2. Functions only do ONE thing

def read_data(datafile, skiprows=None):
    return pd.read_csv(datafile, skiprows=skiprows)
    
def add_users_map(df, dict):
    df['User'] = df['Card No.'].map(dict)
    return df['User']

def modify_cols(df: pd.DataFrame, tablename=None, user=None, date=None):
    if user != None:
        df['User'] = user
        
    if date != None:
        df['Date'] = pd.to_datetime(df[date])
        df['Date'] = df['Date'].dt.date

    if tablename != None:
        df['Table'] = tablename

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

def send_to_csv(df, datafolder, outputfile):
    return df.to_csv(os.path.join(datafolder, 'func_data_files', outputfile))

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

def merge_dataframes(debit_df, credit_df):## make this function use *args
    return pd.concat([debit_df, credit_df])

def converting_amount_indicator(df):
    df['Credit'] = np.where(df['Credit Debit Indicator'] == 'Credit', df['Amount'], 'NaN')
    df['Debit'] = np.where(df['Credit Debit Indicator'] == 'Debit', df['Amount'], 'NaN')
    return df['Credit'], df['Debit']

def validate_in_dict(object, company_dict, keys: list = None):
    if keys != None:
        if not all(key in company_dict[object] for key in keys):
            raise KeyError('Missing necessary dictionary keys for company: {}. Make sure it includes {}'.format(object, keys))

    if object not in company_dict:
        raise ValueError('Invalid company: {}. Valid options are {}'.format(object, list(company_dict.keys())))
    
    return True

if __name__ == '__main__':
    functions_list = [func for func in dir() if callable(globals()[func]) and hasattr(globals()[func], '__call__')]
    print(functions_list)