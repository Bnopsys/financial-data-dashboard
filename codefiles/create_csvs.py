import os
import pandas as pd
from codefiles.utils.utils import validate_in_dict


def df_list_func(file_list: list):
    """
    takes a list of files and creates dataframes based on them.
    """
    try:
        return [pd.read_csv(file, index_col=0) for file in file_list]
        
    except ValueError as ve:
        print('Value Error Occured: ', ve)
        raise

    except KeyError as ke:
        print('Key Error Occured: ', ke)
        raise

    # TODO make sure this is working since this is the missing link in the main file. 
    # Currently I can refresh the csv and also merge the dataframes but i need to provide the dataframes from this

def get_company_list(*companies, company_dict):
    """
    Takes a list of company strings and converts them to a list and validates them on our dictionary. Returns: file list for companies.
    """
    companies = list(companies)
    if all([validate_in_dict(x, company_dict) for x in companies]):
        return [company_dict[x] for x in companies] # this gets a list of the file locations; I need to get the dataframes so I'll need to create df's first.