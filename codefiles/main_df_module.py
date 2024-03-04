import pandas as pd
import numpy as np # look more into numpy for extra data
from codefiles.data_assist import boba_shops, grocery_list

class Maindf:

    def __init__(self, df: pd.DataFrame, mainpath: str) -> None:
        self.data = df
        self.filepath = mainpath


    def current_categories_dict(self):
        """
        This function drops duplicates from the 'Category' Column and then uses this as a list in a dictionary composition to return 
        {Key='Category': Value='Dataframe of Category'}
        """
        unique_categories = list(self.data['Category'].drop_duplicates())
        return {category: self.data[(self.data['Category'] == category)] for category in unique_categories}


    def sort_dfs(self, categs_dict: dict):
        """
        TODO rather than returning a dict, this should just modify self.data so its only function is to sort the data.
        """
        return {category: df.sort_values(by=['Date']) for category, df in categs_dict.items()} # takes more than two values


    def create_excel(self, categs_dict):
        """
        This takes the categories_dict and turns it into an excel sheet to see all data.
        TODO make an extra sheet which has data like averages, totals and other metrics.
        TODO look up if its good practice to use except Exception as e.
        """
        try:
            with pd.ExcelWriter(self.filepath) as writer:
                for sheetname, df in categs_dict.items():
                    df = pd.DataFrame(df)
                    df.to_excel(writer, sheet_name=sheetname, index=False)
        
        except Exception as e:
            print(e)


    def totals_per_cat(self, categs_dict):
        totals_dict = {}
        for category, df in categs_dict.items():
            debit_var = df['Debit'].sum()
            credit_var = df['Credit'].sum()
            totals_dict[category] = debit_var - credit_var

        return pd.DataFrame(list(totals_dict.items()), columns=['Category', 'Total'])


    def correcting_categories(self, shop_list: list, newloc: str):
        for item in shop_list:
            mask = self.data['Description'].str.contains(item, case=False)
            self.data.loc[mask, 'Category'] = newloc # TODO  what does this mean with the .loc/ learn all the different uses for .loc


    def run(self):
        """
        Public method to run everything. Its job is to combine the differnt methods together and run everything in the correct order rather than chaining different events.
        """
        # correct categories
        dict_of_cats_to_correct = {'Boba':boba_shops, 'Groceries': grocery_list}
        for category, shoplist in dict_of_cats_to_correct.items():
            self.correcting_categories(shop_list=shoplist, newloc=category)

        # get dict
        categories_dict = self.current_categories_dict()
        
        # sort categories
        categories_dict = self.sort_dfs(categories_dict)

        # add totals 
        categories_dict['Total'] = self.totals_per_cat(categories_dict)
        # export to excel
        self.create_excel(categories_dict)

    
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


class MainfileProj:
    def __init__(self):
        ...
    # refresh csvs
    def refresh_csvs(self):
        ...
        # add process_{bank_acc}()s

    # create dfs
    def create_dfs(self):
        ...
        # make a list of companies, validate, then return files for each company
        # list comprehension changing files to dataframes for each company

    # merge dfs
    def merge_dfs(self):
        ...
        # use the dataframes list from create_dfs and merge them into one

    # get main df
    def main_df(self):
        ...
        # read_data for maindata file

    # rename/move purchases based on category(boba, grocery stores)
    def move_purchases(self):
        ...
        # take the grocery and boba lists aand correcting_categories for them

if __name__ == "__main__":
    mainfile = '/Users/roddystones/Documents/datafiles/main_datafile.csv'
    exportpath = '/Users/roddystones/Documents/datafiles/main_df_test.xlsx'

    df = pd.read_csv(mainfile)
    
    # using class
    main_df_tsting = Maindf(df, exportpath)
    main_df_tsting.run()
