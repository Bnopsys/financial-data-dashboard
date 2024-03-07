import pandas as pd
import numpy as np # look more into numpy for extra data
from codefiles.data_assist import boba_shops, grocery_list

class Maindf:
    """
    The purpose of this class is to take the product of main_df_creation(name subject to change) and make base changes to it.
    
    Think of this class as restructuring the bones of the data. It handles bigger operations (moving lines to different categories)

    After execution of this class the next class that takes the data will analyze it/prepare it for the visualization phase.
    
    """
    def __init__(self, df: pd.DataFrame):
        self.data = df

    def correcting_categories(self, shop_list: list, newloc: str):
        for item in shop_list:
            mask = self.data['Description'].str.contains(item, case=False)
            self.data.loc[mask, 'Category'] = newloc # TODO  what does this mean with the .loc/ learn all the different uses for .loc

    def run(self):
        """
        Public method to run everything. Its job is to combine the differnt methods together and run everything 
        in the correct order rather than chaining different events. 

        TODO change this so make it more scalable.
        """
        # correct categories
        dict_of_cats_to_correct = {'Boba':boba_shops, 'Groceries': grocery_list}
        for category, shoplist in dict_of_cats_to_correct.items():
            self.correcting_categories(shop_list=shoplist, newloc=category)

        return self.data

    
def current_categories(df):
    """
    This function drops duplicates in category column of dataframe and returns the list. This is used to create dataframes based on all categories.
    """
    unique_categories = list(df['Category'].drop_duplicates())
    return unique_categories

def create_categorical_dfs(df: pd.DataFrame, unique_categories: list):
    """
    this returns a list of dataframes that we can iterate over based on category.
    TODO make this into an excel file with different excel sheets (name is {category})
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
    Gets the sum of the debit column and subtracts the credit column to display the total for the table 
    """
    debit_var = df['Debit'].sum()
    credit_var = df['Credit'].sum()

    return debit_var - credit_var

def correcting_categories(df: pd.DataFrame, shop_list, newloc):
    """
    This function takes the dataframe, a list of stores and a new category to put them into to move the category of all items 
    containing the given word in its description.
    """
    for item in shop_list:
        mask = df['Description'].str.contains(item, case=False)
        df.loc[mask, 'Category'] = newloc # TODO  what does this mean with the .loc/ learn all the different uses for .loc




if __name__ == "__main__":
    mainfile = '/Users/roddystones/Documents/datafiles/main_datafile.csv'
    exportpath = '/Users/roddystones/Documents/datafiles/main_df_test.xlsx'

    df = pd.read_csv(mainfile)
    
    # using class
    main_df_tsting = Maindf(df, exportpath)
    main_df_tsting.run()
