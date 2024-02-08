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

def retrieving_main_df():
    return access_dataframe(os.path.join(folder_path, 'main_datafile.csv'))
    

def unique_categories_func(df):
    """
    how to call create_categorical_dfs(mainframe, current_categories(mainframe))
    """
    unique_categs = current_categories(df)
    categorical_dfs = create_categorical_dfs(df, unique_categs)
    return categorical_dfs
    

# get totals for gas money| why did we spend more than last month on gas
# how much for maintenance cost per month or 3 months
# military provides us 800 for food
# tracking payment to credit and from checkings
# how much we spend on clothing
# tracking higene items
# insurance
# how much we spend on liquor
# how much we spend on fast food/resturants
# move target, walmart, costco to groceries df

# make a boba regex to pick out the boba purchases.
# boba_identifier(mainframe)
def boba_func(df):
    """
    Wrapper to the boba_identifier() function. This isn't a great way to identify boba places but it does give me some insight 
    
    """
def top_five_func(df):
    return find_top_five_purchases(df)

def categorical_totals_func(df, unique_categories):
    # call with categorical_totals_func(mainframe, current_categories(mainframe))
    categorical_totals(df, unique_categories)

if __name__ == '__main__':
    refresh_csv()
    merging_dfs(create_dfs(), folder_path)
    mainframe = retrieving_main_df()
    # create_categorical_dfs(mainframe, current_categories(mainframe))
    print(boba_identifier(mainframe))
    

    
