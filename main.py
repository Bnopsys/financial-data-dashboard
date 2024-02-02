# CURRENTLY REFACTORING WITH CLASSES
# This files main purpose is to act as a top down perspective on whats happening.


import pandas as pd
from codefiles import *
import matplotlib.pyplot as plt
from additionalresources.pysankey import sankey
import os

# files

path_to_func_folder = '/Users/roddystones/Documents/datafiles/func_data_files'
path_to_data_folder = '/Users/roddystones/Documents/datafiles'
citi_csv = os.path.join(path_to_func_folder, 'citi_data.csv')
cof_csv = os.path.join(path_to_func_folder, 'capital_one_data.csv')
navyfed_csv = os.path.join(path_to_func_folder, 'navyfed_data.csv')

class Fiancial_df:
    """
    This class takes the category passed to it and filters down the main table with that criteria.

    TODO Use the categorical tables for individual analysis.
    """
    def __init__(self, dataframe, category):
        self.dataframe = dataframe
        self.category = category
    
    def filter_category(self, dataframe, category):
        return dataframe.loc[dataframe['Category'] == category]
    
class ProcessData:
    """
    This class takes the csv's passed and creates dataframes for each. While it may not need to be contained within a class, it adds structure to the file.
    """

    company_dict = {'Citi': 
                        {'Data File': {'Debit': os.path.join(path_to_data_folder, 'CitiDebit.csv'), 
                                       'Credit': os.path.join(path_to_data_folder, 'CitiCredit.csv')}, 
                        'Modified File': os.path.join(path_to_func_folder, 'citi_data.csv'), 
                        'ResetCSVFunction': citi_to_csv}, 


                    'Capital One': 
                        {'Data File': os.path.join(path_to_data_folder, 'CapitalOneTrans.csv'), 
                         'Modified File': os.path.join(path_to_func_folder, 'capital_one_data.csv'), 
                         'ResetCSVFunction': cof_to_csv}, 


                    'Navy Fed': 
                        {'Data File': {'Debit': os.path.join(path_to_data_folder, 'NavyFedCheckings.csv'), 
                                       'Credit': os.path.join(path_to_data_folder, 'NavyFedCredit.csv')}, 
                         'Modified File': os.path.join(path_to_func_folder, 'navyfed_data.csv'), 
                         'ResetCSVFunction': navy_fed_to_csv}}
    

    def __init__(self, company):
        self.company = company
        

    def refresh_csv(self):
        try:
            # check if provided company is in dictionary
            if self.company not in self.company_dict:
                raise ValueError('Invalid company: {}. Valid options are: {}'.format(self.company, list(self.company_dict.keys())))

            # check if the necessary data fields exist in the dictionary
            required_keys = ['ResetCSVFunction', 'Data File']
            if not all(key in self.company_dict[self.company] for key in required_keys):
                raise KeyError('Missing necessary dictionary keys for company: {}. Make sure it includes {}'.format(self.company, required_keys))
            
            # check if the company has debit and credit or just a single file
            if self.company in ['Citi', 'Navy Fed']:
                required_subkeys = ['Debit', 'Credit']
                if not all(subkey in self.company_dict[self.company]['Data File'] for subkey in required_subkeys):
                    raise KeyError('Missing necessary sub-dictionary keys for company: {}. Make sure "Data File" includes: {}'.format(self.company, required_subkeys))
                
                # call the appropriate function with the necessary data
                self.company_dict[self.company]['ResetCSVFunction'](debit_csv= self.company_dict[self.company]['Data File']['Debit'], 
                                                               credit_csv= self.company_dict[self.company]['Data File']['Credit'])
                
            elif self.company == 'Capital One':
                self.company_dict[self.company]['ResetCSVFunction'](file= self.company_dict[self.company]['Data File'])

        except ValueError as ve:
            print('Value Error occured: ', ve)
            raise

        except KeyError as ke:
            print('Key Error occurred: ', ke)
            raise
    
    def create_df(self):
        try:
            # company exists in dictionary
            if self.company not in self.company_dict:
                raise ValueError('Invalid company: {}. Valid options are: {}'.format(self.company, list(self.company_dict.keys())))

            # modified file exists in dictionary
            required_key = 'Modified File'
            if required_key not in self.company_dict[self.company]:
                raise KeyError('Missing necessary dictionary keys for company: {}. Make sure it includes {}'.format(self.company, required_key))

            return pd.read_csv(self.company_dict[self.company]['Modified File'], index_col=0)
            
        except ValueError as ve:
            print('Value Error occured: ', ve)
            raise

        except KeyError as ke:
            print('Key Error occurred: ', ke)
            raise 




# TODO make a regex for finding which files are citi, cof, and navy fed. also for the files with two different 
#      files identify them.have it so i can iterate over a folder
# TODO look up decorators and if I would benifit from using a config file
# TODO look into functools as it has alot of helpful resources with classes/functions
# TODO working with all of the different dataframes created from mainframe
# TODO make a class for the visuals
# TODO make a class for dealing with retrieving data from the other files


def merge_financial_csvs(citi_df, cof_df, navyfed_df):
    main_dataframe = pd.concat([citi_df, cof_df, navyfed_df], ignore_index=True)
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
    # Step 2. Grab CSV files. Save return as dataframe(s)

    citi = ProcessData(company='Citi')
    capital_One = ProcessData(company='Capital One')
    navy_Fed = ProcessData(company='Navy Fed')
    
    [x.refresh_csv() for x in [citi, capital_One, navy_Fed]]


    merge_financial_csvs(citi_df=citi.create_df(), 
                         cof_df=capital_One.create_df(), 
                         navyfed_df=navy_Fed.create_df())
    
    mainframe = access_mainframe()

    # Step 3. Merge together dataframes so all information is centeralized for data analysis/visualization.
    # merge_financial_csvs(citi_df, cof_df, navyfed_df) # OLD WAY OF MERGING DATAFRAMES


    print(list(mainframe['Category'].drop_duplicates()))
    mainframe = mainframe.loc[mainframe['Category'] != 'Payment/ToCredit']

    # separate data into separate dataframes(categories, top 5 purchases, )



    # Step 4. Create Diagrams
    

# get an app to blur photos for the readme so i can blur out bank details