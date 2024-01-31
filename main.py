# CURRENTLY REFACTORING WITH CLASSES
# This files main purpose is to act as a top down perspective on whats happening.


import pandas as pd
from codefiles import citi_to_csv, cof_to_csv, navy_fed_to_csv
import matplotlib.pyplot as plt
from additionalresources.pysankey import sankey
import os

# files

path_to_func_folder = '/Users/roddystones/Documents/datafiles/func_data_files'
path_to_data_folder = '/Users/roddystones/Documents/datafiles' # learn how to use the path above and go back one level then add the filename.
citi_csv = os.path.join(path_to_func_folder, 'citi_data.csv')
cof_csv = os.path.join(path_to_func_folder, 'capitalone_data.csv')
navyfed_csv = os.path.join(path_to_func_folder, 'navyfed_data.csv')

class fiancial_df:
    def __init__(self, dataframe, category):
        self.dataframe = dataframe
        self.category = category
    
    def filter_category(self, dataframe, category):
        return dataframe.loc[dataframe['Category'] == category]
    




# TODO make a regex for finding which files are citi, cof, and navy fed. also for the files with two different 
#      files identify them.have it so i can iterate over a folder
# TODO look into functools as it has alot of helpful resources with classes/functions
# TODO working with all of the different dataframes created from mainframe
# TODO make a class for the visuals
# TODO make a class for dealing with retrieving data from the other files

def refresh_all_csv():
    citi_to_csv(debit_csv=os.path.join(path_to_data_folder, 'CitiTransactionsDebit.csv'), 
                credit_csv=os.path.join(path_to_data_folder, 'CitiTransactionsDecemberCredit.csv'))
    cof_to_csv(file=os.path.join(path_to_data_folder, 'captialoneTransactionsDecember.csv'))
    navy_fed_to_csv(checkings_csv=os.path.join(path_to_data_folder, 'NavyFedCheckings.csv'), credit_csv=os.path.join(path_to_data_folder, 'NavyFedCredit.csv'))



def create_df():
    citi_df = pd.read_csv(citi_csv, index_col=0)
    cof_df = pd.read_csv(cof_csv, index_col=0)
    navyfed_df = pd.read_csv(navyfed_csv, index_col=0)
    return citi_df, cof_df, navyfed_df




def merge_financial_csvs(citi, cof, navyfed):
    main_dataframe = pd.concat([citi, cof, navyfed], ignore_index=True)
    main_dataframe['Date'] = pd.to_datetime(main_dataframe['Date'])
    main_dataframe['Date'] = main_dataframe['Date'].dt.date
    main_dataframe = main_dataframe.sort_values(by=['Date'])
    main_dataframe.reset_index(inplace=True, drop=True)
    main_dataframe.to_csv(os.path.join(path_to_data_folder, 'main_datafile.csv'), index=0)



def creating_sankey(df):
    # - Find the source code for this on GitHub at: 'https://github.com/anazalea/pySankey' 
    # This really helps me make the financial diagram I'd like to use, since Matplotlib doesn't support it natively.
    sankey(
        df['User'], df['Category'], leftWeight=df['Debit'], 
        aspect=20, fontsize=12, figureName='DebitSankey'
    )



def access_mainframe():
    mainframe = pd.read_csv(os.path.join(path_to_data_folder, 'main_datafile.csv'))
    return mainframe



def barchart():
    ...



def scatterplot():
    ...


def stackedbarchart():
    ...




if __name__ == '__main__':
    # Step 1. Refresh CSV files to be current. Use functions from other files to do this process
    refresh_all_csv()

    # Step 2. Grab CSV files. Save return as dataframe(s)
    citi_df, cof_df, navyfed_df = create_df()

    # Step 3. Merge together dataframes so all information is centeralized for data analysis/visualization.
    merge_financial_csvs(citi_df, cof_df, navyfed_df)
    mainframe = access_mainframe()

    print(list(mainframe['Category'].drop_duplicates()))
    mainframe = mainframe.loc[mainframe['Category'] != 'Payment/ToCredit']

    # separate data into separate dataframes(categories, top 5 purchases, )



    # Step 4. Create Diagrams
    

# get an app to blur photos for the readme so i can blur out bank details