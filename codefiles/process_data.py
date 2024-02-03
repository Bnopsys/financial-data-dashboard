import pandas as pd
import os
from data_cleaning import *

path_to_func_folder = '/Users/roddystones/Documents/datafiles/func_data_files'
path_to_data_folder = '/Users/roddystones/Documents/datafiles'

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
    
def does_company_exist(company):
    # check if provided company is in dictionary
    if company not in company_dict:
        raise ValueError('Invalid company: {}. Valid options are: {}'.format(company, list(company_dict.keys())))

def do_necessary_felds_exist(company):
    # check if the necessary data fields exist in the dictionary
    required_keys = ['Data File', 'Modified File', 'ResetCSVFunction']
    if not all(key in company_dict[company] for key in required_keys):
        raise KeyError('Missing necessary dictionary keys for company: {}. Make sure it includes {}'.format(company, required_keys))

def debit_credit_fields_exist(company):
    # does the company have debit/credit fields in the dictionary? if not return a different answer
    required_subkeys = ['Debit', 'Credit']
    if not all(subkey in company_dict[company]['Data File'] for subkey in required_subkeys):
        raise KeyError('Missing necessary sub-dictionary keys for company: {}. Make sure "Data File" includes: {}'.format(company, required_subkeys))

def refresh_csv():
    for company in company:
        try:
            does_company_exist(company)
            do_necessary_felds_exist(company)
            
            # check if the company has debit and credit or just a single file
            if company in ['Citi', 'Navy Fed']:
                debit_credit_fields_exist(company)
                
                # call the appropriate function with the necessary data
                company_dict[company]['ResetCSVFunction'](debit_csv= company_dict[company]['Data File']['Debit'], 
                                                            credit_csv= company_dict[company]['Data File']['Credit'])
                
            elif company == 'Capital One':
                company_dict[company]['ResetCSVFunction'](file= company_dict[company]['Data File'])

        except ValueError as ve:
            print('Value Error occured: ', ve)
            raise

        except KeyError as ke:
            print('Key Error occurred: ', ke)
            raise

def create_df(company):
    try:
        does_company_exist(company)
        do_necessary_felds_exist(company)
        return pd.read_csv(company_dict[company]['Modified File'], index_col=0)
        
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

def handle_multiple_dataframes():
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

        refresh_csv()
        dataframes_list = [create_df(x) for x in company]
        merge_financial_csvs(dataframes_list)
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

    refresh_csv()
    merge_financial_csvs([create_df(x) for x in company])
    print('Single Dataframe Sucess!')


if __name__ == '__main__':
    ...
    # Gameplan
    # refresh csv

