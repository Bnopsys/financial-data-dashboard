from codefiles import *
import os



# move other files into an __init__ file later so i can import as * 
folder_path = '/Users/roddystones/Documents/datafiles'

modified_files_dict = {'Capital One': os.path.join(folder_path, 'func_data_files', 'capital_one_data.csv'), 
                       'Citi': os.path.join(folder_path, 'func_data_files', 'citi_data.csv'), 
                       'Navy Fed': os.path.join(folder_path, 'func_data_files', 'navyfed_data.csv')}

budget_rough = {'Transportation': 400, 
                'Misc': 350, 
                'Groceries': 1100, 
                'Insurance': 500, 
                'Restaurants': 400, 
                'Boba': 150, 
                'Savings': 700}

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
    return read_data(os.path.join(folder_path, 'main_datafile.csv'))

def categorical_totals_func(df):
    """
    This function prints out dataframes categorically separated by the items in the list.

    This function has a dependency on the `current_categories()` function. It was a separate argument, 
    but I found it too confusing and decided to just implement it into the function directly.

    """
    # call with categorical_totals_func(mainframe, current_categories(mainframe))
    categorical_totals(df, current_categories(df))

def grocery_stores(df):
    """
    This function takes a list of different grocery stores(target, walmart, costco) and adds them to the grocery category 
    since theyre considered as merchandise initially.
    Put this function before create_categorical_dfs to organize before printing to terminal.
    """
    grocery_list = ['Tokyo Central', 'Costco whse', 'Target', 
                'WAL-MART', 'WM SUPERCENTER', 'TARGET', 
                'MARINE MART', 'NIJIYA MARKET', 'COSTCO WHSE', 
                'MIRAMAR MAIN']
    correcting_categories(df, shop_list=grocery_list, newloc='Groceries')

def boba_stores(df):
    """
    This function takes a list of different boba shops(Yifang, Sharetea, Happy Lemon) and adds them to a separate category for boba.
    Put this function before create_categorical_dfs to organize before printing to terminal.
    """ 
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
    correcting_categories(df, shop_list=boba_shops, newloc='Boba')


if __name__ == '__main__':
    refresh_csv()
    merging_dfs(create_dfs(), folder_path)
    mainframe = retrieving_main_df()
    boba_stores(mainframe)
    grocery_stores(mainframe)
    create_categorical_dfs(mainframe, current_categories(mainframe))
    tracking_payments(mainframe)
    
    categs_table = data_stats(mainframe, date='PastMonth')
    deviation = budget_deviation(categs_table['total_spend'], budget_rough)
    print(deviation)
    print('a')
    categorical_describe(mainframe, 'Groceries')
    # take the categorical list and remove outliers based on individual categorical outlier data and move to a new list
