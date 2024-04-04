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

    company_list = create_mainfile.refresh_csvs()
    df_list = create_mainfile.create_dfs()
    create_mainfile.merge_dataframes(dataframes_list=df_list, folder_path=folder_path)
    mainframe = create_mainfile.retrieving_main_df()

    # adjust categories boba/grocery stores in dataframe using class: 
    Maindf(mainframe).correct_boba_and_groceries()

    std_outliers = StandardDeviationData(mainframe)
    print(std_outliers.run(['Groceries', 'Boba', 'Transfers']))
    # TODO this returns an outlier table but it doesnt change the amounts from the mainframe. fix this.
    # TODO look into analytical data file and remove useless metrics. Also add new ones that are more useful for plotting.

    """
    ideas: 
    * savings rate: the ratio of income to money going into savings.
    * total income, total expences, net income: main values to display on dashboard.
    * goal tracking: set a goal and see how much progress youve made towards it and the percentage added in the last month.
    * spending per day: track which days of the week are more expensive
    * discresionary spending: the amount spent on non-essential items like vacations, hobbies, dining out, entertainment. measure as a total or percentage of total earning/spending.
    """