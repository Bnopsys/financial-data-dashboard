import pandas as pd
import numpy as np # look more into numpy for extra data

def current_categories(df):
    """
    This function drops duplicates in category column of dataframe and returns the list. This is used to create dataframes based on all categories.
    """
    unique_categories = list(df['Category'].drop_duplicates())
    return unique_categories

def create_categorical_dfs(df: pd.DataFrame, unique_categories: list):
    """
    this returns a list of dataframes that we can iterate over based on category.
    """
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

def sum_debit_credit_cols(df: pd.DataFrame) -> float: # change this to using pandas vectorized functions then delete.
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

def correcting_categories(df: pd.DataFrame, shop_list, newloc):
    """
    This function takes the dataframe, a list of stores and a new category to put them into to move the category of all items 
    containing the given word in its description.
    """
    for item in shop_list:
        mask = df['Description'].str.contains(item, case=False)
        df.loc[mask, 'Category'] = newloc


