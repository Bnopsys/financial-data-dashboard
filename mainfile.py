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


if __name__ == '__main__':

    # grabs data from csv files, changes them into dataframes, merges them into one and accesses/exports data.
    create_mainfile = MainfileCreation()

    company_list = create_mainfile.refresh_csvs(navyfed=True, citi=True, capitalone=True)
    df_list = create_mainfile.create_dfs(company_list)
    create_mainfile.merge_dfs(df_list=df_list, folder_path=folder_path)
    mainframe = create_mainfile.retrieving_main_df()

    # adjust categories boba/grocery stores in dataframe using class: 
    Maindf(mainframe).correct_boba_and_groceries()

    # try out datastats
    metrics_data = DataStats(df=mainframe, user='Roderick S.')
    print(metrics_data.data_cols())
    print(mainframe.loc[mainframe['Category'] == 'Transfers'])
