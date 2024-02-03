import pandas as pd
import os

path_of_folder = '/Users/roddystones/Documents/datafiles'

debit_file = os.path.join(path_of_folder, 'CitiDebit.CSV')
credit_file = os.path.join(path_of_folder, 'CitiCredit.CSV')

default_categories = {'Payment/Credit': 'Payment/FromCheckings', 
                      'Restaurants': 'Food', 
                      'Vehicle Services': 'Transportation', 
                      'Merchandise': 'Merchandise', 
                      'Services': 'Misc'}

def transactions_debit(file):
    debit_df = pd.read_csv(file, skiprows=5)
    user_col(debit_df, 'Roderick S.')
    datetime_date(debit_df)
    debit_df = desired_col(debit_df)
    return debit_df

# file for credit
def transactions_credit(credit_file):
    credit_df = pd.read_csv(credit_file)
    credit_df = filter_out_debit_charges(credit_df)
    positive_values_amounts(credit_df, 'Credit')
    credit_df['Category'] = 'Payment/Credit'
    user_col(credit_df, 'Roderick S.')
    datetime_date(credit_df)
    credit_df = desired_col(credit_df)
    return credit_df

def filter_out_debit_charges(dataframe):
    dataframe_filter = dataframe[dataframe['Credit'] < 0]
    return dataframe_filter 
# when returning a dataframe you need to save it as a new variable(or the same) to overwrite since its returning the whole thing not a col

def positive_values_amounts(dataframe, col_name):
    dataframe[f'{col_name}'] = dataframe[f'{col_name}'].abs()
    return dataframe[f'{col_name}']

def user_col(dataframe, user):
    dataframe['User'] = user
    return dataframe['User']

def datetime_date(dataframe):
    dataframe['Date'] = pd.to_datetime(dataframe['Date'])
    dataframe['Date'] = dataframe['Date'].dt.date
    return dataframe['Date']

def desired_col(dataframe):
    dataframe_cols_modified = dataframe[['Date', 'User', 'Category', 'Description', 'Debit', 'Credit']]
    return dataframe_cols_modified

def merge_citi_dataframes(debit_df, credit_df):
    citi_dataframe = pd.concat([debit_df, credit_df])
    citi_dataframe['Table'] = 'Citi'
    citi_dataframe = citi_dataframe.sort_values(by=['Date']) # had to set equal to dataframe for it to work
    citi_dataframe.reset_index(inplace=True, drop=True)
    citi_dataframe['Category'] = citi_dataframe['Category'].map(default_categories)
    return citi_dataframe

def citi_to_csv(debit_csv, credit_csv):
    merged_df = merge_citi_dataframes(
                                    debit_df=transactions_debit(debit_csv), 
                                    credit_df=transactions_credit(credit_csv))
    
    return merged_df.to_csv(os.path.join(path_of_folder, 'func_data_files', 'citi_data.csv'))


if __name__ == '__main__':
    credit = transactions_credit(credit_file)
    debit = transactions_debit(debit_file)
    citi_dataframe = merge_citi_dataframes(debit, credit)
    print(citi_dataframe)