import pandas as pd
import numpy as np # look more into numpy for extra data
from codefiles.utils.utils import read_data

grocery_list = ['Tokyo Central', 'Costco', 'Target', 
                'WAL-MART', 'WM SUPERCENTER', 'TARGET', 
                'MARINE MART', 'NIJIYA MARKET', 'COSTCO WHSE', 
                'MIRAMAR MAIN']

boba_shops = [
    "SHARETEA",
    "MOSHI MOSHI TEA",
    "UEP*LA CHA",
    "TASTEA-",
    "CHICHA SAN CHEN",
    "HAPPY LEMON",
    "YIFANG FRUIT TEA",
    "ARTEAZEN HAND CRAFTED TE",
    "BOBA LOVE",
    "CAFE PRUVIA"]

def access_dataframe(filepath): # could be unnecessary. look into just calling read_data in function call
    """
    wrapper function that invokes the read_data function from utils.
    It's only one line of code but for the sake of saving my __init__ file from importing directly from utils, this wrapper is used
    to create an inbetween.
    """
    return read_data(filepath)

def current_categories(df):
    unique_categories = list(df['Category'].drop_duplicates())
    return unique_categories

def create_categorical_dfs(df: pd.DataFrame, unique_categories: list):
    """
    this returns a list of dataframes that we can iterate over based on category.
    """
    
    # return {f'{category} Dataframe': df.loc[df['Category'] == category] for category in unique_categories}
    for category in unique_categories:
        print(f'{category} Dataframe')
        current_df: pd.DataFrame = df.loc[df['Category'] == category]
        current_df = current_df.sort_values(by=['Date'])
        print(current_df)
        print(f'Total: {sum_debit_credit_cols(current_df)}') # comment out if you would prefer the totals to be in a separate dict
        print('')

def categorical_totals(df: pd.DataFrame, unique_categories: list):
    """
    This function prints the dataframe and then the total balance on it. Lastly the category and amount are added to a dictionary and returned.
    """
    totals_dict = {}
    for category in unique_categories:
        print(f'{category} Dataframe: ')
        df1 = df.loc[df['Category'] == category]
        print(f'Total: {sum_debit_credit_cols(df1)}')
        print('')
        totals_dict[category] = sum_debit_credit_cols(df1)
    
    return totals_dict

def sum_debit_credit_cols(df: pd.DataFrame) -> float:
    """
    Used in the categorical_totals function to get the total debit and credit amounts per row. 
    """
    running_total = 0.0
    for _, row in df.iterrows():
        debit_val = convert_to_float(row['Debit'])
        credit_val = convert_to_float(row['Credit'])

        running_total += debit_val - credit_val
    
    return running_total

def convert_to_float(val):
    """
    Simple function the does some validation then returns the value as a float for calculation in the sum_debit_credit_cols function.
    """
    if pd.isna(val) or val == '':
        return 0.0
    
    try:
        return float(val)
    except ValueError:
        return 0.0

def find_top_five_purchases(df: pd.DataFrame):
    df = df.loc[df['Category'] != 'Payment/ToCredit']
    df = df.sort_values(by=['Debit'], ascending=False)
    return df.head(5)

def correcting_categories(df: pd.DataFrame, shop_list, newloc):
    for item in shop_list:
        mask = df['Description'].str.contains(item, case=False)
        df.loc[mask, 'Category'] = newloc

def identifying_payments(df: pd.DataFrame):
    credit_df = df.loc[df['Category'] == 'Payment/FromCheckings']
    payment_total = 0
    for _, row in credit_df.iterrows():
        payment: float = row['Debit']
        if pd.isna(payment) or payment == '':
            continue
        payment_total += payment

    return payment_total
