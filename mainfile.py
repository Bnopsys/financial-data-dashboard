from codefiles import *
from os import path

budget_rough = {'Transportation': 400, 
                'Misc': 350, 
                'Groceries': 1100, 
                'Insurance': 500, 
                'Restaurants': 400, 
                'Boba': 150, 
                'Savings': 700}

folder_path = '/Users/roddystones/Documents/datafiles'
modified_files_dict = {'Capital One': path.join(folder_path, 'func_data_files', 'capital_one_data.csv'), 
                       'Citi': path.join(folder_path, 'func_data_files', 'citi_data.csv'), 
                       'Navy Fed': path.join(folder_path, 'func_data_files', 'navyfed_data.csv')}

if __name__ == '__main__':

    # grabs data from csv files, changes them into dataframes, merges them into one and accesses/exports data.
    create_mainfile = MainfileCreation()

    company_list = create_mainfile.refresh_csvs(navyfed=True, citi=True, capitalone=True)
    df_list = create_mainfile.create_dfs(company_list)
    create_mainfile.merge_dfs(df_list=df_list, folder_path=folder_path)
    mainframe = create_mainfile.retrieving_main_df()

    # adjust categories boba/grocery stores in dataframe using class: 
    Maindf(mainframe).run()
    print(mainframe)

    # TODO 1. decouple the run function of Maindf
    # TODO 2. start going through the different analytical data and ensure that they're still functional. 

    """create_categorical_dfs(mainframe, current_categories(mainframe))
    tracking_payments(mainframe)
    
    categs_table = data_stats(mainframe, date='PastMonth')
    deviation = budget_deviation(categs_table['total_spend'], budget_rough)
    mainframe, outliers_df = categorical_describe(mainframe, 'Groceries')
    print(outliers_df)"""
    # make a for loop or comprehension for the categorical describe to go over all categories.

    """
    TODO Transfer code from main_df_module thats used here to the class format.
    
    """