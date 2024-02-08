# CURRENTLY REFACTORING WITH CLASSES
# This files main purpose is to act as a top down perspective on whats happening.


import pandas as pd
from codefiles import *
import matplotlib.pyplot as plt
from additionalresources.pysankey import sankey
import os

# folder paths
path_to_func_folder = '/Users/roddystones/Documents/datafiles/func_data_files'
path_to_data_folder = '/Users/roddystones/Documents/datafiles'

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

    The company_dict dictionary below is used for validation in the place of explicit variables. This technique of storing companies as dictionary key, value pairs
    we get the modularity benifits that you can add new fields and there will be no change to the code.
    """

    company_dict = {'Citi': 
                        {'Data File': {'Debit': os.path.join(path_to_data_folder, 'CitiDebit.csv'), 
                                       'Credit': os.path.join(path_to_data_folder, 'CitiCredit.csv')}, 
                        'Modified File': os.path.join(path_to_func_folder, 'citi_data.csv'), 
                        'ResetCSVFunction': "citi_to_csv"}, 


                    'Capital One': 
                        {'Data File': os.path.join(path_to_data_folder, 'CapitalOneTrans.csv'), 
                         'Modified File': os.path.join(path_to_func_folder, 'capital_one_data.csv'), 
                         'ResetCSVFunction': "cof_to_csv"}, 


                    'Navy Fed': 
                        {'Data File': {'Debit': os.path.join(path_to_data_folder, 'NavyFedCheckings.csv'), 
                                       'Credit': os.path.join(path_to_data_folder, 'NavyFedCredit.csv')}, 
                         'Modified File': os.path.join(path_to_func_folder, 'navyfed_data.csv'), 
                         'ResetCSVFunction': "navy_fed_to_csv"}}
    

    def __init__(self, *company):
        self.company = list(company)
        
    def does_company_exist(self, company):
        # check if provided company is in dictionary
        if company not in self.company_dict:
            raise ValueError('Invalid company: {}. Valid options are: {}'.format(company, list(self.company_dict.keys())))
            
    def do_necessary_felds_exist(self, company):
        # check if the necessary data fields exist in the dictionary
        required_keys = ['Data File', 'Modified File', 'ResetCSVFunction']
        if not all(key in self.company_dict[company] for key in required_keys):
            raise KeyError('Missing necessary dictionary keys for company: {}. Make sure it includes {}'.format(company, required_keys))

    
    def debit_credit_fields_exist(self, company):
        # does the company have debit/credit fields in the dictionary? if not return a different answer
        required_subkeys = ['Debit', 'Credit']
        if not all(subkey in self.company_dict[company]['Data File'] for subkey in required_subkeys):
            raise KeyError('Missing necessary sub-dictionary keys for company: {}. Make sure "Data File" includes: {}'.format(company, required_subkeys))
    
    def refresh_csv(self):
        for company in self.company:
            try:
                self.does_company_exist(company)
                self.do_necessary_felds_exist(company)
                
                # check if the company has debit and credit or just a single file
                if company in ['Citi', 'Navy Fed']:
                    self.debit_credit_fields_exist(company)
                    
                    # call the appropriate function with the necessary data
                    self.company_dict[company]['ResetCSVFunction'](debit_csv= self.company_dict[company]['Data File']['Debit'], 
                                                                credit_csv= self.company_dict[company]['Data File']['Credit'])
                    
                elif company == 'Capital One':
                    self.company_dict[company]['ResetCSVFunction'](file= self.company_dict[company]['Data File'])

            except ValueError as ve:
                print('Value Error occured: ', ve)
                raise

            except KeyError as ke:
                print('Key Error occurred: ', ke)
                raise
    
    def create_df(self, company):
        try:
            self.does_company_exist(company)
            self.do_necessary_felds_exist(company)
            return pd.read_csv(self.company_dict[company]['Modified File'], index_col=0)
            
        except ValueError as ve:
            print('Value Error occured: ', ve)
            raise

        except KeyError as ke:
            print('Key Error occurred: ', ke)
            raise 
    
    def converting_to_datetime():
        ...

    def merge_financial_csvs(self, dataframes_list):
        """
        The core principal of this function is to concat all applicable datafrmes together.
        
        
        """
        main_dataframe = pd.concat(dataframes_list, ignore_index=True)
        main_dataframe['Date'] = pd.to_datetime(main_dataframe['Date'])
        main_dataframe['Date'] = main_dataframe['Date'].dt.date
        main_dataframe = main_dataframe.sort_values(by=['Date'])
        main_dataframe.reset_index(inplace=True, drop=True)
        main_dataframe.to_csv(os.path.join(path_to_data_folder, 'main_datafile.csv'), index=0)

    def handle_multiple_dataframes(self):
        """
        Used when working with multiple companies

        For example in this project I've been working with Capital One, Citi, and Navy Fed I would run the command:

        `maindf = ProcessData('Citi', 'Capital One', 'Navy Fed').handle_multiple_dataframes()`

        or 

        ```
        maindf = ProcessData('Citi', 'Capital One', 'Navy Fed')
        maindf.handle_multiple_dataframes()
        ```
        
        These two ways allow you to specify multiple companies in the same class. 
        """

        self.refresh_csv()
        dataframes_list = [self.create_df(x) for x in self.company]
        self.merge_financial_csvs(dataframes_list)
        print('Sucess!') # for testing the difference between single and multiple handler
    

    def handle_single_dataframe(self):
        """
        Used when working with a single company

        For example if I only want to see something with Citi I would run the command:
        `maindf = ProcessData('Citi').handle_single_dataframe()`

        or 

        ```
        maindf = ProcessData('Citi')
        maindf.handle_single_dataframe()
        ```
        
        This would let you only run the set of instructions on the single company.
        """

        self.refresh_csv()
        self.merge_financial_csvs([self.create_df(x) for x in self.company])
        print('Single Dataframe Sucess!')


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

# have functions here for grouped functions from codefiles


if __name__ == '__main__':
    # Step 1. Refresh CSV files to be current. Use functions from other files to do this process
    # Step 2. Grab CSV files. Save return as dataframe(s)

    maindf = ProcessData('Citi', 'Capital One', 'Navy Fed').handle_multiple_dataframes()
    mainframe = access_mainframe()

    # Step 3. Merge together dataframes so all information is centeralized for data analysis/visualization.
    # merge_financial_csvs(citi_df, cof_df, navyfed_df) # OLD WAY OF MERGING DATAFRAMES


    print(list(mainframe['Category'].drop_duplicates()))
    mainframe = mainframe.loc[mainframe['Category'] != 'Payment/ToCredit']

    # separate data into separate dataframes(categories, top 5 purchases, )



    # Step 4. Create Diagrams
    

# get an app to blur photos for the readme so i can blur out bank details