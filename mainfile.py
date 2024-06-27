from codefiles import *

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
    create_mainfile = MainfileCreation(companylist=['navy fed', 'Capital One', 'Citi'])

    create_mainfile.refresh_csvs()
    df_list = create_mainfile.create_dfs()
    create_mainfile.merge_dataframes(dataframes_list=df_list, folder_path=folder_path)
    mainframe = create_mainfile.retrieving_main_df()

    # adjust categories boba/grocery stores in dataframe using class: 
    Maindf(mainframe).correct_boba_and_groceries()

    # Spending Per Category Data
    spending_per_cat_data = DataStats(mainframe).type_data(financial_type='Debit')['total_spend']
    
    # Current Monthly Total
    total_monthly_spending = DataStats(mainframe).current_expenses_total()
    print(total_monthly_spending)
    # currently trying to see why the data isnt getting filtered based on date when using the prior month and month to date functions.

    """
    ideas: 
    * savings rate: the ratio of income to money going into savings.
    * total income, total expences, net income: main values to display on dashboard.
    * goal tracking: set a goal and see how much progress youve made towards it and the percentage added in the last month.
    * spending per day: track which days of the week are more expensive

    * make a tracker for tasks in Project - legit tracker this time tho
    * discresionary spending: the amount spent on non-essential items like vacations, hobbies, dining out, entertainment. measure as a total or percentage of total earning/spending.
    """