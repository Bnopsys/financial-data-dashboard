from codefiles import *
import os


# move other files into an __init__ file later so i can import as * 
folder_path = '/Users/roddystones/Documents/datafiles'

modified_files_dict = {'Capital One': os.path.join(folder_path, 'func_data_files', 'capital_one_data.csv'), 
                       'Citi': os.path.join(folder_path, 'func_data_files', 'citi_data.csv'), 
                       'Navy Fed': os.path.join(folder_path, 'func_data_files', 'navyfed_data.csv')}

def refresh_csv():
    """
    This function links to the navy fed, citi, and capital one modules and processes their data into a standard format.
    """

    process_navy_fed()
    process_citi()
    process_capital_one()

def create_dfs() -> list:
    """
    By giving the get_company_list function *companies, it puts them into a list and uses list comprehension to get true or false values based on the company. 
    If all of the company validations come back without errors, then the all() function returns a list of files based on the companies.

    The df_list_func takes the given list of filepaths and returns a list of dataframes. 
    """
    company_list = get_company_list('Capital One', 'Citi', 'Navy Fed', company_dict=modified_files_dict)
    return df_list_func(company_list)


def merging_dfs(df_list: list, folder_path):
    """
    This function takes a list of dataframes and a path to where we'll save the main dataframe file.
    """
    merge_dataframes(df_list, folder_path)


if __name__ == '__main__':
    refresh_csv()
    merging_dfs(create_dfs(), folder_path)
    
