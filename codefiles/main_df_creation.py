from .navy_fed_module import process_navy_fed
from .citi_module import process_citi
from .capital_one_module import process_capital_one
from .create_csvs import df_list_func, get_company_list
from .mergefiles import merge_dataframes
from .utils.utils import read_data
from os import path

folder_path = '/Users/roddystones/Documents/datafiles'
modified_files_dict = {'Capital One': path.join(folder_path, 'func_data_files', 'capital_one_data.csv'), 
                       'Citi': path.join(folder_path, 'func_data_files', 'citi_data.csv'), 
                       'Navy Fed': path.join(folder_path, 'func_data_files', 'navyfed_data.csv')}


class MainfileCreation:
    def __init__(self):
        pass

    def refresh_csvs(self, navyfed=False, citi=False, capitalone=False):
        """
        This function checks if the associated banks variables above are true. 
        Then finds their data files and proceses them into a standard format.
        TODO remove file locations so it can be more modular.
        """
        companylist = []
        if navyfed:
            process_navy_fed()
            companylist.append('Navy Fed')
        if capitalone:
            process_capital_one()
            companylist.append('Capital One')
        if citi:
            process_citi()
            companylist.append('Citi')
        return companylist
        

    def create_dfs(self, companies:list):
        company_list = get_company_list(companies=companies, company_dict=modified_files_dict)
        return df_list_func(company_list)


    def merge_dfs(self, df_list: list, folder_path: str):
        merge_dataframes(df_list, folder_path)

    def retrieving_main_df(self):
        return read_data(path.join(folder_path, 'main_datafile.csv'))
