from codefiles import *
import os

budget_rough = {'Transportation': 400, 
                'Misc': 350, 
                'Groceries': 1100, 
                'Insurance': 500, 
                'Restaurants': 400, 
                'Boba': 150, 
                'Savings': 700}

if __name__ == '__main__':

    # grabs data from csv files, changes them into dataframes, merges them into one and accesses/exports data.
    mainframe = MainfileCreation()
    mainframe = mainframe.run()

    # adjust categories boba/grocery stores in dataframe using class: 
    Maindf(mainframe).run()
    print(mainframe)

    # TODO Now that my code isn't tied to any of these other functions start purging them.

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